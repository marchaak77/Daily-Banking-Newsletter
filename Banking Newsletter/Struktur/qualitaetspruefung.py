#!/usr/bin/env python3
"""Qualitaetspruefung fuer den taeglichen Financial Services Consulting Newsletter.

Prueft die fertige PDF maschinell gegen die harten Vorgaben aus Struktur.md,
BEVOR sie gepusht und per Mail versendet wird.

Aufruf:
    python3 qualitaetspruefung.py "Pfad/zur/20260813_Financial Services Consulting Newsletter.pdf"

Rueckgabewert:
    0  = alle Pruefungen bestanden, Versand freigegeben
    1  = mindestens eine Pruefung fehlgeschlagen, NICHT versenden

Benoetigt PyMuPDF:  pip install pymupdf
"""

import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("FEHLER: PyMuPDF fehlt. Installieren mit:  pip install pymupdf")


# --- Vorgaben aus Struktur.md -------------------------------------------------
MIN_QUELLEN = 45           # Abschnitt 6, Punkt 2
MAX_LEERRAUM_PT = 40       # Abschnitt 4.6, Seiten 1 bis 4
MAX_LEERRAUM_S5_PT = 80    # Abschnitt 4.6, Seite 5 (Quellenliste geht selten exakt auf)
SEITENZAHL = 5             # Abschnitt 11
FUSSZEILE_AB_Y = 815       # Fusszeile bei der Leerraum-Messung ausklammern
COVER_SPALTEN_X = [45.3, 222.8, 391.0]   # Abschnitt 12.2, 3x2-Raster
SPALTEN_TOLERANZ = 12      # pt

# --- Exakte Layoutmasse der Seiten 2 bis 5 (Abschnitt 12.2, aus der Vorlage gemessen) ---
KOPFBAND_UNTEN = 63.0      # Kopfband #05415A endet hier
SEITENBAND_UNTEN = 81.8    # Seitenband #008CC8 endet hier
TITEL_GROESSE = 12.5       # "Financial Services / Consulting Newsletter"
MASS_TOLERANZ = 2.5        # pt Spielraum
PRIMAER = "#05415A"
AKZENT = "#008CC8"

# --- Cover (Abschnitt 12.2) ---
KARTE_X0, KARTE_X1, KARTE_Y0 = 31.5, 564.0, 408.0   # weisse News-Karte
COVER_MAX_FLAECHEN = 8      # Vorlage hat 3; mehr deutet auf nachgebauten Verlauf

# --- Zulaessige Farben (Abschnitt 12.3) ---
PALETTE = {
    "#05415A",  # Primaerton Dunkelblau
    "#008CC8",  # Akzent-Blau
    "#7CBFDF",  # helles Akzent-Blau
    "#DCEBFA",  # Kernaussage-Box
    "#DBEAF2",  # rechte Spalte
    "#CFE0E9",  # Hero-Verlauf hell
    "#C3D9E4",  # Hero-Verlauf mittel
    "#1E2B33",  # Fliesstext
    "#8FA0AA",  # Sekundaertext grau
    "#4A5B66",  # Fusszeile grau
    "#AFD7EB",  # Untertitel im Kopfband
    "#FFFFFF",  # Weiss
    "#000000",  # Schwarz (Rahmen/Schatten)
}


def _hex(farbe):
    return '#%02X%02X%02X' % tuple(int(round(v * 255)) for v in farbe)


def pruefe_kopfbereich(doc, befunde):
    """Kopfband, Seitenband und Titelgroesse auf den Seiten 2 bis 5."""
    for i in range(1, min(5, len(doc))):
        seite = doc[i]
        nr = i + 1
        kopf = band = None
        for dr in seite.get_drawings():
            f, r = dr.get("fill"), dr["rect"]
            if not f or r.width < 500:
                continue
            h = _hex(f)
            if h == PRIMAER and r.y0 < 5:
                kopf = r.y1
            elif h == AKZENT and r.y0 < 120:
                band = r.y1

        if kopf is None:
            befunde.append((False, f"S{nr} Kopfband", "kein dunkelblaues Kopfband gefunden"))
        else:
            ok = abs(kopf - KOPFBAND_UNTEN) <= MASS_TOLERANZ
            befunde.append((ok, f"S{nr} Kopfband-Hoehe",
                            f"{kopf:.1f} pt (Vorlage {KOPFBAND_UNTEN})"))

        if band is None:
            befunde.append((False, f"S{nr} Seitenband", "kein Seitenband gefunden"))
        else:
            ok = abs(band - SEITENBAND_UNTEN) <= MASS_TOLERANZ
            befunde.append((ok, f"S{nr} Seitenband-Ende",
                            f"{band:.1f} pt (Vorlage {SEITENBAND_UNTEN})"))

        # Titelgroesse im Kopfband
        groessen = [
            s["size"]
            for b in seite.get_text("dict")["blocks"] if b["type"] == 0
            for l in b["lines"] for s in l["spans"]
            if s["bbox"][1] < 40 and "Financial Services" in s["text"]
        ]
        if groessen:
            g = groessen[0]
            ok = abs(g - TITEL_GROESSE) <= MASS_TOLERANZ
            befunde.append((ok, f"S{nr} Titel-Schriftgroesse",
                            f"{g:.1f} pt (Vorlage {TITEL_GROESSE})"))


def pruefe_cover_aufbau(doc, befunde):
    """Cover: weisse Karte an der richtigen Stelle, kein nachgebauter Verlauf."""
    if not len(doc):
        return
    seite = doc[0]

    # 1) genau ein eingebettetes Bild
    n_bilder = len(seite.get_images())
    befunde.append((n_bilder == 1, "S1 Hero-Bild",
                    f"{n_bilder} Bild(er) eingebettet (erwartet 1)"))

    # 2) keine gestapelten Streifen
    flaechen = [d for d in seite.get_drawings()
                if d.get("fill") and d["rect"].width > 80 and d["rect"].height > 5]
    ok = len(flaechen) <= COVER_MAX_FLAECHEN
    befunde.append((ok, "S1 Aufbau",
                    f"{len(flaechen)} Zeichenflaechen (Vorlage 3, erlaubt bis {COVER_MAX_FLAECHEN}) "
                    f"{'— Verlauf nachgebaut?' if not ok else ''}"))

    # 3) weisse Karte an der richtigen Stelle
    karte = None
    for d in flaechen:
        r, f = d["rect"], d["fill"]
        if _hex(f) == "#FFFFFF" and 300 < r.y0 < 500 and r.width > 400:
            karte = r
            break
    if karte is None:
        befunde.append((False, "S1 weisse Karte", "keine weisse News-Karte gefunden"))
    else:
        passt = (abs(karte.x0 - KARTE_X0) <= MASS_TOLERANZ
                 and abs(karte.x1 - KARTE_X1) <= MASS_TOLERANZ
                 and abs(karte.y0 - KARTE_Y0) <= MASS_TOLERANZ)
        befunde.append((passt, "S1 weisse Karte",
                        f"x {karte.x0:.1f}–{karte.x1:.1f}, y {karte.y0:.1f} "
                        f"(Vorlage x {KARTE_X0}–{KARTE_X1}, y {KARTE_Y0})"))


def pruefe_farbpalette(doc, befunde):
    """Es darf keine Farbe ausserhalb der Palette aus Abschnitt 12.3 vorkommen."""
    fremd = {}
    for seite in doc:
        for d in seite.get_drawings():
            for key in ("fill", "color"):
                f = d.get(key)
                if not f:
                    continue
                h = _hex(f)
                if h not in PALETTE:
                    fremd[h] = fremd.get(h, 0) + 1
    if not fremd:
        befunde.append((True, "Farbpalette", "nur Farben aus Abschnitt 12.3"))
    else:
        top = ", ".join(f"{k} ({v}x)" for k, v in sorted(fremd.items(), key=lambda x: -x[1])[:4])
        befunde.append((False, "Farbpalette",
                        f"{len(fremd)} Fremdfarbe(n): {top}"))


def pruefe_kernaussage_box(doc, befunde):
    """Nur Seite 2 traegt die Kernaussage-Box (Vorlage: Seiten 3 und 4 haben keine)."""
    if len(doc) < 2:
        return
    hat_titel = "KERNAUSSAGE DES TAGES" in doc[1].get_text().upper()
    befunde.append((hat_titel, "S2 Kernaussage-Titel",
                    "vorhanden" if hat_titel else "Titel 'KERNAUSSAGE DES TAGES' fehlt"))


def pruefe_spaltenueberschriften(doc, befunde):
    """Beide Spalten brauchen ihre Ueberschrift. Links wechselt der Text je Seite."""
    erwartet_links = {1: ("NACHRICHTENLAGE",),
                      2: ("NACHRICHTENLAGE",),
                      3: ("ZAHLEN DES TAGES", "NACHRICHTENLAGE")}
    for i, varianten in erwartet_links.items():
        if i >= len(doc):
            continue
        oben = doc[i].get_text().upper()
        links = any(v in oben for v in varianten)
        rechts = "BANKING-CONSULTING" in oben or "BERATUNGSHEBEL" in oben
        befunde.append((links and rechts, f"S{i+1} Spaltenueberschriften",
                        f"links {'OK' if links else 'FEHLT (' + varianten[0] + ')'}, "
                        f"rechts {'OK' if rechts else 'FEHLT'}"))


def pruefe_seitenzahl(doc, befunde):
    ok = len(doc) == SEITENZAHL
    befunde.append((ok, "Seitenzahl",
                    f"{len(doc)} Seiten (erwartet {SEITENZAHL})"))


def pruefe_fuellung(doc, befunde):
    """Jede Seite muss bis kurz vor die Fusszeile gefuellt sein."""
    for i, seite in enumerate(doc, start=1):
        unterkante = 0.0
        for block in seite.get_text("dict")["blocks"]:
            if block["type"] == 0 and block["bbox"][3] < FUSSZEILE_AB_Y:
                unterkante = max(unterkante, block["bbox"][3])
        leerraum = FUSSZEILE_AB_Y - unterkante
        grenze = MAX_LEERRAUM_S5_PT if i == 5 else MAX_LEERRAUM_PT
        ok = leerraum <= grenze
        befunde.append((ok, f"Seite {i} gefuellt",
                        f"{leerraum:.0f} pt Leerraum unten (erlaubt bis {grenze})"))


def pruefe_quellenzahl(doc, befunde):
    """Seite 5 muss mindestens MIN_QUELLEN APA-Eintraege listen."""
    if len(doc) < 5:
        befunde.append((False, "Quellenzahl", "Seite 5 fehlt"))
        return
    text = doc[4].get_text()
    # APA-Muster: "Autor. (Jahr...)." bzw. "(2026, 4. August)."
    treffer = re.findall(r'\((?:19|20)\d{2}[^)]{0,40}\)\.', text)
    anzahl = len(treffer)
    ok = anzahl >= MIN_QUELLEN
    befunde.append((ok, "Quellen auf Seite 5",
                    f"{anzahl} Eintraege (Mindestmass {MIN_QUELLEN})"))


def pruefe_cover_raster(doc, befunde):
    """Cover muss das 3x2-Raster haben, nicht 2 oder 1 Spalte."""
    if not len(doc):
        befunde.append((False, "Cover-Raster", "keine Seiten"))
        return
    seite = doc[0]
    x_werte = []
    for block in seite.get_text("dict")["blocks"]:
        if block["type"] == 0 and block["bbox"][1] > 400:   # unterhalb des Hero-Bilds
            x_werte.append(round(block["bbox"][0], 1))

    gefunden = []
    for soll in COVER_SPALTEN_X:
        if any(abs(x - soll) <= SPALTEN_TOLERANZ for x in x_werte):
            gefunden.append(soll)
    ok = len(gefunden) == 3
    befunde.append((ok, "Cover 3x2-Raster",
                    f"{len(gefunden)} von 3 Spaltenkanten gefunden "
                    f"(erwartet bei x={COVER_SPALTEN_X})"))


def pruefe_quellenangaben_innenseiten(doc, befunde):
    """Seiten 2 bis 4 brauchen Kurzbelege in der linken Spalte."""
    for i in (1, 2, 3):
        if i >= len(doc):
            befunde.append((False, f"Quellenangaben Seite {i+1}", "Seite fehlt"))
            continue
        # nur linke Spalte betrachten
        links = doc[i].get_text("dict")
        text = " ".join(
            span["text"]
            for block in links["blocks"] if block["type"] == 0
            for line in block["lines"] for span in line["spans"]
            if block["bbox"][0] < 300
        )
        belege = re.findall(r'\([A-ZÄÖÜ][^()]{2,60},\s*(?:19|20)\d{2}\)', text)
        ok = len(belege) >= 5
        befunde.append((ok, f"Quellenangaben Seite {i+1} links",
                        f"{len(belege)} Kurzbelege gefunden (mindestens 5 erwartet)"))


def pruefe_prozentschreibweise(doc, befunde):
    """Im Text darf 'Prozent' nicht ausgeschrieben stehen."""
    treffer = 0
    for seite in doc:
        treffer += len(re.findall(r'\bProzent\b', seite.get_text()))
    ok = treffer == 0
    befunde.append((ok, "Schreibweise %",
                    f"{treffer}x 'Prozent' ausgeschrieben (erlaubt: 0, nur '%')"))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pfad = Path(sys.argv[1])
    if not pfad.exists():
        sys.exit(f"FEHLER: Datei nicht gefunden: {pfad}")

    doc = fitz.open(pfad)
    befunde = []

    pruefe_seitenzahl(doc, befunde)
    pruefe_cover_raster(doc, befunde)
    pruefe_cover_aufbau(doc, befunde)
    pruefe_farbpalette(doc, befunde)
    pruefe_kopfbereich(doc, befunde)
    pruefe_kernaussage_box(doc, befunde)
    pruefe_spaltenueberschriften(doc, befunde)
    pruefe_fuellung(doc, befunde)
    pruefe_quellenzahl(doc, befunde)
    pruefe_quellenangaben_innenseiten(doc, befunde)
    pruefe_prozentschreibweise(doc, befunde)
    doc.close()

    print(f"\nQUALITAETSPRUEFUNG  —  {pfad.name}\n" + "=" * 72)
    for ok, titel, detail in befunde:
        print(f"  [{'OK  ' if ok else 'FEHL'}]  {titel:32} {detail}")

    fehler = [b for b in befunde if not b[0]]
    print("=" * 72)
    if fehler:
        print(f"ERGEBNIS: {len(fehler)} Pruefung(en) fehlgeschlagen.")
        print("Der Newsletter ist NICHT fertig. Nicht pushen, nicht versenden.\n")
        return 1
    print("ERGEBNIS: Alle Pruefungen bestanden. Versand freigegeben.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

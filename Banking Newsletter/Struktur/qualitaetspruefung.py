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

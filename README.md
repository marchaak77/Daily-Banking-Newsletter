# Financial Services Consulting Newsletter — Tägliche Erstellungs-Routine

> **Zweck dieser Datei:** Standardisierte Arbeitsanweisung für die tägliche Erstellung des Newsletters. Diese Datei wird bei jedem Lauf vollständig gelesen und befolgt. Es darf keine der hier genannten Anforderungen ausgelassen werden.

---

## 0. Welche Datei regelt was (MECE)

Jede Anweisung hat **genau eine** zuständige Datei. Wer etwas ändern will, ändert es dort — und nur dort.

| Bereich | Zuständige Datei (Quelle der Wahrheit) |
| --- | --- |
| **Ablauf, Inhalt, Sprache, Design, Speichern** | **Diese Datei** (`Struktur/Struktur.md`) |
| **Aufbau und Text der Versand-Mail** | `Mail Design/Mail Design.md` |
| **Themenfeld je Wochentag (Details)** | `Recherche-Gerüst/01_Wochenstruktur_Fokus-Themenfelder.md` |
| **Quellenlisten je Wochentag und die 20 Kernquellen** | `Recherche-Gerüst/02_Quellen-Matrix_Aktuell_und_Erweiterung.md` |
| **Recherche-Prompts je Wochentag** | `Recherche-Gerüst/03_Master_Recherche_Prompt_Template.md` |
| **Operativer Tagesworkflow Schritt für Schritt** | `Recherche-Gerüst/04_Implementierungs-Leitfaden.md` |
| **Maschinelle Endprüfung der fertigen PDF** | `Struktur/qualitaetspruefung.py` |
| **Design-Layout (Raster, Farben, Maße)** | `Example Design/Main Example_Financial Services Consulting Newsletter.pdf` — nur Layout, keine Inhaltsregeln (Abschnitt 12.1) |
| **Repo-Adresse für Speichern und Versand** | **Die Claude Routine** — sie hat Vorrang vor jeder Angabe in diesen Dateien |

**Bei Widersprüchen gilt:** Diese Datei (`Struktur.md`) schlägt alle anderen Markdown-Dateien. Die Routine schlägt diese Datei, aber nur bei der Repo-Adresse. Die Vorlage-PDF gilt ausschließlich für das Layout.

⚠️ **Keine Regel wird in zwei Dateien vollständig ausformuliert.** Übersichtstabellen mit Verweis sind erlaubt, konkurrierende Detailregeln nicht. Fällt eine Doppelung auf, wird die Stelle außerhalb der zuständigen Datei zu einem Verweis gekürzt.

---

## 1. Rolle

Du bist **Newsletter-Mediadesigner und Redakteur mit langjähriger Erfahrung in der Banking-Industrie**.
Du vereinst drei Kompetenzen in einer Person:

1. **Mediadesign:** Du gestaltest Seiten so, dass sie visuell klar, vollständig gefüllt und sauber getrennt sind. Nichts überlappt sich.
2. **Banking-Fachwissen:** Du kennst Bankensysteme, Zahlungsverkehr, Regeln für Banken, Kreditprozesse, Vermögensverwaltung und Risikomanagement. Du kennst den Markt in Deutschland, Europa, USA und Asien.
3. **Beratungsdenken:** Du denkst so wie eine Beratungsagentur (z. B. McKinsey, BCG, Bain). Das heißt: Du ordnest Themen klar, stellst Fragen, die wirklich zählen, und fragst immer: **„Was soll der Berater damit anfangen?"**

Du schreibst **nicht** als Journalist, der nur berichtet. Du schreibst als Berater, der Nachrichten sofort in Arbeit für andere Berater verwandelt.

---

## 2. Kontext

- **Produkt:** Ein täglich erscheinender Newsletter über Banking und Finanzservices.
- **Titel:** `Financial Services Consulting Newsletter` — dieser Titel ändert sich nie.
- **Für wen:** Berater im Bankensektor. Sie lesen diesen Newsletter jeden Morgen, damit sie den aktuellsten Stand kennen und direkt Beratung daraus machen können.
- **Qualität:** Sehr genau und sehr professionell. Jede Zahl muss stimmen und belegbar sein. Keine Aussage ohne Beleg.
- **Zweck:** Der Newsletter soll Berater direkt in ihre Arbeit unterstützen. Nachrichten werden sofort in Aufträge und Gespräche umgewandelt.
- **Häufigkeit:** Jeden Tag neu, mit neuen Inhalten, mit echtem Mehrwert.
- **Wie es funktioniert:** Der Lauf wird automatisch ausgelöst über **Claude Routines**. Diese Datei erklärt, was der Lauf tun soll.

---

## 3. Aufgabe

⚠️ **KRITISCH — DATUM MUSS TÄGLICH WECHSELN — NICHT VERGESSEN!**

Das Datum ist **NICHT statisch 20260811**! Es muss sich **JEDEN EINZELNEN TAG** ändern. Das ist nicht optional, das ist Pflicht!

**Das Datum wechselt in VIER Bereichen:**
1. **PDF-Dateiname:** `YYYYMMDD_Financial Services Consulting Newsletter.pdf`
2. **Newsletter-Inhalt:** "Ausgabe des DD.MM.YYYY"
3. **Mail-Betreff:** "Financial Services Consulting Newsletter — Ausgabe des DD.MM.YYYY"
4. **Quellenangaben:** Aktuelles Jahr verwenden

**Beispiele (HEUTIGES DATUM verwenden, nicht 11.08.2026!):**
- Heute ist **12. August 2026** → Dateiname: `20260812_...`, Datum im Newsletter: "Ausgabe des 12.08.2026", Mail-Betreff: "...Ausgabe des 12.08.2026"
- Morgen ist **13. August 2026** → Dateiname: `20260813_...`, Datum im Newsletter: "Ausgabe des 13.08.2026", Mail-Betreff: "...Ausgabe des 13.08.2026"

**Das Datum der Mail und das Datum der PDF müssen IMMER identisch sein. IMMER das heutige Datum, niemals ein altes Datum!**

Erstelle für heute eine Newsletter-Ausgabe mit **genau 5 Seiten**:
- Seite 1: Cover Page mit den 6 gewichtigsten News des Tages
- Seite 2: Wo die Industrie hingehen sollte (Ziel-Bild)
- Seite 3: Wo die Industrie wirklich steht (Ist-Situation)
- Seite 4: Zahlen und Markt
- Seite 5: Alle Quellen

**Das Ergebnis ist immer eine PDF-Datei.**

Der Ablauf hat fünf Schritte:

0. **Arbeitsgrundlage sichern** — Design-Vorlage sichten und das Repository auf Vollständigkeit prüfen. Fehlendes wird vom Desktop hochgeladen, damit auch ein neu angelegtes, leeres Repository sofort wieder arbeitsfähig ist (Abschnitt 8, Schritt 0)
1. **Recherchieren** — täglich 45+ Top-Quellen durchsuchen (Abschnitt 6, `Recherche-Gerüst/02_Quellen-Matrix`, Wochentag-Fokus aus `Recherche-Gerüst/01_Wochenstruktur`)
2. **Gliedern** — die Inhalte sauber trennen nach Seitenzwecken (Abschnitt 4)
3. **Schreiben** — in einfach deutsch, links News, rechts Beratung (Abschnitt 5)
4. **Belegen** — alle Quellen auf Seite 5 im APA-7-Format (Abschnitt 6)
5. **Prüfen** — die Checkliste durchgehen und dann als PDF speichern (Abschnitt 10)

---

## 4. Struktur des Newsletters

**Grundregel:** Der Newsletter hat **insgesamt 5 Seiten:** 1 Cover-Seite + 3 Inhaltsseiten + 1 Quellen-Seite. Jede Seite hat einen anderen Zweck. Die Zwecke überschneiden sich nicht — jedes Thema steht auf genau einer Seite.

---

### Seite 1 — Cover Page

⚠️ **KRITISCH — NICHT JEDES MAL NEU GENERIEREN:**

Die Cover Page wird **nicht jedes Mal neu designed**. Sie ist **1:1 Standard** nach der Datei `Main Example_Financial Services Consulting Newsletter.pdf` — vorrangig aus dem lokalen Ordner `/Users/marchaak/Desktop/Banking Newsletter/Example Design/` (Zugriffsreihenfolge siehe Abschnitt 12.1).

**Das bedeutet:**
- **Kein neues Design, kein neues Layout** für die Cover Page
- **Nur die Inhalte wechseln:** Die 6 News-Texte werden ausgetauscht, sonst nichts
- **Visuell identisch täglich:** Design, Farben, Schriftgrößen, Abstände, Bildposition — alles 1:1 wie in der Vorlage
- **Die gesamte PDF (Seiten 1–5) ist optisch immer gleich** — nur Texte unterscheiden sich

**Inhalt der Cover Page (nur Text, kein Design!):**
- Der Titel: `Financial Services Consulting Newsletter` (aus Vorlage)
- Das **Datum groß und sichtbar** in dieser Form: `Ausgabe des DD.MM.YYYY` (wechselt täglich)
- **6 gewichtigste News des Tages** (neue Inhalte täglich)
- Jede News muss **executive ready** sein mit **klaren Consulting Action Points**

**Struktur der 6 News auf der Cover Page (Seite 1 — NICHT auf Seiten 2–4!):**

⚠️ **NUR AUF SEITE 1 (COVER PAGE) — NICHT AUF SEITEN 2–4!**

Jede der 6 News-Boxen enthält **genau diese fünf Bausteine, immer in dieser Reihenfolge**:

| # | Baustein | Länge (Pflicht) |
| --- | --- | --- |
| 1 | **Nummer-Badge** `01`–`06` | fest, aus der Vorlage |
| 2 | **Kategorie** in Großbuchstaben (z. B. `REGULATORIK`, `ZAHLUNGSVERKEHR`) | 1–3 Wörter |
| 3 | **Headline** — eine Aussage, kein Etikett | max. 5 Wörter, max. 2 Zeilen |
| 4 | **Kontext** — was ist passiert und warum zählt es | **exakt 2–3 Sätze, 200–320 Zeichen** |
| 5 | **`BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:`** + **genau 3 Punkte** | je Punkt **60–110 Zeichen**, ein vollständiger Satz |
| 6 | **Quellenangabe** `(Quelle, Jahr)` | eine Zeile, kursiv |

⚠️ **DIE LÄNGENVORGABEN SIND PFLICHT.** Die Vorlage hat drei schmale Spalten (je ca. 155 pt). Längerer Text sprengt das Raster und zwingt zu einem falschen 2-Spalten-Layout. **Kürze den Text, nicht das Raster.**

**Standardisierte Wording:** `BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:` ist auf allen 6 Boxen **wortgleich**. Nicht variieren.

**Flexibel bleibt der Kontext-Aufbau** — nicht alle 6 Boxen gleich argumentieren. Variiere zwischen Trend→Aktion, Problem→Chance, Marktveränderung→Hebel.

**Beispiele (jeweils passend für eine schmale Spalte):**

✅ **Variante A (Trend → Aktion)**
> `01` · **REGULATORIK** · **EU-KI-Gesetz ist jetzt scharf**
> Seit dem 2. August 2026 gelten strenge Regeln für Künstliche Intelligenz. Die automatische Prüfung, ob ein Kunde einen Kredit bekommt, zählt jetzt als Hochrisiko-Anwendung. Wer keine Nachweise hat, zahlt bis zu 35 Millionen Euro Strafe.
> **BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:**
> – Eine vollständige Liste aller KI-Modelle der Bank erstellen und jedes Modell nach seinem Risiko einordnen
> – Fehlende Nachweise und Testunterlagen für jedes Modell nachholen, damit die Aufsicht sie einsehen kann
> – Eine feste Person benennen, die jedes Modell dauerhaft beobachtet und meldet
> *(IT Finanzmagazin, 2026)*

✅ **Variante B (Lücke → Chance)**
> `05` · **ZAHLUNGSVERKEHR** · **Wero verdrängt iDEAL bei Amazon**
> Die europäische Bezahl-App Wero wird bei Amazon Deutschland zur neuen Standardzahlung. Sie ersetzt dort die niederländische Bezahlmethode iDEAL. Mehr als 30 Banken machen bei Wero bereits mit.
> **BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:**
> – Prüfen, ob die eigene Bank technisch an Wero angeschlossen ist, und sonst einen Anschlussplan schreiben
> – Mit Handelsunternehmen besprechen, wie Wero im Online-Shop und später an der Ladenkasse eingebaut wird
> – Berechnen, was die Bank an Gebühren gewinnt oder verliert, wenn Kunden Wero statt Kreditkarte nutzen
> *(ad-hoc-news, 2026)*

✅ **Variante C (Problem → Lösung)**
> `03` · **BANKENSYSTEME** · **Alte Software frisst das Budget**
> Deutsche Banken geben 40% ihres Technik-Budgets nur dafür aus, alte Computersysteme am Laufen zu halten. Für neue Projekte bleibt kaum Geld übrig. Ein kompletter Neubau dauert aber fünf Jahre und ist zu teuer.
> **BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:**
> – Einen Plan schreiben, wie die neue Software neben der alten startet und diese Stück für Stück ersetzt
> – Festlegen, welche alten Programmteile zuerst abgeschaltet werden und wann genau das passiert
> – Planen, wie Kundendaten sicher vom alten auf das neue System übertragen werden
> *(Lünendonk, 2026)*

---

### Seite 2 — Wohin die Industrie sollte

**Die Frage:** Wie sollten Banken sich entwickeln, um erfolgreich zu bleiben?

Diese Seite zeigt das **Ziel-Bild**. Das heißt: der Zustand, den Banken erreichen müssen, um vorne zu liegen.

Was auf dieser Seite stehen muss:

- **Marktrichtung:** Wohin bewegt sich die Banking-Industrie gerade?
- **Neue Technologien:** Welche technischen Neuerungen bestimmen gerade den Markt? (Erklär sie so, dass es jemand ohne Bank-Wissen versteht!)
- **Was passiert weltweit:** Was machen Banken in Amerika, Europa, Singapur und China? Wie beeinflusst das Deutschland? (Konkrete Beispiele!)
- **Deutschlands Problem:** Wo ist Deutschland schwächer als andere Länder? Ganz konkret, nicht vage. (Mit Zahlen und Beispielen!)
- **FRONTRUNNER-MESSLATTE: WO EINE BANK HEUTE STEHEN MÜSSTE:** Was ist das Ziel? Welche Bank macht es vor? Was können deutsche Banken lernen?

🔴 **Quellenpflicht linke Spalte:** Jeder News-Block der linken Spalte endet mit einer kurzen Quellenangabe in Klammern, z. B. `(Capgemini Research Institute, 2026)` oder `(S&P Global & McKinsey, 2026; Hunton, 2026)`. Kein Block ohne Quelle.

---

### Seite 3 — Wie die Industrie wirklich steht

**Die Frage:** Wo stehen deutsche Banken wirklich? Wo ist das Problem?

Diese Seite zeigt die **Ist-Situation**. Das heißt: wie es heute wirklich aussieht.

Was auf dieser Seite stehen muss:

- **Wirklichkeit:** Was passiert tatsächlich in deutschen Banken?
- **Probleme:** Alte Systeme, nicht genug Mitarbeiter, zu viele Regeln, zu wenig Geld, schlechte Datenqualität, Silostrukturen (jeder Bereich arbeitet für sich), langsame Entscheidungen.
- **Erwartung vs. Wirklichkeit:** So sieht es aus: Die Welt erwartet X, aber deutsche Banken kümmern sich immer noch um Y.
- **Die Lücke:** Wo genau ist der Unterschied zwischen Ziel (Seite 2) und Wirklichkeit (Seite 3) in Deutschland? Mit konkreter Beratungsleistung:
  - Ziel: Zahlungsverkehr in Echtzeit (1 Sekunde)
  - Wirklichkeit: deutsche Banken brauchen noch 3–5 Tage
  - Lücke: 4–5 Tage Verzögerung
  - **Beratungsdienstleistung:** Zahlungs-Modernisierung mit RPA-Tools + Cloud-Banking
  - **Way Forward:** Erstgespräch mit Operations-Leiter über Automatisierungs-Roadmap

Pflichtelement: eine **Gap-Tabelle** mit den Spalten:
`Themenfeld | Ziel | Wirklichkeit | Größe der Lücke | Was der Berater damit tun kann`

Die Tabelle braucht mindestens 5 Zeilen. Die Themenfelder dürfen sich nicht überschneiden — jedes Thema steht in genau einer Zeile.

🔴 **Quellenpflicht linke Spalte:** Jeder News-Block der linken Spalte endet mit einer kurzen Quellenangabe in Klammern. Kein Block ohne Quelle.

---

### Seite 4 — Zahlen und Geld im Markt

**Die Frage:** Wo verdienen Banken gerade Geld? Welche Bereiche wachsen?

Diese Seite ist für **Zahlen**. Sie zeigt, wo Geld ist.

Was auf dieser Seite stehen muss:

- **Schnell wachsende Industrien:** Welche Branchen wachsen? Warum?
- **Schnell wachsende Beratungs-Felder:** Z. B. KI, Regeln für Banken, Modernisierung von Systemen, Zahlungen, Sicherheit, Kostenreduktion, Firmen-Übernahmen.
- **Wachstumszahlen und Marktgrößen:** Mit Zahl, Einheit, Jahr und Zeitraum. Z. B. „Wachstum von 14 % pro Jahr bis 2030" oder „Markt: 8,2 Milliarden Euro 2025".
- **Was schrumpft:** Welche Bereiche werden kleiner? Mit Zahlen.
- **Die besten Verdiener:** Welche Geschäftsbereiche verdienen am meisten? Warum sind sie lukrativ?

Regel für diese Seite: **Jede Aussage braucht eine Zahl.** Jede Zahl braucht eine **konkrete, spezifische Begründung** in maximal zwei Sätzen. Nicht "Gewinnmargen sind hoch", sondern: "Gewinn bei Zahlungsverkehr für Firmenkunden: 55%, bei klassischen Kundenkrediten: 32%. Grund: Zahlungsverkehr ist automatisiert, Kredite brauchen Beratung". Keine Zahl ohne Jahresangabe.

Pflichtelemente: eine **Rangliste** der Top-Wachstums-Felder und eine **Negativliste** (was schrumpft). Diese zwei Listen stehen nebeneinander und sind klar voneinander getrennt.

🔴 **Quellenpflicht linke Spalte:** Jeder Zahlen-Block der linken Spalte endet mit einer kurzen Quellenangabe in Klammern. Gerade hier ist das wichtig, weil jede Aussage auf dieser Seite eine Zahl trägt — der Leser muss sehen, woher sie stammt. Kein Block ohne Quelle.

---

### 4.6 PFLICHT-MINDESTMENGEN — JEDE SEITE MUSS VOLL SEIN

⚠️ **KRITISCH — HALBLEERE SEITEN SIND DER HÄUFIGSTE FEHLER. DIESE MENGEN SIND PFLICHT.**

Die Vorlage `Main Example_Financial Services Consulting Newsletter.pdf` füllt die Seiten 1 bis 4 bis auf **3 bis 7 pt Restraum** über der Fußzeile. Das ist der Maßstab.

**Verbindliche Obergrenzen für den Leerraum** (so prüft auch das Skript aus Schritt 13b):

| Seite | Höchstens erlaubter Leerraum über der Fußzeile |
| --- | --- |
| Seiten 1 bis 4 | **40 pt** |
| Seite 5 (Quellen) | **80 pt** — die letzte Spalte der Quellenliste geht selten exakt auf |

Alles darüber gilt als halbleere Seite und wird **nicht gespeichert**.

| Seite | Pflicht-Inhalt (Mindestmenge) |
| --- | --- |
| **Seite 1** | Genau **6 News-Boxen** im 3×2-Raster. Jede Box: Kategorie + Headline + Kontext (200–320 Zeichen) + 3 Punkte (je 60–110 Zeichen) + Quelle. **Alle 6 Boxen gleich hoch gefüllt** — keine Box merklich leerer als die anderen. |
| **Seite 2** | Kernaussage-Box mit **3 Punkten**. Links **mindestens 8 News-Blöcke** (je Kategorie + Headline + 3–5 Sätze). Rechts **mindestens 7 Beratungsblöcke** (je Balken-Überschrift + Problem + Beratungsdienstleistung). Am Ende rechts die Box `FRONTRUNNER-MESSLATTE: WO EINE BANK HEUTE STEHEN MÜSSTE` mit **mindestens 6 Punkten**. |
| **Seite 3** | Kernaussage-Box mit **3 Punkten**. Links **mindestens 8 News-Blöcke**. Rechts **mindestens 7 Beratungsblöcke**. Zusätzlich die **Gap-Tabelle mit mindestens 6 Zeilen**. |
| **Seite 4** | Kernaussage-Box mit **3 Punkten**. Links **mindestens 8 Zahlen-Blöcke** (jeder mit Zahl, Einheit, Jahr, Begründung). Rechts **mindestens 7 Beratungsblöcke**. Zusätzlich **Rangliste** (mind. 5 Zeilen) und **Negativliste** (mind. 4 Zeilen). |
| **Seite 5** | **MINDESTENS 45 QUELLENEINTRÄGE** im APA-7-Format, zweispaltig, alphabetisch. Harte Untergrenze, nach oben offen. |

**Der Füll-Test vor dem Speichern (Pflicht):**

1. Öffne die fertige PDF und sieh dir **jede der 5 Seiten** an.
2. Frage bei jeder Seite: **Ist unten am Rand ein sichtbarer leerer Block?**
3. Wenn ja → **die Seite ist NICHT fertig.** Ergänze weitere News-Blöcke, Beratungsblöcke, Tabellenzeilen oder Quellen, bis die Seite voll ist.
4. Erst wenn **alle 5 Seiten randvoll** sind, wird gespeichert.

❌ **Niemals eine Seite mit sichtbarem Leerraum unten abspeichern.** Lieber einen Block mehr recherchieren als eine halbleere Seite abliefern.

⚠️ **Wenn der Stoff nicht reicht:** Das ist ein Recherche-Problem, kein Layout-Problem. Zurück zu Abschnitt 6 und weitere Quellen auswerten — **nicht** die Schrift größer machen, **nicht** die Abstände aufblähen, **nicht** das Raster ändern.

---

### Seite 5 — Alle Quellen

Seite 5 ist nur für Quellen. Nichts anderes steht dort.

- Alle Quellen sind im **APA-7-Format** geschrieben.
- Sie sind alphabetisch sortiert (nach Autor oder Organisation).
- Jede Quelle, die auf Seite 1–4 verwendet wurde, steht hier — und nur diese.
- Format: `Autor/Organisation. (Jahr, Monat Tag). Titel. Publikation. URL`

---

## 5. Äußerer Aufbau und Layout-Regeln

1. **Jede Seite wird komplett gefüllt** — Seiten 1 bis 4 bis höchstens **40 pt** Restraum über der Fußzeile, Seite 5 bis höchstens **80 pt**. Keine halb leeren Seiten. Die Pflicht-Mindestmengen stehen in **Abschnitt 4.6** und sind verbindlich: mindestens **8 News-Blöcke links** und **7 Beratungs-Blöcke rechts** pro Seite (Seiten 2–4), mindestens **45 Quellen** auf Seite 5. Weißraum ist nur erlaubt, wo er die Lesbarkeit stützt — nie als Platzfüller. **Reicht der Stoff nicht, wird weiter recherchiert — nicht das Layout gestreckt.**

2. **Linke Spalte = blanke News mit „So What?" Erklärung** (Seiten 2–4). Die linke Spalte zeigt reine Fakten aus den Nachrichten mit klarer Erklärung, was das bedeutet. Wichtig: Das „So What?" ist ZENTRAL — jede Zahl, jedes Zitat muss erklärt werden, warum es wichtig ist. Die Spaltenbreite ist ungefähr 40–45 %.

   **Die „So What?"-Regel für die linke Spalte (NEWS):**
   - Fakt/Zahl nennen
   - **Erklären, was das konkret bedeutet** (für Grundschüler verständlich!)
   - **Warum ist das wichtig/relevant?** (Kontext setzen)
   - **Kein reines Fakten-Dumping** — jede Information muss einen Sinn haben, den der Leser sofort versteht

   **Beispiele (FALSCH vs. RICHTIG):**

   - ❌ Falsch: "Gewinn 55%, Ertrag 47%"
   - ✅ Richtig: "Banken verdienen 55% ihrer Gewinne im Zahlungsverkehr, machen dort aber nur 47% ihres Umsatzes. Der Zahlungsverkehr ist für Banken also billig, weil Maschinen die Arbeit erledigen. Damit ist er das lukrativste Geschäft."

   - ❌ Falsch: "KI-Agenten-Adoption bei 11%"
   - ✅ Richtig: "Nur 11% der Banken nutzen KI-Agenten wirklich produktiv, obwohl 70% das planen. Zwischen Planung und Umsetzung liegt also eine riesige Lücke. Viele Häuser kommen nicht voran."

   - ❌ Falsch: "Core Banking Modernisierung wächst 16,9% pro Jahr"
   - ✅ Richtig: "Der Markt für neue Bankensysteme wächst 16,9% pro Jahr. Er wächst damit schneller als der gesamte Technik-Markt. Der Grund dafür sind die alten Systeme, die Banken dringend loswerden müssen. Für Berater ist das eine große Geschäftschance."

   - ❌ Falsch: "Wero: 43,5 Millionen Nutzer"
   - ✅ Richtig: "Die europäische Zahlungs-App Wero hat jetzt 43,5 Millionen Nutzer. Viele Hausbanken haben sie trotzdem nicht angebunden. Die Kunden wünschen sich also digitale Zahlungen, während die Banken hinterherhinken."

3. **Rechte Spalte = Beratungshebel — NUR Problem + Beratungsdienstleistung, KEINE Tools!** (Seiten 2–4). Die rechte Spalte zeigt **konkrete, praktische Beratungsansätze für Beratungshäuser**. **DIGITALE TOOLS SIND HIER NICHT RELEVANT.** Die Spaltenbreite ist ungefähr 55–60 %.

   **Struktur pro Rubrik (Seiten 2–4) — NUR 2 Elemente:**
   
   1. **Problem präzise erklären** (leicht verständlich, Grundschüler-Level + für Berater sinnvoll)
      - Was ist das konkrete Problem bei Banken oder im Markt?
      - Wer hat das Problem?
      - Was kostet das Problem dem Geschäft?
      - Warum können Berater hier helfen?
      - Beispiel GUT: "Alte Bankensysteme binden 40% des IT-Budgets für Wartung. Das Geld fehlt für Innovation. Das ist ein Wettbewerbsnachteil."
      - Beispiel FALSCH: "KI-Modelle müssen evaluiert werden" (unpräzise, nicht konkret)

   2. **Beratungsdienstleistung konkret — sehr klare Action Points**
      - Welche spezifischen Tätigkeiten führt der Berater durch?
      - Nicht abstrakt „Lösung", sondern: „Compliance-Audit durchführen", „Sidecar-Roadmap schreiben", „Schulungsprogramm entwickeln", „Governance-Modelle aufbauen", „Datenmigrationsprozess planen"
      - Beispiel GUT: "Beratungshäuser können einen Sidecar-Plan schreiben, um alte Systeme parallel zu neuen zu betreiben. Oder eine Stilllegungsstrategie für veraltete Module."
      - Beispiel FALSCH: "Modernisierung bieten" (zu vage, schammig)

   **⚠️ WICHTIG: Keine digitalen Tools auf der rechten Seite!**
   - Tools gehören NICHT hier hin — sie bringen nichts für die Beratungsleistung
   - Der Platz ist KOMPLETT für Problembeschreibung + Beratungsdienstleistung reserviert
   - Nur klare, verständliche Action Points. Keine Marketing-Sprache oder Rollen-Spiele.

   **Fachbegriffe gehören hin und werden konkretisiert:**
   - ❌ Falsch: "Transaction Banking optimieren"
   - ✅ Richtig: "Zahlungsverkehr, also der Geldtransfer zwischen Firmen. Eine Überweisung dauert heute drei bis fünf Tage statt einem Tag. Deshalb wandern Kunden zu schnelleren Anbietern ab. Berater können den Ablauf automatisieren und die Kundenkommunikation neu aufsetzen."

4. **Jede Nachricht bekommt eine Überschrift** (Seiten 2–4). Die Überschrift zeigt sofort, worum es geht. Beispiele: `Regulatorik`, `KI und Automatisierung`, `Zahlungsverkehr`, `Bankensysteme`, `Cybersicherheit`, `Nachhaltigkeit`, `Firmenkredite`, `Vermögensmanagement`, `Marktstruktur`.
   Das Gleiche gilt für die rechte Spalte: Auch jeder Beratungs-Block hat die gleiche Überschrift wie der News-Block links. So sieht man sofort, welche News zu welcher Beratung gehört — ohne Nummern oder Pfeile.

5. **Sprache muss super leicht verständlich, konkret und hilfreich sein — als würde man einem Kind erklären, was passiert.**

   ⚠️ **KRITISCH — SUPER LEICHT VERSTÄNDLICH!**
   
   - **Grundregel:** Schreibe **vollständige, sinnvolle Sätze**, die man sofort versteht. Keine Insider-Jargon, keine komplizierten Begriffe. Jedes Wort muss verständlich sein.
   - **❌ FALSCH:** "Die Wirkung des digitalen Euro auf die eigenen Einlagen ist gerechnet." (Niemand versteht das!)
   - **✅ RICHTIG:** "Die europäische Zentralbank plant einen digitalen Euro. Das ist wie elektronisches Bargeld. Man hat das Geld digital auf dem Handy statt als Scheine im Portemonnaie. Banken müssen dafür neue Systeme bauen, damit ihre Kunden dieses digitale Geld nutzen können."
   - **🔴 SATZZEICHEN-REGEL — MENSCHLICH GESCHRIEBEN, GENAU DIESE DREI PUNKTE:**

     **a) Bindestriche in zusammengesetzten Wörtern sind ERLAUBT**, wenn die Rechtschreibung sie verlangt oder sie das Lesen erleichtern. Das ist normales Deutsch und soll nicht künstlich vermieden werden.
     - ✅ Erlaubt: `EU-KI-Gesetz`, `KI-Agenten`, `Core-Banking-System`, `Vor-Ort-Prüfung`
     - Diese Schreibweise ist **kein Fehler** und wird **nicht** in Leerzeichen aufgelöst.

     **b) Gedankenstriche im Fließtext sind VERBOTEN.** Ein Gedankenstrich (`—` oder freistehendes `-`) zerhackt den Satz und liest sich maschinell. Schreibe stattdessen zwei ganze Sätze.
     - ❌ Falsch: `Die Bank hat ein Problem — sie ist zu langsam.`
     - ✅ Richtig: `Die Bank hat ein Problem. Sie arbeitet zu langsam.`
     - ❌ Falsch: `Wero wächst schnell - über 43 Millionen Menschen nutzen es.`
     - ✅ Richtig: `Wero wächst schnell. Über 43 Millionen Menschen nutzen es.`

     **c) Doppelpunkte im Fließtext sind VERBOTEN.** Ein Doppelpunkt mitten im Satz wirkt wie eine Stichwortliste, nicht wie ein geschriebener Text.
     - ❌ Falsch: `Das Problem: alte Systeme kosten zu viel.`
     - ✅ Richtig: `Das Problem sind die alten Systeme. Sie kosten zu viel Geld.`
     - ❌ Falsch: `Der Grund: Maschinen erledigen die Arbeit.`
     - ✅ Richtig: `Der Grund dafür ist, dass Maschinen die Arbeit erledigen.`

     **AUSNAHME für Doppelpunkte:** Als Abschluss einer **Beschriftung** sind sie erlaubt und sogar vorgeschrieben, weil sie Struktur zeigen und nicht Teil eines Satzes sind:
     - ✅ `BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:` (Seite 1)
     - ✅ `Problem:` und `Beratungsdienstleistung:` (Seiten 2 bis 4, rechte Spalte)
     - Diese Beschriftungen bleiben **unverändert**. Die Regel betrifft **nur den Fließtext dahinter**.

     **Selbstprüfung:** Lies jeden Absatz laut. Klingt er wie ein Mensch, der etwas erklärt? Oder wie eine Aufzählung mit Satzzeichen dazwischen? Nur das Erste ist richtig.
   - **Fachbegriffe — IMMER erklären:** 
     - ❌ "APIs ermöglichen Integration" (Niemand versteht das!)
     - ✅ "APIs sind technische Brücken, die verschiedene Computerprogramme verbinden. Sie funktionieren wie Leitungen, die Daten hin und her leiten"
     - ❌ "Core Banking Modernisierung"
     - ✅ "Die zentrale Bankensoftware modernisieren, die alle Konten und Geldtransfers verwaltet"
   - **Banking-Anfänger als Zielgruppe:** Schreib so, als würde jemand ohne jede Bank-Erfahrung den Text lesen. Jeder Fachbegriff muss erklärt sein. Keine Abkürzungen ohne Erklärung.
   - **Informativer Inhalt:** Der Leser soll DANACH wissen, worum es geht — ohne woanders recherchieren zu müssen. Schreib konkrete Details, nicht vage Aussagen.
   - **Unternehmerische News — nur gewichtig:** Product Launches, Partnerschaften (z.B. "Goldman Sachs und BlackRock arbeiten zusammen mit einem KI-Unternehmen"). **Nur aufnehmen, wenn es echte Markt-Auswirkungen gibt.** **IMMER erklären, was das für Banken bedeutet.**
   - Kein Beratungs-Jargon. Jedes Wort muss konkret sein und einen Sinn haben.

6. **Quellenangaben auf Seiten 1–4 (neu — wichtig für Nachvollziehbarkeit):**
   - **Neue Regel:** Jede News, jedes Zitat, jede Zahl auf Seiten 1–4 bekommt eine **kurze Quellenangabe am Ende des Abschnitts**.
   - **Format (kurz halten, nur 1–2 Zeilen):**
     - `(McKinsey, 2026)`
     - `(Financial Times, August 2026)`
     - `(EZB Pressemitteilung, 2026)`
     - `(Handelsblatt, 11.08.2026)`
     - `(Deloitte Whitepaper, 2026)`
   - **Zweck:** Leser kann sofort sehen, woher die Information kommt. Vollständige Referenz findet sich auf Seite 5 im APA-7-Format.
   - **Positionierung:** Am Ende des News-Blockes, vor dem Zeilenumbruch zur nächsten News.
   - **Platzverbrauch:** Minimal — nur eine kurze Zeile, keine großen Textboxen.
   - **Alle Seiten (1–4):** Cover, Seite 2, Seite 3, Seite 4 — überall Quellenangaben.

7. **Struktur muss sehr klar sein.** Nichts überlappt sich. Alles ist leicht zu lesen. Feste Reihenfolge. Feste Blockgrößen. Klare Abstände. Saubere Linien zwischen den Blöcken.

7b. **🔴 KEINERLEI WIEDERHOLUNGEN — JEDE INFORMATION STEHT GENAU EINMAL.**

   Wiederholungen sind der häufigste Qualitätsmangel und **niemals erlaubt**. Eine Zahl, eine Aussage, ein Sachverhalt erscheint im gesamten Newsletter **exakt einmal** — an der Stelle, wo sie am meisten Sinn ergibt.

   **🔴 MECE über den GESAMTEN Newsletter — nicht nur je Seite.** Der Newsletter ist **ein** Dokument. Ein Thema, das auf Seite 1 steht, ist damit **verbraucht** und darf auf den Seiten 2, 3 und 4 nicht erneut als eigener Block auftauchen. Geprüft wird über alle 5 Seiten hinweg, nicht seitenweise.

   **Was als Wiederholung gilt (alles davon ist verboten):**
   - **🔴 Dasselbe Thema zweimal im Newsletter.** Steht `EU-KI-Gesetz` als Cover-Box 01, darf es auf Seite 2 keinen weiteren Block über das EU-KI-Gesetz geben. Auch nicht unter anderer Überschrift, auch nicht mit anderem Zahlenmaterial. **Ein Thema, ein Platz.**
   - **Dieselbe Zahl zweimal.** Steht `43,5 Millionen Wero-Nutzer` auf Seite 1, darf sie auf Seite 2 nicht erneut auftauchen.
   - **Dieselbe Aussage anders formuliert.** `Banken hinken bei der Technik hinterher` und `Deutsche Institute sind technisch nicht auf Höhe` sind **dieselbe** Aussage. Nur eine davon bleibt.
   - **Dieselbe Beratungsdienstleistung mehrfach.** Steht `Einen Plan für die Datenübertragung schreiben` schon bei einem Thema, gehört sie nicht noch einmal zu einem anderen.
   - **Dasselbe Thema in zwei Blöcken derselben Seite.** Zwei Blöcke über KI-Regulierung werden zu **einem** Block zusammengezogen.
   - **Wiederholung zwischen den Spalten.** Was links als Nachricht steht, wird rechts **nicht** noch einmal erzählt. Rechts steht ausschließlich, was ein Berater daraus macht.

   **Die Themenliste als Werkzeug:** Führe beim Schreiben eine laufende Liste der bereits vergebenen Themen. Jedes neue Thema wird gegen diese Liste geprüft, **bevor** es geschrieben wird. Bei rund 30 Blöcken über fünf Seiten sind das 30 verschiedene Themen — aus 62 verfügbaren Quellen ist das problemlos zu erreichen.

   **Die Prüfmethode vor dem Speichern (Pflicht):**
   1. Schreibe **Thema und Kernaussage jedes Blocks** in je einem Satz auf — über **alle 5 Seiten** hinweg. Bei 6 Cover-Boxen und 3 mal 8 News-Blöcken sind das rund 30 Einträge.
   2. Lege sie nebeneinander. **Kommt ein Thema zweimal vor?** Dann fliegt das schwächere raus und wird durch ein neues aus der Tagesliste ersetzt.
   3. **Sagen zwei Kernaussagen dasselbe?** Dann bleibt nur eine.
   4. Sammle alle genannten **Zahlen** in einer Liste. **Kommt eine Zahl zweimal vor?** Dann steht sie an der schwächeren Stelle zu viel und wird dort gestrichen.
   5. **🔴 NACHZÄHLEN NACH JEDEM STREICHEN:** Sind es immer noch **mindestens 45 Quellen**? Sind alle Seiten **noch voll**? Stehen links noch **8 Blöcke** und rechts **7**? Wenn nein → die Lücke mit einem **neuen Thema** füllen, nicht offen lassen.
   6. Erst wenn jedes Thema, jede Kernaussage und jede Zahl **einmalig** ist **und** die Mengenvorgaben weiterhin erfüllt sind, wird gespeichert.

   ---

   #### 🔴 KOPPLUNG: MECE UND VOLLSTÄNDIGKEIT GELTEN GLEICHZEITIG

   ⚠️ **Wiederholungsfreiheit ist ein Grund zum ERSETZEN, niemals ein Grund zum WEGLASSEN.**

   Die MECE-Regel darf **unter keinen Umständen** dazu führen, dass am Ende weniger Inhalt dasteht. Beide Anforderungen gelten **zusammen und ungeschmälert**:

   | Anforderung | Wert | Gilt auch dann, wenn … |
   | --- | --- | --- |
   | **Quellen auf Seite 5** | **mindestens 45**, nach oben offen | … Dubletten entfernt wurden |
   | **Seiten 1 bis 4 gefüllt** | höchstens **40 pt** Leerraum | … Blöcke gestrichen wurden |
   | **Seite 5 gefüllt** | höchstens **80 pt** Leerraum | … Quellen zusammengelegt wurden |
   | **Blöcke je Seite** | mind. **8 links**, **7 rechts** | … Themen doppelt waren |
   | **Themen, Zahlen, Aussagen** | jedes **genau einmal** | … dafür nachrecherchiert werden muss |

   **Das Verfahren beim Streichen — Pflicht in dieser Reihenfolge:**

   1. **Dublette erkennen** (Thema, Zahl oder Aussage kommt zweimal vor).
   2. **Die schwächere Stelle streichen.**
   3. **🔴 SOFORT ERSETZEN.** An dieselbe Stelle kommt ein **neues, bisher unbenutztes Thema** aus der Tagesliste oder den Kernquellen — mit **eigener, neuer Quelle**.
   4. **Zählen.** Sind es immer noch mindestens 45 Quellen? Ist die Seite immer noch voll? Wenn nein → weiter ersetzen.

   ❌ **Verboten:** Eine Dublette streichen und die Lücke stehen lassen. Das erzeugt genau die halbleeren Seiten und die 27-Quellen-Ausgaben, die nicht mehr vorkommen dürfen.
   ❌ **Verboten:** Die Lücke mit einer Umformulierung des Gestrichenen füllen. Das ist wieder eine Wiederholung.
   ❌ **Verboten:** Zwei Themen zusammenlegen, um Platz zu sparen, und dadurch unter 45 Quellen zu fallen.

   **Warum das ohne Konflikt aufgeht:** Pro Tag stehen **62 Quellen** zur Verfügung (20 Kernquellen + 42 der Tagesliste). Der Newsletter braucht rund 30 Themen und mindestens 45 Quellen. Der Vorrat ist also deutlich größer als der Bedarf. **Jede gestrichene Dublette lässt sich ersetzen** — es gibt keinen Fall, in dem MECE und Vollständigkeit sich wirklich widersprechen. Entsteht der Eindruck eines Widerspruchs, wurde zu flach recherchiert. Dann gilt Abschnitt 6, Punkt 2: zurück in die Recherche.

8. **Standards einer Beratungsagentur:** Gestalte wie bei McKinsey, BCG oder Bain.
   - **MECE ist Pflicht:** Die Themenfelder überschneiden sich nicht, und es fehlt nichts Wichtiges. Jedes Thema steht genau einmal (siehe Punkt 7b).
   - **Top-down:** Erst die Kernaussage, dann die Begründung, dann das Detail.
   - **Highlights verwenden:** Fettung, Boxen mit Nummern, Zeilen wie „Das bedeutet für den Berater:".
   - **Klare Abgrenzung:** Soll vs. Ist, Wachstum vs. Schrumpfung, Deutschland vs. Ausland — das muss klar unterschiedlich aussehen.
   - **Jede Überschrift ist eine Aussage** — nicht nur ein Etikett.

9. **Keine Fußnoten.** Keine hochgestellten Zahlen. Keine Endnoten. Die einzige Fußzeile ist das Datum des Tages.

10. **Datum auf Seite 1 (Cover Page):** Das Datum der heutigen Ausgabe steht groß und auffällig auf Seite 1: `Ausgabe des DD.MM.YYYY`.

11. **Titel:** Der Titel lautet immer exakt: `Financial Services Consulting Newsletter`.

12. **Schriftart:** Überall die gleiche Schriftart: **Arial**. Auf allen fünf Seiten. In Überschriften, Fließtext, Tabellen, Zahlen, Quellen. Keine zweite Schriftart. Die Hierarchie entsteht nur durch Größe, Fettung und Farbe.

---

## 6. Recherche und Quellenangaben

1. **Intensive, täglich aktualisierte Recherche mit maximaler Quellenbreite — 45+ QUELLEN TÄGLICH!** Recherchiere täglich in **mindestens 45 verschiedenen Top-Quellen** (nicht nur 6–8), um den **allerneuesten Stand** abzubilden und ein **ganzheitliches, fundiertes Marktbild** zu erzeugen. 

   **Hochwertige Quellen nach Kategorie (täglich recherchieren):**
   - **Nachrichtenmedien (Financial Times, Bloomberg, Wirtschaftswoche, Handelsblatt, FAZ, Reuters, The Economist, TechCrunch):** Täglich aktuelle Meldungen, Breaking News
   - **Whitepaper & Research:** McKinsey, Boston Consulting Group (BCG), Bain, PwC, Deloitte, EY, KPMG, Strategy&, Roland Berger, Gartner, Forrester — aktuelle Studien und Marktanalysen
   - **Unternehmen & Verbände:** Pressemitteilungen, Geschäftsberichte, Produktankündigungen, Zentralbanken (EZB, Fed, BoE, SNB), Bankenverbände, regulatorische Körperschaften
   - **Hochwertige Blogs & Analysen:** Fach-Blogs von renommierten Analysten, Banking-Expert-Blogs, FinTech-Publikationen, Tech-Analyst-Seiten
   - **Websites von Unternehmen & Instituten:** Offizielle Ankündigungen, Produktseiten, Research-Seiten

2. **🔴 IMMER MINDESTENS 45 QUELLEN PRO NEWSLETTER — JEDEN TAG, OHNE AUSNAHME.**

   ⚠️ **DAS IST EINE HARTE UNTERGRENZE, KEIN RICHTWERT.** Eine Ausgabe mit 27, 35 oder 44 Quellen ist **nicht fertig** und wird **nicht gespeichert**. Die Zahl 45 gilt an jedem Wochentag gleichermaßen, unabhängig vom Themenfokus.

   **Die Zählregel:**
   - Am Ende der Recherche werden die Einträge auf Seite 5 **gezählt**.
   - Sind es **weniger als 45** → **zurück in die Recherche.** Weitere Quellen aus `Recherche-Gerüst/02_Quellen-Matrix` auswerten.
   - **45 ist der Boden, nicht das Ziel. Es gibt keine Obergrenze.** 50, 60 oder 70 geprüfte Quellen sind besser als 45. Höre nicht auf, sobald 45 erreicht sind, sondern wenn der Themenfokus des Tages wirklich ausgeschöpft ist.

   **Gleichbleibend hohe Qualität an jedem Wochentag:**
   - Zusätzlich zur Tagesliste gelten **20 Kernquellen, die an jedem Tag geprüft werden** — unabhängig vom Themenfokus. Dazu zählen McKinsey, BCG, Bain, PwC, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB, BaFin, EBA und Deutsche Bundesbank.
   - Sie stehen in `Recherche-Gerüst/02_Quellen-Matrix` im Abschnitt „TÄGLICHE KERNQUELLEN" und **kommen zur Tagesliste hinzu**, sie ersetzen sie nicht.
   - **Rechnung: 20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen pro Tag.**
   - Dadurch ist die Datenlage an einem Mittwoch genauso gut wie an einem Montag. Der **Fokus** wechselt täglich, die **Qualitätsbasis** nicht.

   **Qualitätsanforderungen an jede Quelle:**
   - Autor oder Organisation ist eindeutig benannt
   - Veröffentlichungsdatum ist gesetzt
   - Zahlen sind überprüfbar
   - **Mindestens 10–12 Quellen** stammen aus anderen Ländern oder internationalen Publikationen
   - **Aktualität hat Vorrang:** Quellen der letzten 24–72 Stunden werden bevorzugt

   **So kommt man verlässlich auf 45+:**
   - `Recherche-Gerüst/02_Quellen-Matrix` listet je Wochentag **42 Quellen** (Abschnitt „NUTZUNGSLOGIK NACH WOCHENTAG"). Diese Liste wird **vollständig abgearbeitet**, nicht nur die ersten sechs bis acht.
   - `Recherche-Gerüst/03_Master_Recherche_Prompt_Template` enthält je Wochentag den passenden Prompt. Jeder dieser sieben Prompts trägt die Überschrift **„RECHERCHIERE IN 45+ QUELLEN TÄGLICH"** und listet unter **„Danach AUCH"** die Quellen bis Position 42.
   - ⚠️ **Prüfe beim Start: Trägt der Prompt des heutigen Wochentags die 45+-Überschrift und den Abschnitt „Danach AUCH"?** Wenn dort nur eine kurze Liste mit sechs bis acht Quellen steht, ist der Prompt defekt — dann die vollständige Tagesliste aus Datei 02 verwenden. Genau dieser Defekt führte am Mittwoch, 12.08.2026 zu nur 27 Quellen.
   - Jede der vier Inhaltsseiten (1–4) zieht aus diesem Pool. Bei 6 News + 3×8 Blöcken links + 3×7 Blöcken rechts entstehen dabei zwangsläufig mehr als 40 Belege.
   - **Wenn am Ende weniger als 45 Quellen dastehen, wurde zu flach recherchiert** — nicht die Zahl schönen, sondern nacharbeiten.

3. **Täglich Neues bringen, nie wiederholen.** 
   - Vor dem Schreiben: Schau die Ausgaben der **letzten 5 Tage** an (Ordner `Output`). Welche Themen sind schon behandelt worden? Führe eine Liste dieser Themen.
   - **🔴 Regel: Mindestens 80 % der Themen müssen neu sein gegenüber den letzten 5 Tagen.** Bei rund 30 Blöcken heißt das: **höchstens 6 Themen** dürfen fortgeführt werden, mindestens 24 sind neu.
   - Ein Thema darf **nur dann** wiederkommen, wenn es eine **echte neue Entwicklung** gibt (neuer Beschluss, neue Zahl, neue Wendung). Dann wird **ausschließlich das Neue** berichtet, nicht der bereits bekannte Sachverhalt wiederholt.
   - **Der Bezugszeitraum sind immer die letzten 5 Tage**, nicht nur der Vortag. Ein Thema von vorgestern zählt genauso als bekannt wie eines von gestern.
   - Wenn zwei News dem gleichen Trend folgen (z.B. beide über KI-Regulatorik), kombiniere sie zu einer Aussage, statt beide einzeln zu schreiben.

4. **Wenn Quellen widersprechen:** Schreibe auf, was die meisten Quellen sagen. Schreibe auch auf, was die Minderheit sagt, in einem Satz. Erfinde **niemals** eine Zahl. Wenn eine Zahl unsicher ist, schreibe „geschätzt" dazu.

4b. **🔴 QUELLENPRÜFUNG — KEINE FALSCHAUSSAGEN, KEINE ERFUNDENEN BELEGE.**

   Jede Quelle und jede Zahl wird vor der Aufnahme geprüft. Ein Newsletter mit einer falschen Zahl oder einer erfundenen Quelle ist **wertlos** und beschädigt das Vertrauen dauerhaft.

   **Vier Prüfungen für jede einzelne Quelle:**

   | # | Prüfung | Was konkret geprüft wird |
   | --- | --- | --- |
   | 1 | **Existiert die Quelle wirklich?** | Der Bericht, die Pressemitteilung oder der Artikel muss tatsächlich aufrufbar sein. **Niemals** eine plausibel klingende Quelle aus dem Gedächtnis konstruieren. |
   | 2 | **Steht die Zahl wirklich dort?** | Die genannte Zahl muss in der Quelle stehen, nicht daraus abgeleitet oder gerundet sein. Wenn dort `47,3%` steht, schreibe nicht `fast die Hälfte`. |
   | 3 | **Stimmt die Zuordnung?** | Die Zahl gehört zu genau dieser Organisation, diesem Zeitraum und diesem Bezugsrahmen. Eine Zahl über **europäische** Banken darf nicht als Aussage über **deutsche** Banken erscheinen. |
   | 4 | **Stimmt das Datum?** | Jahr und Monat müssen mit der Quelle übereinstimmen. Eine Studie aus 2025 wird nicht als `2026` ausgewiesen. |

   **Verboten (jede dieser Handlungen macht die Ausgabe unbrauchbar):**
   - Eine Quelle nennen, die nicht geprüft wurde
   - Eine URL angeben, die nicht aufgerufen wurde
   - Zwei Quellen zu einer Aussage verschmelzen, die keine davon so trifft
   - Eine Zahl aus dem Zusammenhang reißen, sodass sie etwas anderes aussagt
   - Eine ältere Zahl als aktuell darstellen

   **Bei Unsicherheit gilt immer:** Lieber die Meldung **weglassen** und ein anderes Thema aus der 42er-Tagesliste nehmen, als eine ungeprüfte Aussage aufnehmen. Es gibt genug Quellen, um jede Lücke sauber zu füllen.

   **Widersprechen sich zwei geprüfte Quellen bei derselben Zahl?** Dann nenne beide Werte mit ihrer jeweiligen Quelle, statt dich stillschweigend für eine zu entscheiden.

5. **Aktualität ist Pflicht:** Der Newsletter soll den allerneuesten Stand zeigen. **Priorität:** Nachrichten der letzten 24 Stunden. Fallback: der letzten 48–72 Stunden. Ältere Studien und Markt-Zahlen sind ok, wenn sie erklären, worum es geht — aber dann immer mit Jahresangabe und dem Hinweis „Stand 202X".

6. **Auf Seiten 1–4 steht eine KURZE Quellenangabe, auf Seite 5 die vollständige Referenz.**
   - **Seiten 1–4:** Am Ende jedes News-Blocks eine knappe Angabe in Klammern, kursiv, klein: `(McKinsey, 2026)` oder `(Handelsblatt, August 2026)`. Eine Zeile, mehr nicht.
   - **Verboten bleiben:** Fußnoten, Endnoten, hochgestellte Verweiszeichen, ausgeschriebene URLs, nummerierte Verweise.
   - **Seite 5:** Die **vollständige** Referenz im APA-7-Format inklusive URL. Der Leser findet dort jede Kurzangabe von Seite 1–4 wieder.

7. **Seite 5 ist die vollständige Quellen-Seite.** Alle Quellen werden dort im **APA-7-Format** als alphabetische Referenzliste gesammelt — **mindestens 45 Einträge** (siehe Punkt 2).

---

## 7. Tägliche Wiederholung und Mehrwert

Der Newsletter wird **jeden Tag** erneut erstellt, ausgelöst über **Claude Routines**. Diese Regel gilt dabei:

- **Jede Ausgabe bringt Neues:** Mindestens **80 % der Themen sind neu** im Vergleich zu den **letzten 5 Ausgaben** (nicht nur zur gestrigen).
- **Kein Wiederkäuen:** Ein Thema darf nur wiederkommen, wenn es eine **neue Entwicklung** gibt. Dann wird nur das Neue berichtet — mit einem Halbsatz zur Einordnung.
- **Struktur bleibt gleich:** Über alle Tage hinweg dürfen sich die Zwecke der Seiten nicht vermischen.
- **Abgleich mit alten Ausgaben:** Vor dem Schreiben werden die Ausgaben der letzten 5 Tage aus dem Ordner `Output` angeschaut, um Wiederholungen zu vermeiden und Entwicklungen weiterzuführen.

---

## 8. Schritt-für-Schritt-Arbeitsablauf

0. **🔴 ARBEITSGRUNDLAGE SICHTEN UND IM REPOSITORY WIEDERHERSTELLEN — VOR ALLEM ANDEREN.**

   Dieser Schritt läuft **vor der Recherche, vor dem Datum, vor allem anderen**. Er stellt sicher, dass die komplette Arbeitsgrundlage jeden Tag verfügbar ist — auch dann, wenn das Repository zwischenzeitlich gelöscht und neu angelegt wurde.

   **Schritt 0a — Repo-Adresse aus der Routine übernehmen**

   Die Adresse des öffentlichen Repositories wird **in der Claude Routine hinterlegt** und dort bei jedem Lauf mitgegeben. Sie steht bewusst **nicht** in dieser Datei, damit ein neu angelegtes Repository nur an einer Stelle eingetragen werden muss.
   - Nimm die Repo-Adresse aus der Routine des heutigen Laufs.
   - **Fehlt sie:** melden und **nicht** bauen. Ohne Zieladresse kann weder die Vorlage gesichert noch die fertige Ausgabe abgelegt werden.

   **Schritt 0b — Vorlage lokalisieren, in dieser Reihenfolge**
   1. **Zuerst lokal auf dem Desktop (Master):**
      `/Users/marchaak/Desktop/Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf`
   2. **Nur falls der Desktop nicht erreichbar ist**, die Spiegelkopie im Repository:
      `Example Design/Main Example_Financial Services Consulting Newsletter.pdf`

   **Schritt 0c — Vorlage sichten**

   Öffne die gefundene Datei und **sieh dir alle 5 Seiten an**. Die exakten Maße stehen in Abschnitt 12.2. Präge dir ein: **Cover = 3 Spalten × 2 Reihen in einer weißen Karte.** Seiten 2–4 = zweizeiliger Kopf, links weiß / rechts hellblau, **jeder linke Block endet mit einer Quellenangabe**. Seite 5 = zwei Spalten Quellen.

   **Schritt 0d — 🔴 REPOSITORY AUF VOLLSTÄNDIGKEIT PRÜFEN UND FEHLENDES HOCHLADEN**

   Das Repository heißt **immer gleich** (`Daily-Banking-Newsletter`), wird aber gelegentlich **gelöscht und neu angelegt**, wenn sich Regelwerke ändern. Nach einem solchen Neuaufbau ist es **leer**. Dieser Schritt stellt die Arbeitsgrundlage selbsttätig wieder her.

   **Die Pflichtliste — diese Dateien müssen im Repository liegen:**

   | # | Datei oder Ordner | Wofür sie gebraucht wird |
   | --- | --- | --- |
   | 1 | `Struktur/Struktur.md` | dieses Regelwerk |
   | 2 | `Struktur/qualitaetspruefung.py` | maschinelle Endprüfung (Schritt 13b) |
   | 3 | `Mail Design/Mail Design.md` | Aufbau der Versand-Mail |
   | 4 | `Recherche-Gerüst/01_Wochenstruktur_Fokus-Themenfelder.md` | Themenfeld je Wochentag |
   | 5 | `Recherche-Gerüst/02_Quellen-Matrix_Aktuell_und_Erweiterung.md` | Quellenlisten und Kernquellen |
   | 6 | `Recherche-Gerüst/03_Master_Recherche_Prompt_Template.md` | Recherche-Prompts je Tag |
   | 7 | `Recherche-Gerüst/04_Implementierungs-Leitfaden.md` | Tagesworkflow |
   | 8 | `Example Design/Main Example_Financial Services Consulting Newsletter.pdf` | **die Design-Vorlage** |
   | 9 | `Example Design/Newsletter_Wallpaper.jpeg` | Hero-Bild der Cover Page |
   | 10 | `Output/` | Ablage der Ausgaben und Grundlage der 5-Tage-Sperrliste |

   **Das Verfahren — bei JEDEM Lauf:**

   1. **Prüfen:** Welche Einträge der Pflichtliste fehlen im Repository?
   2. **Fehlendes hochladen:** Alles Fehlende vom Desktop (`/Users/marchaak/Desktop/Banking Newsletter/`) committen und **direkt auf `main`** pushen.
   3. **Abweichungen angleichen:** Liegt eine Datei im Repo, weicht aber vom Desktop ab, **gewinnt der Desktop** (Abschnitt 12.1). Die Repo-Fassung wird überschrieben.
   4. **Erst danach** mit Schritt 1 weiterarbeiten.

   **Entscheidungstabelle:**

   | Lage | Was zu tun ist |
   | --- | --- |
   | **Repository ist leer** (frisch neu angelegt) | **Die komplette Pflichtliste hochladen.** Das ist der Normalfall nach einem Neuaufbau und kein Fehler. Danach weiterarbeiten. |
   | **Einzelne Dateien fehlen** | Nur die fehlenden hochladen. |
   | **Datei vorhanden, weicht vom Desktop ab** | Desktop-Fassung hochladen und die Repo-Fassung überschreiben. |
   | **Alles vorhanden und identisch** | Nichts tun. Weiter mit Schritt 1. |
   | **Repository leer und Desktop nicht erreichbar** | ⚠️ **NICHT BAUEN.** Melden: *„Repository und Desktop sind beide leer. Die Arbeitsgrundlage fehlt vollständig."* |
   | **Datei nur im Repo, Desktop nicht erreichbar** | Repo-Fassung verwenden. Kein Upload nötig. |

   **Warum dieser Schritt Pflicht ist:** Wird das Repository gelöscht und neu angelegt, fehlen dort Regelwerke, Recherche-Gerüst und Design-Vorlage. Ein Cloud-Lauf ohne Desktop-Zugriff hätte dann **keine Arbeitsgrundlage** und würde nach Gedächtnis bauen — genau daraus entstand das fehlerhafte 2-Spalten-Cover am 12.08.2026. Schritt 0d macht den Neuaufbau **selbstheilend**: Der erste Lauf nach dem Löschen stellt alles wieder her, ohne dass etwas von Hand hochgeladen werden muss.

   ⚠️ **Die Repo-Adresse bleibt dabei immer dieselbe** und kommt aus der Routine (Schritt 0a). Ein Neuaufbau ändert den Namen nicht.

1. **Datum UND Wochentag notieren — TÄGLICH AKTUALISIEREN.**

   **1a — Datum:** Heute ist welcher Tag? Format: `DD.MM.YYYY` (z.B. `12.08.2026`). Dieses Datum wird in den Dateinamen übersetzt: YYYYMMDD (z.B. `20260812`). **Das Datum wechselt jeden Tag.** Der Dateiname muss das aktuelle Tages-Datum enthalten, sonst würde die alte Ausgabe überschrieben.

   **1b — 🔴 WOCHENTAG BESTIMMEN (steuert das Themenfeld des Tages):**

   Welcher Wochentag ist heute? Daraus ergibt sich der Fokus:

   | Wochentag | Themenfeld des Tages |
   | --- | --- |
   | Montag | Strategische Trends und Zukunftsperspektive |
   | Dienstag | Operative Realität und Projekt-Realität |
   | Mittwoch | Regulierung, Compliance und Governance |
   | Donnerstag | Märkte, Geschäftsmodelle und Finanzen |
   | Freitag | Innovation, Technologie und Zukunft |
   | Samstag | Kundenperspektive, Retail und Experience |
   | Sonntag | People, Organisation und Kultur |

   - Details zum Fokus stehen in `Recherche-Gerüst/01_Wochenstruktur_Fokus-Themenfelder.md`.
   - Die passende Quellenliste steht in `Recherche-Gerüst/02_Quellen-Matrix`, Abschnitt „NUTZUNGSLOGIK NACH WOCHENTAG".
   - Der passende Recherche-Prompt steht in `Recherche-Gerüst/03_Master_Recherche_Prompt_Template`.

   **1c — 🔴 SPERRE: OHNE DATUM UND WOCHENTAG KEINE RECHERCHE.**

   Bevor mit Schritt 3 (Recherche) begonnen wird, müssen **alle drei** Angaben schriftlich festliegen:

   | Angabe | Beispiel | Wofür sie gebraucht wird |
   | --- | --- | --- |
   | **Datum** | `13.08.2026` | Dateiname, Kopfzeile, Mailbetreff, Fußzeile |
   | **Wochentag** | `Donnerstag` | steuert das Themenfeld des Tages |
   | **Themenfeld** | `Märkte, Geschäftsmodelle und Finanzen` | steuert Recherche, Quellenliste und Prompt |

   ⚠️ **Fehlt eine dieser drei Angaben, wird die Recherche NICHT begonnen.** Erst Schritt 1 vollständig abschließen, dann weiter.

   **Warum diese Sperre besteht:** Der Wochentag bestimmt das Themenfeld. Wird er nicht ermittelt, greift die Recherche auf ein beliebiges oder auf das gestrige Themenfeld zurück — der Newsletter gleicht dann dem von gestern. Das Themenfeld ist der einzige Grund, warum jeder Tag eine andere Ausgabe ergibt. **Es ist deshalb kein Nebenschritt, sondern die Voraussetzung für alles Folgende.**

2. **Alte Ausgaben prüfen — SPERRLISTE FÜR HEUTE ERSTELLEN.**

   Schau in den Ordner `Output` auf die **letzten 5 Tage** und notiere **jedes dort behandelte Thema**. Diese Liste ist die **Sperrliste** für den heutigen Lauf.

   - **🔴 Mindestens 80 % der heutigen Themen müssen neu sein.** Bei rund 30 Blöcken dürfen **höchstens 6** von der Sperrliste stammen.
   - Ein gesperrtes Thema darf nur zurückkommen, wenn es eine **echte neue Entwicklung** gibt. Dann wird **ausschließlich das Neue** berichtet.
   - Die Sperrliste wird während der Recherche (Schritte 3 bis 6) **laufend abgeglichen**, nicht erst am Ende.

   ⚠️ **Auch hier gilt die Kopplung aus Abschnitt 5, Punkt 7b:** Ein wegen der Sperrliste verworfenes Thema wird durch ein **neues ersetzt**, nicht ersatzlos gestrichen. Am Ende stehen weiterhin **45+ Quellen** und **volle Seiten**.

3. **Recherche für Seite 1 (Cover Page) — in 45+ Quellen.**

   ⚠️ **Voraussetzung:** Schritt 1c ist abgeschlossen. Datum, Wochentag und Themenfeld liegen fest. Sonst hier **nicht** beginnen.

   Nutze das in Schritt 1b bestimmte Themenfeld (Details in `Recherche-Gerüst/01_Wochenstruktur`) und recherchiere in 45+ Top-Quellen (Tagesliste in `Recherche-Gerüst/02_Quellen-Matrix`, Prompt in `Recherche-Gerüst/03_Master_Recherche_Prompt_Template`). Finde die 6 gewichtigsten News des Tages aus den 45+ Quellen. Diese müssen Executive-Level sein und klare Consulting-Implikationen haben.

4. **Recherche für Seite 2 — in 45+ Quellen.** Nutze die gleichen 45+ Quellen (priorisiert nach Wochentag-Fokus). Suche nach neuen Ideen, globalen Trends, Deutschlands Problemen, wem der Markt folgt.

5. **Recherche für Seite 3 — in 45+ Quellen.** Nutze die gleichen 45+ Quellen. Suche nach dem, was deutsche Banken wirklich tun, wo sie kämpfen, wo alte Programme laufen, wo Programme gescheitert sind.

6. **Recherche für Seite 4 — in 45+ Quellen.** Nutze die gleichen 45+ Quellen. Suche nach Wachstumsraten, Marktgrößen, Beratungs-Markt-Daten, Segment-Margen, was schrumpft.

7. **Quellen sammeln.** Wer hat das geschrieben? Wann? Wie gut ist die Quelle? Stimmt die Mehrheit der Quellen überein? Alle Quellen für Seite 5 notieren.

8. **Themen gliedern.** Welche Themenfelder gibt es? Überschneiden sie sich? Jedes Thema sollte genau einmal vorkommen (MECE).

9. **Seite 1 (Cover Page) — nur Inhalte, kein Design, flexible Struktur mit standardisierter Wording.** 
   - **NICHT neu designen.** Das Design ist 1:1 Standard nach `Main Example_Financial Services Consulting Newsletter.pdf`.
   - **NUR die Texte schreiben:** Die 6 gewichtigsten News mit:
     - Kontext erklären (leicht verständlich, Grundschüler-Level)
     - **"Bedeutung für Beratungsdienstleistung:" (STANDARDISIERT — immer dieser Begriff!)**
     - Quellenangabe kurz (Quelle, Jahr)
   - **Flexible Satzstruktur:** NICHT jede News gleich aufgebaut. Variiere zwischen Trend→Aktion, Problem→Chance, Marktveränderung→Hebel. Aber die Überschrift "Bedeutung für Beratungsdienstleistung:" bleibt identisch.
   - **Visuell identisch zu gestern** — nur die Inhalte und ihre Strukturierung sind neu.
   - Das Layout, die Bildposition, die Farbcodes, die Schriftgrößen bleiben alle gleich wie in der Vorlage.
   
   ⚠️ **HINWEIS:** Die standardisierte Wording "Bedeutung für Beratungsdienstleistung:" ist NUR auf Seite 1 (Cover Page)! Nicht auf Seiten 2–4!

10. **Seiten 2–4 schreiben — NUR Problem + Beratungsdienstleistung, KEINE Tools!** 

   **Links: blanke News mit „So What?" — MIT QUELLENANGABE AM BLOCKENDE**

   Jeder News-Block der linken Spalte hat **genau diese vier Bausteine in dieser Reihenfolge**:

   1. **Kategorie** in Großbuchstaben, Akzent-Blau (z. B. `KI IM BETRIEB`, `AUFSICHTSROLLEN`, `ASIEN`)
   2. **Headline** — eine Aussage, fett, dunkelblau
   3. **Fließtext** — Fakt nennen, Bedeutung erklären, Kontext setzen. Keine Beratung, keine Meinung. Grundschüler-Level. Zahlen fett hervorheben.
   4. **🔴 QUELLENANGABE — PFLICHT, NIEMALS WEGLASSEN:** Direkt unter dem Fließtext, eigene Zeile, in Klammern, klein und grau/kursiv.

   **Format der Quellenangabe (exakt so):**
   - Eine Quelle: `(Capgemini Research Institute, 2026)`
   - Mehrere Quellen: `(S&P Global & McKinsey, 2026; Hunton, 2026)` — mit **Semikolon** trennen
   - Mit Monat: `(Handelsblatt, August 2026)`

   ⚠️ **JEDER EINZELNE Block der linken Spalte auf Seite 2, Seite 3 UND Seite 4 endet mit dieser Quellenzeile.** Kein Block ohne Quelle. Das gilt auch für die Zahlen-Blöcke auf Seite 4. Danach folgt die dünne Trennlinie zum nächsten Block.

   
   **Rechts: Beratungshebel — NUR 2 Elemente (KEINE TOOLS!):**
   
   1. **Problem präzise erklären (sehr konkret, Grundschüler-Level + für Berater sinnvoll)**
      - Was ist das konkrete Problem bei Banken?
      - Wer hat das Problem?
      - Was kostet das Problem dem Geschäft?
      - Warum können Berater hier helfen?
      - Beispiel: "Alte Bankensysteme binden 40% des IT-Budgets für Wartung. Das Geld fehlt für neue Projekte. Das ist ein großer Wettbewerbsnachteil."
   
   2. **Beratungsdienstleistung konkret — super konkrete, klare Action Points!**
      - **KONKRETE Tätigkeiten, nicht abstrakt!**
      - ❌ Nicht: „Lösung bieten" oder „Modernisierung anbieten"
      - ✅ Ja: „Eine Checkliste schreiben, was die Bank ändern muss", „Ein Plan machen, wie neue Systeme langsam alte ersetzen", „Training für alle Mitarbeiter durchführen", „Neue Regeln aufschreiben, an die die Bank sich halten muss"
      - **Beispiel KONKRET:** "Wenn eine Bank alte Bankensysteme hat, die zu teuer werden, können Berater einen Plan schreiben: Die alte Software läuft noch weiter, während die Bank gleichzeitig eine neue Software aufbaut. Dann können die Daten peu à peu von alt zu neu übertragen werden, ohne dass der Bankbetrieb stoppt."
      - **Beispiel KAUDERWELSCH (❌ FALSCH):** "Sidecar-Strategie entwerfen" — Was ist das? Niemand versteht es!
      - **Action Points müssen verständlich sein, nicht fachlich beeindruckend!**
   
   **Beispiel-Struktur (gut):**
   - **Problem:** "Alte Bankensysteme binden 40% des Technik-Budgets. Ein kompletter Neubau dauert über fünf Jahre und kostet zu viel."
   - **Beratung:** "Einen Plan schreiben, wie die neue Software neben der alten startet und diese Stück für Stück ersetzt. Festlegen, welche alten Programmteile zuerst abgeschaltet werden. Planen, wie die Kundendaten sicher auf das neue System kommen."
   
   ⚠️ **KEIN 3. Element für Tools — dieser Platz ist reserviert für Problem + Beratung!**
   
   Fachbegriffe gehören hier hin, aber werden konkretisiert. Fokus: Präzises Problem + Konkrete Beratungsleistung. Keine Rollen-Spiele, keine Way Forwards, KEINE Tools-Erklärung.

   ⚠️ **Zur Klarstellung, weil hier schon einmal ein Fehler entstand:** Die Beratungsblöcke der **rechten** Spalte brauchen **keine** eigene Quellenangabe — sie sind Schlussfolgerung, nicht Meldung. Die **linke** Spalte dagegen bekommt **immer** eine Quellenangabe am Blockende (siehe oben). Dieses „keine Quellenangaben" bezieht sich **ausschließlich auf die rechte Spalte** und darf **niemals** auf die linke Spalte übertragen werden.

11. **Seite 5 erstellen.** APA-7-Referenzliste, alphabetisch sortiert.

12. **Layout anwenden — NICHT neu designen, 1:1 Vorlage kopieren.**
    - **Vorlage:** Kopiere die Struktur und das Design 1:1 aus der Datei, die du in Schritt 0 geöffnet hast — **vorrangig vom Desktop** (`/Users/marchaak/Desktop/Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf`), ersatzweise aus der Repo-Spiegelkopie (Abschnitt 12.1).
    - **Alle Seiten (1–5):** Nicht neu designen, nicht neu gestalten. Nur die Inhalte (Texte, Tabellen, Quellen, Datum) austauschen.
    - **Keine Änderungen an:** Farben, Schriftgrößen, Spaltenbreiten, Abstände, Icons, Balken, Header, Footer — nichts.
    - **Das Design ist täglich identisch.** Es gibt keine Variationen. Der Newsletter sieht optisch genauso aus wie gestern, nur mit anderen Texten.

13. **Checkliste durchgehen.** Schau Abschnitt 10 an. Passt alles?

13b. **🔴 MASCHINELLE QUALITÄTSPRÜFUNG — DAS TOR ZUM VERSAND.**

    Die fertige PDF wird durch das Prüfskript geschickt, **bevor** sie gepusht und versendet wird:

    ```bash
    python3 "Struktur/qualitaetspruefung.py" "Output/YYYYMMDD_Financial Services Consulting Newsletter.pdf"
    ```

    Das Skript prüft maschinell, was sich maschinell prüfen lässt:

    | Prüfung | Kriterium |
    | --- | --- |
    | Seitenzahl | genau 5 |
    | Cover-Raster | alle 3 Spaltenkanten bei x = 45,3 / 222,8 / 391,0 |
    | Füllung je Seite | höchstens 60 pt Leerraum über der Fußzeile |
    | Quellen auf Seite 5 | mindestens 45 Einträge |
    | Kurzbelege Seiten 2–4 | mindestens 5 je Seite in der linken Spalte |
    | Schreibweise | 0-mal „Prozent" ausgeschrieben |

    **Auswertung:**
    - **Rückgabewert 0** → alle Prüfungen bestanden, weiter mit Schritt 14
    - **Rückgabewert 1** → **NICHT pushen, NICHT versenden.** Die gemeldeten Punkte nachbessern und erneut prüfen.

    ⚠️ **Diese Prüfung ist kein Ersatz für die Checkliste, sondern eine zusätzliche Absicherung.** Sie erkennt Mengen und Layout, aber nicht, ob der Inhalt inhaltlich stimmt, ob die Quellen echt sind oder ob sich Aussagen wiederholen. Das bleibt Aufgabe der Abschnitte 5 bis 10.

14. **PDF speichern — GITHUB `main` IST DER PFLICHTWEG.**

    ⚠️ **Wichtig zur Laufumgebung:** Die Routine läuft in einer **Cloud-Umgebung ohne Zugriff auf den Mac**. Ein Schreibversuch nach `/Users/marchaak/Desktop/...` schlägt dort **immer** fehl. Deshalb gilt:

    - **Schritt 1 — Ins öffentliche Repository speichern (PFLICHT, immer zuerst):**
      - Datei: `YYYYMMDD_Financial Services Consulting Newsletter.pdf` mit **heutigem** Datum
      - Ziel: Repository `Daily-Banking-Newsletter`, Ordner `Output/`, Branch **`main`**
      - **Direkt auf `main` committen und pushen.** Kein Feature-Branch, kein Pull Request — sonst ist die öffentliche Adresse nicht erreichbar und der Mailversand scheitert.
      - Prüfen: Liefert die öffentliche Adresse Status 200 und beginnt der Inhalt mit `%PDF`? Falls NEIN → Fehler melden, **nicht** versenden.

    - **Schritt 2 — Lokale Archivkopie (nur wenn technisch möglich):**
      - Läuft der Newsletter **lokal auf dem Mac**: zusätzlich in `/Users/marchaak/Desktop/Banking Newsletter/Output/` ablegen.
      - Läuft er in der **Cloud-Routine**: Dieser Schritt entfällt ersatzlos. Das ist **kein Fehler** und **kein Grund**, den Mailversand zu stoppen. Das GitHub-Repository ist dann das Archiv.

    - **Merksatz:** GitHub `main` ist Pflicht und Voraussetzung für die Mail. Die lokale Kopie ist eine Zugabe, wenn die Umgebung sie zulässt.

15. **Mail automatisch versenden.** Folge den Anweisungen in `Mail Design/Mail Design.md`. Nach erfolgreichem Push auf `main`:
    - Abrufen: Die öffentliche Adresse der PDF wird aus dem Repository abgerufen
    - Prüfen: Status 200 und PDF-Header (`%PDF`) werden geprüft
    - Versenden: Die Mail geht über den Zapier-Connector an **`marc.haak@students.ebs.de`** mit der geprüften Adresse als Anhang (siehe Abschnitt 11.2)

---

## 9. Nicht erlaubt

- **KAUDERWELSCH — NIEMALS!** Sätze wie "Die Wirkung des digitalen Euro auf die eigenen Einlagen ist gerechnet" sind VERBOTEN! Jeder Satz muss vollständig sein und Sinn ergeben. Jemand ohne Bank-Wissen muss es verstehen!
- **Unverständliche Fachbegriffe ohne Erklärung:** "Sidecar-Roadmaps", "Governance-Modelle", "Datenmigration" sind FALSCH — schreib stattdessen in normalen Worten!
- **"Prozent" — NIEMALS!** Nur "%" verwenden! Nie "40 Prozent" oder "40 % ", sondern immer "40%"
- **Zu vage oder unpräzise Aussagen:** "Modernisierung bieten" oder "Lösung anbieten" ist FALSCH — schreib konkrete Tätigkeiten, die jemand versteht!
- Halbleere Seiten oder dünne Blöcke
- Meinungen oder Empfehlungen in der linken Spalte (Seiten 2–4)
- Nur reine Nachrichten-Wiederholung auf der rechten Spalte, ohne Beratungswert (Seiten 2–4)
- Nachrichten ohne Überschrift
- Zahlen ohne Jahresangabe oder Einheit
- Erfundene oder geschätzte Angaben ohne Kennzeichnung „geschätzt"
- **Quellenangaben auf Seite 1–4 OHNE kurzes Format.** Jede News muss eine Quellenangabe haben (McKinsey, 2026) — aber kurz und am Ende des Abschnitts, nicht als großer Textblock.
- **🔴 Quellenangaben nur auf der Cover Page.** Das ist ein realer, schon aufgetretener Fehler. Die linke Spalte auf **Seite 2, 3 und 4** braucht sie **genauso**. Ein News-Block ohne Quellenzeile ist unvollständig.
- Fußnoten, Endnoten, hochgestellte Verweiszeichen (außer: Datum in der Fußzeile)
- Eine andere Schriftart als Arial
- **Jede Abweichung vom Design-Muster:** Der gesamte Newsletter (Seiten 1–5) exakt nach `Example Design/Main Example_Financial Services Consulting Newsletter.pdf`. Keine visuellen Varianten. Jeder Newsletter sieht optisch identisch aus.
- **Neues Design jedes Mal:** Die Cover Page darf nicht täglich neu designed werden. Das Design ist Standard, nur Inhalte wechseln.
- **Layout-Improvisation:** „Heute machen wir die Überschrift größer" oder „Das Bild sieht hier besser aus" — nicht erlaubt. 1:1 Vorlage, täglich gleich.
- **Digitale Tools auf der rechten Spalte (Seiten 2–4) — KOMPLETT ENTFERNT!** Die rechte Spalte ist nur für Problem-Erklärung + Beratungsdienstleistung. Tools gehören dort NICHT hin. Kein Cloud Computing, keine APIs, keine „generischen Tools" — nichts davon! 100% Fokus auf Problem + Beratung.
- **Unpräzise Problemdarstellung.** „Systeme sind alt" ist nicht gut genug. „Alte Bankensysteme binden 40% des IT-Budgets für Wartung, statt dass das Geld in Innovation fließt" ist präzise und wird verstanden.
- **Abstrakte Beratungsleistungen.** „Optimierung", „Modernisierung", „Transformation" sind zu vage. Konkrete Action Points: „Audits durchführen", „Roadmaps schreiben", „Governance-Modelle aufbauen", „Schulungsprogramme entwickeln", „Datenmigration planen".
- **Gedankenstriche und Doppelpunkte im Fließtext.** `Die Bank hat ein Problem — sie ist zu langsam` ist nicht erlaubt → `Die Bank hat ein Problem. Sie arbeitet zu langsam` ist erlaubt. `Das Problem: alt` ist nicht erlaubt → `Das Problem sind die alten Systeme` ist erlaubt. **Bindestriche in zusammengesetzten Wörtern wie `EU-KI-Gesetz` bleiben erlaubt.** Doppelpunkte als Beschriftung (`Problem:`, `BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:`) bleiben ebenfalls erlaubt.
- **Erklärungen für allgemein bekannte Begriffe wie KI.** "KI (Künstliche Intelligenz)" nicht erklären. "Core Banking (zentrale Banking-Software)" aber ja — das ist Banking-spezifisch.
- Fachbegriffe ohne Konkretisierung. "Transaction Banking" allein ist nicht erlaubt. "Transaction Banking also Zahlungsverkehr zwischen Firmen" ist erlaubt.
- Abstrakte Probleme ohne Marktkontext. "Systeme sind alt" ist nicht erlaubt. "Alte Zahlungssysteme dauern drei bis fünf Tage, Kunden erwarten einen Tag" ist erlaubt.
- **News ohne „So What?" Erklärung — SEHR WICHTIG!** "KI-Adoption bei 11%" allein ist nicht erlaubt. Erkläre, was das bedeutet: "KI-Adoption bei 11% — das heißt, 89% der Banken nutzen KI noch nicht wirklich produktiv, obwohl 70% das planen. Das ist eine riesige Lücke zwischen Planung und Umsetzung". JEDE Zahl braucht ein „So What?" — warum ist das wichtig?
- **Zahlen ohne Kontextualisierung.** "Gewinn 55%, Ertrag 47%" allein ist nicht erlaubt. Erkläre: "Banken verdienen 55% Gewinn im Zahlungsverkehr, machen dort aber nur 47% des Umsatzes — das heißt, Zahlungsverkehr ist das lukrativste Geschäft, weil Maschinen es billig abwickeln"
- **Fakten ohne Bedeutung für Leser.** Jede Information muss einen Sinn haben, den ein Grundschüler sofort versteht. Nicht „Dies ist ein Fakt", sondern „Das bedeutet XYZ und ist wichtig, weil...". Das „So What?" ist ZENTRAL!
- Rollen-Spiele oder Way Forwards. "Sprechen Sie mit dem CFO" gehört nicht hier hin. Fokus auf Seiten 2–4: **Problem + Beratungsdienstleistung**. Fokus auf Seite 1: **Kontext + Bedeutung für Beratungsdienstleistung**.
- Themenfelder, die sich überschneiden (MECE verletzt)
- **🔴 Jede Form von Wiederholung.** Dasselbe Thema zweimal im Newsletter, dieselbe Zahl zweimal, dieselbe Aussage anders formuliert, dieselbe Beratungsdienstleistung bei zwei Themen, oder links und rechts dieselbe Information. Jede Information steht **genau einmal** über alle 5 Seiten hinweg (Abschnitt 5, Punkt 7b).
- **🔴 Wiederholungsfreiheit auf Kosten der Vollständigkeit.** Eine Dublette zu streichen und die Lücke **offen zu lassen**, ist verboten. Jede gestrichene Stelle wird durch ein **neues Thema mit neuer Quelle** ersetzt. Am Ende stehen weiterhin **mindestens 45 Quellen** und **volle Seiten** — beides gilt gleichzeitig und ungeschmälert (Abschnitt 5, Punkt 7b, Kopplung).
- **🔴 Ungeprüfte Quellen und Falschaussagen.** Eine Quelle nennen, die nicht aufgerufen wurde. Eine Zahl angeben, die so nicht in der Quelle steht. Eine Zahl aus dem Zusammenhang reißen. Eine ältere Zahl als aktuell darstellen (Abschnitt 6, Punkt 4b).
- Nicht genau 5 Seiten
- **Banking-Fachbegriffe ohne Erklärung.** "APIs" allein ist nicht erlaubt. "APIs also technische Schnittstellen, die Systeme verbinden" ist erlaubt. Jeder Banking-Fachbegriff, der nicht sofort klar ist, braucht eine Kurzerklärung.
- **Unternehmerische Meldungen (Product Launch, Partnerschaften) ohne Consulting-Key-Takeaway.** "Goldman Sachs und BlackRock partnern mit einem KI-Unternehmen" allein ist nicht erlaubt. Es muss rechts im Newsletter als **Problem + Beratungsdienstleistung** gezeigt werden, was Berater damit anfangen. Keine News ohne Beratungsanker.
- **Unspannende unternehmerische Infos.** "Kleinbank X hat neue App gestartet" ist zu dünn. Nur aufnehmen, wenn wirkliche Marktimplikation. Bei Platzproblemen: Weglassen.
- **Wiederholungen von alten News.** Mindestens **80 %** der Themen müssen neu sein gegenüber den **letzten 5 Tagen**. Ein Thema darf nur wiederkommen, wenn es eine **echte neue Entwicklung** gibt — dann wird ausschließlich das Neue berichtet. Wird ein Thema deswegen gestrichen, wird es durch ein **neues ersetzt**, nicht weggelassen (Kopplung in Abschnitt 5, Punkt 7b).
- **Den Push auf `main` auslassen.** Die PDF MUSS direkt auf Branch `main` des Repositories `Daily-Banking-Newsletter` liegen. Ein Feature-Branch oder ein offener Pull Request reicht **nicht** — die öffentliche Adresse liefert dann 404 und die Mail kann nicht versendet werden.
- **Wegen fehlender lokaler Kopie abbrechen.** Läuft die Routine in der Cloud, ist der Mac nicht erreichbar. Das ist erwartet und **kein Abbruchgrund**. Entscheidend ist allein der erfolgreiche Push auf `main`.
- **Halbleere Seiten abspeichern.** Jede der 5 Seiten muss bis unter 10 pt Restraum gefüllt sein (Abschnitt 4.6).
- **Weniger als 45 Quellen auf Seite 5.** Das ist eine harte Untergrenze, kein Richtwert (Abschnitt 6, Punkt 2).
- **Das 3×2-Raster der Cover Page verlassen.** Kein 2-Spalten-Layout, kein 1-Spalten-Layout. Text kürzen statt Raster ändern (Abschnitt 12.2).
- **Eine andere Design-Vorlage heranziehen** als `Main Example_Financial Services Consulting Newsletter.pdf` (Abschnitt 12.1).

---

## 10. Qualitäts-Checkliste vor der Ausgabe

⚠️ **KRITISCHES ERSTES SCREENING — DATUM + FORMAT-PRÜFUNG!**

**BEVOR du weitere Schritte machst, MUSS das überprüft werden:**

- [ ] **🔴 DATUM MUSS TÄGLICH WECHSELN!** Heutiges Datum ist? `DD.MM.YYYY` (z.B. `12.08.2026`)
- [ ] **Dateiname hat das aktuelle Datum:** `YYYYMMDD_...` (z.B. `20260812_...` für heute, NICHT `20260811_`)
- [ ] **Newsletter-Inhalt hat das aktuelle Datum:** "Ausgabe des 12.08.2026" (NICHT "Ausgabe des 11.08.2026")
- [ ] **Mail-Betreff hat das aktuelle Datum:** "...Ausgabe des 12.08.2026" (identisch mit PDF-Datum)
- [ ] **Alle drei Daten (Dateiname, Newsletter, Mail) sind IDENTISCH!** Nicht gemischt!
- [ ] **🔴 KEINE "Prozent" — NUR "%"!** Überall "40%" statt "40 Prozent" oder "40 %"
- [ ] **🔴 COVER PAGE (Seite 1): "Bedeutung für Beratungsdienstleistung:" (standardisiert)** — alle 6 News nutzen diese Wording, nicht variiert

---

- [ ] Der Titel `Financial Services Consulting Newsletter` steht auf Seite 1 (Cover Page)
- [ ] Das Datum `Ausgabe des DD.MM.YYYY` steht groß auf Seite 1
- [ ] Genau 5 Seiten: 1 Cover Page + 3 Inhaltsseiten + 1 Quellenseite
- [ ] **🔴 COVER PAGE IM 3×2-RASTER (3 Spalten × 2 Reihen) in einer weißen Karte** — nicht 2 Spalten, nicht 1 Spalte (Abschnitt 12.2)
- [ ] Seite 1 zeigt die 6 gewichtigsten News, jede mit: Nummer-Badge + Kategorie + Headline + Kontext + `BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:` + Quellenangabe
- [ ] **Längen eingehalten:** Kontext 200–320 Zeichen, je Punkt 60–110 Zeichen — sonst sprengt der Text die schmalen Spalten
- [ ] **Cover Page Wording: ALLE 6 News nutzen `BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:` — wortgleich, nicht variiert**
- [ ] **Kopfzeile Cover rechts zeigt `AUSGABE DES TT.MM.JJJJ`** — nicht einen Social-Media-Namen oder sonstigen Text
- [ ] Seite 2 zeigt das Ziel (Soll-Bild), Seite 3 zeigt die Wirklichkeit (Ist-Situation), Seite 4 zeigt Zahlen, Seite 5 zeigt Quellen
- [ ] **🔴 WOCHENTAG BESTIMMT UND FOKUS ANGEWENDET** (Schritt 1b): Der heutige Wochentag ist notiert, das zugehörige Themenfeld gewählt und die passende Tagesliste aus `02_Quellen-Matrix` verwendet ✓
- [ ] **🔴 SCHRITT 0 VOLLSTÄNDIG DURCHLAUFEN — VOR ALLEM ANDEREN:**
  - [ ] **Repo-Adresse aus der Routine** übernommen ✓
  - [ ] **Vorlage lokalisiert** — vorrangig vom Desktop `/Users/marchaak/Desktop/Banking Newsletter/Example Design/`, ersatzweise aus der Repo-Spiegelkopie ✓
  - [ ] **Vorlage gesichtet** — alle 5 Seiten angesehen, nicht aus dem Gedächtnis gebaut ✓
  - [ ] **🔴 REPOSITORY AUF VOLLSTÄNDIGKEIT GEPRÜFT** (Schritt 0d) — alle 10 Einträge der Pflichtliste liegen im Repo ✓
  - [ ] **War das Repository leer** (Neuaufbau)? Dann wurde die **komplette Pflichtliste** hochgeladen ✓
  - [ ] Fehlende oder abweichende Dateien wurden vom Desktop nachgeladen. Der Desktop ist der Master ✓
  - [ ] Bei Fehlen an beiden Orten wurde **nicht gebaut**, sondern gemeldet ✓
- [ ] **Der gesamte Newsletter (Seiten 1–5) entspricht 1:1 exakt dem Muster `Main Example_Financial Services Consulting Newsletter.pdf`** — keine Abweichungen. Jeder Newsletter sieht optisch identisch aus, nur die Texte wechseln.
- [ ] **Design wird NICHT täglich neu erstellt:** Cover Page, Layout, Farben, Schriftgrößen, Abstände, Icons — alles 1:1 wie in der Vorlage. Nur Inhalte sind neu.
- [ ] **Visuell identisch zu gestern:** Ein Leser, der zwei Ausgaben vergleicht, sieht optisch den gleichen Newsletter mit anderen Texten — keine Design-Unterschiede.
- [ ] **Cover Page (Seite 1) — dynamische Struktur:** Die 6 News haben nicht alle das gleiche Format. Variiere zwischen Trend→Aktion, Problem→Chance, Marktveränderung→Hebel. Flexibel strukturiert, nicht monoton.
- [ ] **Rechte Spalte Seiten 2–4 — NUR Problem + Beratungsdienstleistung, KEINE Tools!** Problem ist präzise erklärt (Grundschüler-Level + für Berater sinnvoll). Beratungsleistung hat konkrete Action Points (Audits, Roadmaps, Schulung, Governance, Stilllegungspläne).
- [ ] **KEINE digitalen Tools auf der rechten Seite!** Die rechte Spalte ist 100% reserviert für Problem-Erklärung + Beratungsdienstleistung. Tools bringen keinen Mehrwert und gehören nicht hier hin.
- [ ] **🔴 ACTION POINTS SIND SUPER KONKRET UND VERSTÄNDLICH — NICHT FACHBEGRIFFE!**
  - [ ] ❌ FALSCH: "Sidecar-Roadmap schreiben", "Governance-Modelle aufbauen", "Datenmigration planen"
  - [ ] ✅ RICHTIG: "Einen Plan schreiben, wie alte und neue Software parallel laufen", "Aufschreiben, wer welche Entscheidungen treffen darf", "Mitarbeiter schulen, damit sie die neuen Regeln verstehen"
  - [ ] Jemand ohne Bank-Wissen muss verstehen, was der Berater konkret tun wird
- [ ] Linke Spalte (Seiten 2–4) hat nur blanke News — keine Beratung, keine Meinung
- [ ] Rechte Spalte (Seiten 2–4) erklärt, was jede News für einen Berater bedeutet (**Problem + Beratungsdienstleistung**, keine Tools)
- [ ] Jeder Block links **und** rechts (Seiten 2–4) hat eine Überschrift
- [ ] Seite 3 hat eine Gap-Tabelle mit mindestens 5 Zeilen (Themenfeld | Ziel | Wirklichkeit | Lücke | Beratungs-Hebel)
- [ ] Seite 4 hat Wachstumsraten, Marktgrößen, Rückgänge und beste Verdiener — alle mit Zahlen und kurzer Begründung
- [ ] **🔴 FÜLL-TEST — ALLE 5 SEITEN SIND RANDVOLL (häufigster Fehler!):**
  - [ ] Seite 1 angesehen: alle 6 Boxen etwa gleich hoch gefüllt, **kein leerer Block unten** ✓
  - [ ] Seite 2 angesehen: mind. 8 News-Blöcke links, mind. 7 Beratungsblöcke rechts, **kein leerer Block unten** ✓
  - [ ] Seite 3 angesehen: mind. 8 News-Blöcke links, mind. 7 Beratungsblöcke rechts, Gap-Tabelle mit mind. 6 Zeilen, **kein leerer Block unten** ✓
  - [ ] Seite 4 angesehen: mind. 8 Zahlen-Blöcke links, mind. 7 Beratungsblöcke rechts, Rangliste + Negativliste, **kein leerer Block unten** ✓
  - [ ] Seite 5 angesehen: mind. 45 Quellen, zweispaltig, **kein leerer Block unten** ✓
  - [ ] **Bei sichtbarem Leerraum auf irgendeiner Seite: NICHT speichern.** Weitere Blöcke ergänzen (Abschnitt 4.6)
- [ ] **🔴 SPRACHE IST SUPER LEICHT VERSTÄNDLICH — KEIN KAUDERWELSCH!**
  - [ ] Jeder Satz ist vollständig und ergibt Sinn
  - [ ] Fachbegriffe sind erklärt (z.B. "APIs sind technische Verbindungen zwischen Programmen")
  - [ ] Keine unverständlichen Wörter wie "Wirkung", "gerechnet", "Sidecar", "Governance"
  - [ ] Jemand ohne Bank-Wissen versteht ALLES sofort
  - [ ] ❌ FALSCH: "Die Wirkung des digitalen Euro auf die eigenen Einlagen ist gerechnet"
  - [ ] ✅ RICHTIG: "Die europäische Zentralbank plant digitales Geld. Das ist elektronisches Bargeld auf dem Handy"
- [ ] **LINKE SPALTE — „So What?" ist ZENTRAL:** Jede News, jede Zahl hat eine Erklärung: Was bedeutet das? Warum ist das wichtig? Nicht einfach Fakten droppen.
- [ ] **Keine Zahlen ohne Erklärung:** "Gewinn 55%, Ertrag 47%" muss erklärt werden, was das bedeutet und warum es relevant ist. Grundschüler-Level verständlich.
- [ ] **Linke Spalte ist für Laien verständlich:** Auch jemand ohne Banking-Wissen versteht sofort, warum die News wichtig ist und was sie bedeutet. Jeder Fakt hat einen Sinn.
- [ ] **🔴 SATZZEICHEN — MENSCHLICH GESCHRIEBEN:**
  - [ ] **Kein Gedankenstrich im Fließtext** (`—` oder freistehendes `-`) → stattdessen zwei ganze Sätze ✓
  - [ ] **Kein Doppelpunkt im Fließtext** (`Das Problem: alt`) → stattdessen ein vollständiger Satz ✓
  - [ ] **Bindestriche in zusammengesetzten Wörtern sind erlaubt** (`EU-KI-Gesetz`, `KI-Agenten`) und wurden **nicht** künstlich aufgelöst ✓
  - [ ] **Beschriftungen mit Doppelpunkt sind unverändert** (`Problem:`, `BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:`) ✓
  - [ ] Jeder Absatz laut gelesen. Klingt wie ein Mensch, der erklärt — nicht wie eine Stichwortliste ✓
- [ ] **Nur Banking-spezifische Fachbegriffe erklären** (z.B. Core Banking, Transaction Banking, APIs, DORA), nicht allgemein bekannte Begriffe (KI, Automatisierung, Cloud)
- [ ] **🔴 KEINERLEI WIEDERHOLUNGEN — MECE ÜBER ALLE 5 SEITEN (Abschnitt 5, Punkt 7b):**
  - [ ] Thema und Kernaussage jedes Blocks notiert und **über alle 5 Seiten hinweg** nebeneinandergelegt ✓
  - [ ] **Kein Thema kommt zweimal vor** — ein Thema von Seite 1 taucht auf den Seiten 2 bis 4 nicht erneut auf ✓
  - [ ] **Keine zwei Blöcke sagen dasselbe** — auch nicht anders formuliert ✓
  - [ ] Alle genannten **Zahlen** gesammelt. **Keine Zahl kommt zweimal vor** ✓
  - [ ] Keine Beratungsdienstleistung erscheint bei zwei verschiedenen Themen ✓
  - [ ] **Links und rechts erzählen nicht dasselbe.** Rechts steht nur, was der Berater daraus macht ✓
  - [ ] Entstandene Lücken wurden mit **neuen** Themen gefüllt, nicht mit Umformulierungen ✓
  - [ ] **🔴 NACH DEM ENTFERNEN ALLER DUBLETTEN ERNEUT GEZÄHLT:**
    - [ ] Immer noch **mindestens 45 Quellen** auf Seite 5 ✓
    - [ ] Alle Seiten immer noch **voll** (Seiten 1–4 höchstens 40 pt, Seite 5 höchstens 80 pt Leerraum) ✓
    - [ ] Immer noch mind. **8 Blöcke links** und **7 rechts** je Seite ✓
    - [ ] **Kein einziger Block wurde ersatzlos gestrichen** ✓
- [ ] **🔴 QUELLENPRÜFUNG (Abschnitt 6, Punkt 4b) — JEDE QUELLE EINZELN:**
  - [ ] Jede Quelle **existiert wirklich** und wurde aufgerufen. Keine aus dem Gedächtnis konstruiert ✓
  - [ ] Jede Zahl **steht so in der Quelle** — nicht abgeleitet, nicht gerundet ✓
  - [ ] Zuordnung stimmt: richtige Organisation, richtiger Zeitraum, richtiger Bezugsrahmen ✓
  - [ ] Jahr und Monat stimmen mit der Quelle überein ✓
  - [ ] Bei Unsicherheit wurde die Meldung **weggelassen**, nicht ungeprüft aufgenommen ✓
- [ ] Die Struktur ist sauber — nichts überlappt sich (MECE)
- [ ] Highlights und klare Abgrenzungen sind gesetzt
- [ ] **🔴 SEITE 5 HAT MINDESTENS 45 QUELLEN — GEZÄHLT, NICHT GESCHÄTZT.** 45 ist der Boden, nach oben offen. Bei weniger als 45 → zurück in die Recherche, **nicht** speichern. Davon mindestens **10–12 aus anderen Ländern** oder internationalen Publikationen. Priorität: letzte 24–72 Stunden.
- [ ] **🔴 MINDESTENS 80 % DER THEMEN SIND NEU gegenüber den letzten 5 Tagen** — bei rund 30 Blöcken dürfen höchstens 6 fortgeführt werden, und nur bei echter neuer Entwicklung ✓
- [ ] Die Ausgaben der letzten 5 Tage wurden **vor dem Schreiben** durchgesehen und eine Themenliste erstellt ✓
- [ ] Wegen Vortags-Dopplung gestrichene Themen wurden durch **neue ersetzt** — Quellenzahl und Seitenfüllung sind unverändert erfüllt ✓
- [ ] **🔴 QUELLENANGABEN AUF ALLEN SEITEN 1–4 — HÄUFIGER FEHLER, EINZELN PRÜFEN:**
  - [ ] **Seite 1:** Jede der 6 Cover-Boxen endet mit `(Quelle, Jahr)` ✓
  - [ ] **Seite 2 linke Spalte:** **JEDER** News-Block endet mit `(Quelle, Jahr)` ✓
  - [ ] **Seite 3 linke Spalte:** **JEDER** News-Block endet mit `(Quelle, Jahr)` ✓
  - [ ] **Seite 4 linke Spalte:** **JEDER** Zahlen-Block endet mit `(Quelle, Jahr)` ✓
  - [ ] Format stimmt: klein, grau, in Klammern, eigene Zeile vor der Trennlinie; mehrere Quellen mit Semikolon ✓
  - [ ] **Es reicht NICHT, die Quellen nur auf der Cover Page zu haben.** Fehlt sie auf Seite 2, 3 oder 4 → nachtragen, nicht speichern.
- [ ] **Seite 5 ist im APA-7-Format:** Alphabetisch sortiert, vollständige Referenzen, enthält nur die Quellen, die auf Seite 1–4 verwendet wurden. Leser kann die kurzen Angaben von Seite 1-4 hier nachschlagen.
- [ ] Die Schriftart ist durchgängig Arial
- [ ] Keine Fußnoten außer dem Datum
- [ ] **Alle Banking-Fachbegriffe (z.B. „Core Banking", „APIs", „DORA") haben eine Kurzerklärung** — allgemeine Begriffe wie „KI" nicht erklären
- [ ] **Nur wirklich gewichtige unternehmerische Meldungen sind aufgenommen** (Partnerschaften mit Marktimplikation, relevante Launches). Unspannendes wurde weglassen.
- [ ] **Alle aufgenommenen unternehmerischen Meldungen (Partnerschaften, Product Launches) haben rechts ein Consulting-Key-Takeaway als Problem + Beratungsdienstleistung**
- [ ] Das Ergebnis ist eine PDF
- [ ] **🔴 MASCHINELLE QUALITÄTSPRÜFUNG BESTANDEN** (Abschnitt 8, Schritt 13b): `python3 "Struktur/qualitaetspruefung.py" "<PDF>"` liefert Rückgabewert **0**. Bei Rückgabewert 1 → **nicht pushen, nicht versenden**, erst nachbessern ✓
- [ ] **🔴 SPEICHERUNG — GITHUB `main` IST PFLICHT:**
  - [ ] Die PDF ist im Repository `Daily-Banking-Newsletter`, Ordner `Output/`, **direkt auf Branch `main`** gepusht ✓
  - [ ] **Kein Feature-Branch, kein offener Pull Request** — sonst liefert die öffentliche Adresse 404 ✓
  - [ ] **DATUM-KONTROLLPUNKT:** Der Dateiname trägt das **heutige** Datum (z.B. `20260812_` für 12.08.2026, nicht `20260811_`) ✓
  - [ ] Lokale Archivkopie in `/Users/marchaak/Desktop/Banking Newsletter/Output/` — **nur wenn die Umgebung Zugriff auf den Mac hat.** In der Cloud-Routine entfällt dieser Punkt und ist **kein Fehler** ✓
- [ ] **Öffentliche Adresse geprüft:** `https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Output/YYYYMMDD_Financial%20Services%20Consulting%20Newsletter.pdf` liefert Status 200 und PDF-Header (`%PDF`)
- [ ] Die Mail wurde über Zapier automatisch versendet. Die geprüfte öffentliche Adresse der PDF hängt als Anhang an der Mail.

---

## 11. Ausgabe

- **Format:** Die fertige PDF ist das einzige Auslieferformat.
- **Dateiname:** `YYYYMMDD_Financial Services Consulting Newsletter.pdf` mit heutigem Datum. YYYY = Jahr, MM = Monat, DD = Tag. Beispiel: `20260811_Financial Services Consulting Newsletter.pdf` für 11. August 2026.
- **Seitengröße:** A4 Hochformat, fünf Seiten insgesamt (1 Cover + 3 zweispaltig + 1 Quellen)
- **Schriftart:** Überall Arial
- **Fußzeile jeder Seite:** Nur das Datum in der Form `DD.MM.YYYY`
- **Wie es läuft:** Der Lauf wird automatisch ausgelöst über **Claude Routines**. Der Zeitpunkt wird dort eingestellt und ist nicht Teil dieser Datei.

### 11.1 Wo die PDF gespeichert wird — GITHUB `main` IST PFLICHT

⚠️ **ZUR LAUFUMGEBUNG — DAS IST DIE HÄUFIGSTE FEHLERQUELLE:**

Die Routine läuft in einer **Cloud-Umgebung ohne Zugriff auf den Mac**. Ein Schreibversuch nach `/Users/marchaak/Desktop/...` schlägt dort **immer** fehl — das ist kein Bug, sondern die Bauart der Umgebung. Deshalb ist die Reihenfolge:

⚠️ **DIE REPO-ADRESSE KOMMT AUS DER ROUTINE.**

Die Adresse des öffentlichen Repositories wird **in der Claude Routine hinterlegt** und bei jedem Lauf mitgegeben. Sie gilt für **beides**: das Sichern der Design-Vorlage (Abschnitt 8, Schritt 0) und das Ablegen der fertigen Ausgabe.
- **Immer die Adresse aus der Routine verwenden.** Sie hat Vorrang vor jeder Angabe in dieser Datei.
- Die unten genannte Adresse ist nur der **Standardwert**, falls die Routine keine angibt.
- **Fehlt die Adresse in der Routine und ist kein Standardwert nutzbar:** melden und nicht bauen.

**SCHRITT 1 (PFLICHT): Öffentliches Repository — direkt auf `main`**

| Angabe | Wert |
| --- | --- |
| Repository | **Adresse aus der Routine.** Standardwert: `Daily-Banking-Newsletter` (öffentlich) |
| Pfad im Repository | `Output/` |
| Branch | **`main`** — direkt, ohne Umweg |
| Dateiname | `YYYYMMDD_Financial Services Consulting Newsletter.pdf` mit **heutigem** Datum |

⚠️ **Direkt auf `main` committen und pushen.** Kein Feature-Branch. Kein Pull Request, der offen bleibt. Liegt die Datei nicht auf `main`, liefert `raw.githubusercontent.com` einen **404** — und der Mailversand wird nach eigener Regel („nicht senden, wenn die PDF nicht erreichbar ist") korrekt abgebrochen. Das Ergebnis: keine Mail, obwohl der Newsletter fertig ist.

**Verifikation:** Liefert die öffentliche Adresse Status 200 **und** beginnt der Inhalt mit `%PDF`?
- Falls JA → weiter zum Mailversand ✓
- Falls NEIN → **Fehler melden, nicht versenden**

**SCHRITT 2 (optional): Lokale Archivkopie**

- **Nur wenn die Umgebung Zugriff auf den Mac hat** (also bei lokaler Ausführung).
- Pfad: `/Users/marchaak/Desktop/Banking Newsletter/Output/`
- Läuft die **Cloud-Routine**, entfällt dieser Schritt ersatzlos. Das ist **kein Fehler** und **kein Grund**, den Mailversand zu stoppen — das GitHub-Repository ist dann das Archiv.
- Alte Ausgaben werden **nie** überschrieben und nie gelöscht.

⚠️ **KRITISCH — DATUM MUSS TÄGLICH WECHSELN:**

Das Datum im Dateinamen ist immer das **heutige**. Format YYYYMMDD:
- **12. August 2026** → `20260812_Financial Services Consulting Newsletter.pdf`
- **13. August 2026** → `20260813_Financial Services Consulting Newsletter.pdf`

**Das Datum der PDF und das Datum der Mail müssen täglich identisch sein.**

**Kompletter Ablauf:**
1. PDF erzeugt ✓
2. **Auf `main` pushen** (Repository `Daily-Banking-Newsletter`, Ordner `Output/`) ✓
3. **Verifikation:** Öffentliche Adresse liefert 200 + `%PDF`? Falls nein → FEHLER, STOP ✓
4. **Lokale Kopie**, falls die Umgebung es zulässt — sonst überspringen (kein Fehler) ✓
5. Weiter zum Mailversand ✓

### 11.2 Mail automatisch versenden — nach erfolgreichem Push auf `main`

⚠️ **ES GIBT GENAU EINEN VERSANDWEG: ZAPIER.**

Kein GitHub-Actions-Workflow, kein SMTP-Skript, kein zweiter Automatismus. Ein früher vorhandener Actions-Workflow wurde entfernt, weil er andere Dateinamen erwartete (`Newsletter_JJJJ-MM-TT.pdf`) als dieses Regelwerk vorgibt (`JJJJMMTT_Financial Services Consulting Newsletter.pdf`) — dadurch wurde nie versendet. **Es gilt ausschließlich der Dateiname aus Abschnitt 11.**

Der Mailversand erfolgt **nur nach erfolgreichem Push auf `main` und bestandener URL-Prüfung**. Der Versand läuft vollautomatisch — es wird **kein Entwurf** gespeichert.

**Ablauf (strenge Reihenfolge):**

1. **Push abgeschlossen:** PDF liegt auf `main` im öffentlichen Repository und die Adresse liefert 200 + `%PDF` ✓

2. **Mail-Text erstellen** nach `Mail Design/Mail Design.md`:
   - Betreff: `Financial Services Consulting Newsletter — Ausgabe des DD.MM.YYYY`
   - Aufbau: Hallo zusammen → 3 Rubriken à 3 Bullets → Hinweis auf PDF → Newsletter erscheint täglich → Schlusssatz → Gruß
   - Jeder Bullet: Kontext + konkrete Action Points für die Beratung (keine Tools)
   - Sprache: Menschlich, einfach, Banking-Begriffe erklärt

3. **Öffentliche Adresse der PDF abrufen und prüfen:**
   - Adresse: `https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Output/YYYYMMDD_Financial%20Services%20Consulting%20Newsletter.pdf`
   - Status-Code muss 200 sein (Datei vorhanden)
   - Datei-Header muss mit `%PDF` beginnen (echte PDF, nicht HTML/Text)
   - Falls Prüfung fehlschlägt: **Nicht versenden**, Fehler melden, warten auf Korrektur

4. **Mail über Zapier versenden:**
   - Werkzeug: `execute_zapier_write_action`
   - App: `GoogleMailV2CLIAPI`
   - Aktion: `message`, `tool_name` = `gmail_send_email`
   - Absenderkonto: `marc.haak77@gmail.com`
   - An: `marc.haak@students.ebs.de` (Cc und Bcc bleiben leer)
   - Betreff: `Financial Services Consulting Newsletter — Ausgabe des DD.MM.YYYY`
   - Body: Fertig formatierter Mailtext als HTML
   - Anhang (file): Die geprüfte öffentliche URL der PDF

5. **Erfolgsbestätigung:** Mail wurde versendet ✓

4. Die öffentliche Internet-Adresse der PDF wird geprüft. Der Server muss Status 200 geben (= Datei gefunden). Der Datei-Inhalt muss mit `%PDF` anfangen (= echte PDF, nicht HTML).

5. Die Mail wird über **Zapier** mit dem Gmail-Konto `marc.haak77@gmail.com` versendet. Die geprüfte Adresse wird im Feld für den Anhang eingetragen. Ein lokaler Dateipfad funktioniert dort **nicht**.

6. Der Empfänger ist: `marc.haak@students.ebs.de`. Die Felder Cc und Bcc bleiben leer.

7. Der Dateiname der PDF und der Inhalt der Mail müssen **das gleiche aktuelle Datum** haben. **Das Datum muss täglich aktualisiert sein.** 
   - Wenn heute der 11.08.2026 ist: Mail vom 11.08.2026 + PDF `20260811_Financial Services Consulting Newsletter.pdf`
   - Wenn heute der 12.08.2026 ist: Mail vom 12.08.2026 + PDF `20260812_Financial Services Consulting Newsletter.pdf`
   
   Wenn die Daten nicht übereinstimmen oder das Datum von gestern ist, wird die Mail **nicht** versendet. Sie wird stattdessen korrigiert.

8. Wenn die PDF nicht erreichbar ist, wird die Mail **nicht** versendet. Der Bericht des Laufs zeigt **deutlich**, dass das Problem ist.

---

## 12. Design-Vorlage

### 12.1 Die EINZIGE Design-Referenz

⚠️ **ES GIBT GENAU EINE DESIGN-VORLAGE. KEINE ZWEITE.**

**Der lokale Ordner auf dem Desktop ist die Quelle der Wahrheit (Master):**

```
/Users/marchaak/Desktop/Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf
```

Diese Datei ist die **verbindliche, unveränderbare 1:1-Vorlage für den gesamten Newsletter** (Seiten 1–5). Sie ist keine Inspiration. Sie ist kein Rahmen zum Variieren. Sie ist die **exakte Norm**.

⚠️ **WICHTIGE ABGRENZUNG — DIE VORLAGE IST DER DESIGN-MASSSTAB, NICHT DER INHALTS-MASSSTAB.**

| Bereich | Maßstab |
| --- | --- |
| **Layout, Raster, Spalten, Schriftgrößen, Farben, Bildposition, Kopf und Fuß** | **Die Vorlage-PDF. 1:1 kopieren.** |
| **Inhaltsregeln: Quellenzahl, Quellenangaben, Sprache, Satzzeichen, Wiederholungsfreiheit** | **Diese Datei (Struktur.md).** Die Regeln hier gehen bewusst über die Vorlage hinaus. |

Die Vorlage stammt aus einer früheren Ausgabe und erfüllt die **heutigen Inhaltsregeln nicht**. Eine maschinelle Prüfung der Vorlage zeigt: sie enthält nur 33 Quellen statt 45, hat **keine Kurzbelege** in der linken Spalte der Seiten 2–4 und schreibt „Prozent" 52-mal aus statt `%` zu verwenden.

**Das ist kein Fehler der Vorlage und kein Grund, sie zu ersetzen.** Sie bleibt der Design-Maßstab. Aber: **Kopiere niemals ihre Inhaltsmängel mit.** Konkret gilt für jede neue Ausgabe:
- **45 Quellen statt 33** (Abschnitt 6, Punkt 2)
- **Kurzbelege unter jedem News-Block der linken Spalte** auf den Seiten 2–4 (Abschnitt 6, Punkt 6) — die Vorlage hat sie nicht, deine Ausgabe braucht sie
- **Immer `%`, nie „Prozent"** (Abschnitt 9)

#### Zugriffsreihenfolge — in genau dieser Priorität

| Priorität | Ort | Wann |
| --- | --- | --- |
| **1 (Master)** | `/Users/marchaak/Desktop/Banking Newsletter/Example Design/` | **Immer zuerst versuchen.** Gilt, wann immer die Umgebung Zugriff auf den Mac hat (lokaler Lauf). |
| **2 (Spiegel)** | `Example Design/` im Repository **aus der Routine** (Standardwert `Daily-Banking-Newsletter`) | Nur wenn Priorität 1 nicht erreichbar ist (Cloud-Lauf ohne Mac-Zugriff). Die Repo-Kopie ist **immer nur ein Spiegel** des Desktop-Ordners und wird in Schritt 0d täglich aufgefrischt. |
| **Kein Fallback** | — | Ist **keiner** der beiden Orte erreichbar → **NICHT bauen.** Fehler melden (siehe unten). |

⚠️ **Der Desktop-Ordner gewinnt immer.** Wenn beide Orte erreichbar sind und sich unterscheiden, gilt die Datei vom Desktop. Die Repo-Kopie ist dann veraltet und wird mit der Desktop-Version überschrieben.

#### 🔴 Die gesamte Arbeitsgrundlage wird bei JEDEM Lauf ins Repository gesichert

Das Repository heißt immer gleich, wird aber gelegentlich **gelöscht und neu angelegt**, wenn sich Regelwerke ändern. Danach ist es leer. Ein Cloud-Lauf ohne Desktop-Zugriff hätte dann keine Arbeitsgrundlage. Deshalb ist das **Wiederherstellen der Arbeitsgrundlage der allererste Arbeitsschritt jedes Laufs** (Abschnitt 8, Schritt 0):

1. **Repo-Adresse** aus der Claude Routine übernehmen. Sie wird dort hinterlegt und steht bewusst nicht in dieser Datei.
2. **Vorlage lokalisieren** — Desktop zuerst, Repo als Ersatz.
3. **Vorlage sichten** — alle 5 Seiten ansehen.
4. **Repository auf Vollständigkeit prüfen** und alles Fehlende vom Desktop hochladen — Regelwerke, Recherche-Gerüst, Prüfskript, Design-Vorlage und Wallpaper (Pflichtliste in Schritt 0d). Der Desktop ist der Master und überschreibt abweichende Repo-Fassungen.

**Damit ist der Neuaufbau selbstheilend:** Nach dem Löschen des Repositories stellt der erste Lauf die komplette Arbeitsgrundlage wieder her, ohne manuelles Hochladen.

- **Ist der Desktop nicht erreichbar und das Repository leer** → **NICHT bauen.** Stattdessen melden: *„Die Design-Vorlage fehlt in beiden Ablagen."*
- **Niemals** aus dem Gedächtnis, aus einer alten Ausgabe oder aus einer Beschreibung bauen. Genau daraus entstand bereits ein falsches Cover-Raster.

#### Abgleich-Prüfung

Ob Desktop-Version und Repo-Version identisch sind, lässt sich über die Prüfsumme feststellen:

```bash
shasum -a 256 "/Users/marchaak/Desktop/Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf"
```

Weicht der Wert von der Repo-Kopie ab → **Desktop-Version ins Repository pushen**, damit der nächste Cloud-Lauf mit dem aktuellen Stand arbeitet.

**KEINE anderen Design-Quellen verwenden.** Konkurrierende Vorlagen wurden bewusst aus dem Repository entfernt, damit es keine zweite Wahrheit gibt. Falls dir eine der folgenden Dateien begegnet: **nicht als Layout-Vorlage verwenden.**
- ❌ `Main Example Newsletter.pdf` (alte Version — entfernt)
- ❌ `Example Picture Newsletter.png` (entfernt)
- ❌ `Cover Page Design.png` (entfernt)
- ❌ `Layout-Vorlage_Newsletter.html` (war veraltet, hatte nur 4 statt 5 Seiten und kein Cover-Raster — entfernt)
- ❌ `Marc Haak_Masterarbeit_Grobe Konzeption.pdf` (keine Design-Quelle)
- ❌ Ausgaben aus dem Ordner `Output` (sind Ergebnisse, keine Vorlagen)

**Einzige Bilddatei, die verwendet wird:** `Example Design/Newsletter_Wallpaper.jpeg` als Hero-Bild auf der Cover Page.

**Erster Arbeitsschritt vor jedem Bau:** Die Vorlage-PDF öffnen und ansehen. Wenn sie nicht lesbar ist, wird **nicht gebaut** — stattdessen wird der Fehler gemeldet (siehe Abschnitt 8, Schritt 0).

### 12.2 Exakte Maße der Vorlage (verbindlich, gemessen)

**Seitenformat alle 5 Seiten:** A4 Hochformat, 595 × 842 pt. Schriftart durchgehend **Arial**.

**Seite 1 — Cover Page:**

| Element | Position | Größe | Stil |
| --- | --- | --- | --- |
| Kopfband (dunkel) | y 0–28 | — | Fläche `#05415A` |
| Kopfzeile links `FINANCIAL SERVICES CONSULTING` | x 36.8, y 11.3 | 6.6 pt | Arial, gesperrt |
| Kopfzeile rechts `AUSGABE DES TT.MM.JJJJ` | rechtsbündig bis x 558, y 11.3 | 6.6 pt | Arial, gesperrt |
| Hero-Bild | y 28–400, volle Breite | — | Stadtbild mit dunkelblauem Verlauf |
| `TÄGLICHER MARKTÜBERBLICK FÜR BANKING-CONSULTANTS` | x 36.8, y 242 | 7.4 pt | Arial, gesperrt, weiß |
| `Newsletter` | x 36.8, y 258 | **42 pt** | Arial Bold, weiß |
| `Financial Services Consulting` | x 36.8, y 306 | **21 pt** | Arial regular, weiß |
| Intro-Text (2 Zeilen) | x 36.8, y 373 / 383 | 7.6 pt | Arial, weiß |
| `AUSGABE DES` | rechts, y 365 | 6.4 pt | Arial, gesperrt |
| Datum `TT.MM.JJJJ` | rechts, y 374 | **16 pt** | Arial Bold, weiß |
| **Weiße Karte** (Container der 6 News) | ab y ≈ 405 bis y ≈ 770 | — | Weiß, leichter Schatten, ragt über das Hero-Bild |
| Karten-Titel `DIE 6 WICHTIGSTEN MELDUNGEN DES TAGES` | x 45.3, y 423 | 8.6 pt | Arial Bold, `#05415A`, Großbuchstaben |
| Karten-Hinweis rechts | x 351.6, y 424 | 6.9 pt | Arial, grau |
| Fußzeile | y 793 / 804 | 7.0 pt | zentriert, auf dunklem Grund |

**Die 6 News auf Seite 1 — festes 3-Spalten-Raster (3 Spalten × 2 Reihen):**

| | Spalte 1 | Spalte 2 | Spalte 3 |
| --- | --- | --- | --- |
| Textkante x | **45.3** | **222.8** | **391.0** |
| Nummer-Badge x | 50.2 | 227.6 | 395.8 |
| Spaltenbreite | ca. 155 pt | ca. 155 pt | ca. 155 pt |

| | Reihe 1 (News 01–03) | Reihe 2 (News 04–06) |
| --- | --- | --- |
| Nummer-Badge y | **452** | **623** |
| Kategorie y | 467 | 638 |
| Headline y | 477 | 648 |

Dünne senkrechte Trennlinien zwischen den Spalten. Schriftgrößen in jeder News-Box:

| Element | Größe | Stil |
| --- | --- | --- |
| Nummer-Badge `01`–`06` | 6.6 pt | Arial Bold, weiß auf `#008CC8` |
| Kategorie (z. B. `REGULATORIK`) | 6.2 pt | Arial Bold, `#008CC8`, gesperrt, Großbuchstaben |
| Headline | 8.6 pt | Arial Bold, `#05415A`, max. 2 Zeilen |
| Label `BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:` | 6.1 pt | Arial Bold |
| Fließtext | 6.9 pt | Arial regular, `#1E2B33` |
| Quellenangabe | 6.1 pt | Arial kursiv, grau |

⚠️ **Das 3×2-Raster ist Pflicht.** Nicht auf 2 Spalten umstellen. Nicht auf 1 Spalte umstellen. Wenn Text nicht passt, wird **der Text gekürzt** — nicht das Raster geändert.

**Seiten 2–4 — Zwei-Spalten-Layout:**

| Element | Wert |
| --- | --- |
| Kopfband | `#05415A`, volle Breite, y 0–ca. 90 |
| Titel im Kopfband | `Financial Services` / `Consulting Newsletter` — **zweizeilig**, Arial Bold, weiß |
| Untertitel | `TÄGLICHER MARKTÜBERBLICK FÜR BANKING-CONSULTANTS`, gesperrt |
| Datum rechts im Kopfband | `AUSGABE DES` klein darüber, Datum groß und fett |
| Seitenband darunter | `#008CC8`, links `SEITE X — …`, rechts Kurzhinweis, weiße Schrift |
| Kernaussage-Box | Fläche `#DCEBFA`, linke Kante in `#008CC8`, 3 Punkte |
| Linke Spalte (News) | ca. 42 % Breite, weißer Grund |
| Rechte Spalte (Beratung) | ca. 58 % Breite, Grund `#DBEAF2` |
| Blocküberschrift rechte Spalte | Balken `#05415A`, weiße fette Schrift |
| Fußzeile | Datum `TT.MM.JJJJ`, rechtsbündig, klein grau |

**Aufbau eines News-Blocks in der linken Spalte (Seiten 2–4) — vier Bausteine, immer vollständig:**

| Baustein | Größe | Stil |
| --- | --- | --- |
| Kategorie (z. B. `KI IM BETRIEB`) | ca. 6.2 pt | Arial Bold, `#008CC8`, gesperrt, Großbuchstaben |
| Headline | ca. 8.0 pt | Arial Bold, `#05415A` |
| Fließtext | ca. 6.9 pt | Arial regular, `#1E2B33`, Zahlen fett hervorgehoben |
| **Quellenangabe** | ca. 6.1 pt | **Arial regular, grau `#8FA0AA`, in Klammern, eigene Zeile am Blockende** |
| Trennlinie darunter | 0.5 pt | `#7CBFDF` oder hellgrau, volle Spaltenbreite |

🔴 **Die Quellenzeile ist Teil des Blocks, nicht optional.** Sie steht direkt unter dem Fließtext, vor der Trennlinie. Mehrere Quellen werden mit **Semikolon** getrennt: `(S&P Global & McKinsey, 2026; Hunton, 2026)`.

**Seite 5 — Quellenverzeichnis:**

| Element | Wert |
| --- | --- |
| Kopfband + Seitenband | wie Seiten 2–4, Seitenband-Text `SEITE 5 — QUELLENVERZEICHNIS` |
| Einleitungszeile | „Alphabetisch nach Autor oder Organisation…" |
| Layout | **2 Spalten**, alphabetisch fortlaufend (links zuerst voll, dann rechts) |
| Format | APA-7, Autor fett/normal, Titel kursiv, URL in `#008CC8` |
| Schriftgröße | ca. 6.5 pt, enger Zeilenabstand |

### 12.3 Farbpalette (aus der Vorlage-PDF gemessen)

Diese Farben sind aus `Main Example_Financial Services Consulting Newsletter.pdf` ausgelesen. Sie sind die einzige gültige Palette.

| Farbe-Name | Farb-Code | Wofür benutzt |
| --- | --- | --- |
| Primärton (Dunkelblau) | `#05415A` | Kopfband, Überschriften-Balken, große Überschriften |
| Akzent-Blau | `#008CC8` | Seitenband, Kategorien, Nummer-Badges, Links, Trennlinien |
| Helles Akzent-Blau | `#7CBFDF` | Dünne Linien, Rahmen, Sekundär-Akzente |
| Hellblaue Fläche | `#DCEBFA` | Kernaussage-Box |
| Flächenblau hell | `#DBEAF2` | Hintergrund der rechten Spalte, Tabellen-Kopfzeilen |
| Hero-Verlauf hell | `#CFE0E9` | Verlauf im Cover-Bild |
| Hero-Verlauf mittel | `#C3D9E4` | Verlauf im Cover-Bild |
| Fließtext dunkel | `#1E2B33` | Fließtext, Tabellen-Inhalt |
| Sekundär-Text grau | `#8FA0AA` | Untertitel, Erklärungen, Fußzeile |
| Weiß | `#FFFFFF` | Hintergrund, Schrift auf dunklen Flächen |

Regeln für die Farbe:

- **Nur diese Farben.** Keine anderen. Keine Signal-Farben. Keine bunten Zusatz-Töne.
- **Kontrast prüfen.** Helle Schrift nur auf `#05415A` oder `#008CC8`. Dunkle Schrift nur auf weißen und hellblauen Flächen.

### 12.4 Was täglich wechselt und was nie wechselt

**Wechselt täglich (nur Inhalte):**
- Text der 6 News auf Seite 1
- Überschriften, Fließtext und Punktlisten auf Seiten 2–4
- Tabellendaten (Gap-Tabelle Seite 3, Ranglisten Seite 4)
- Quellenliste auf Seite 5
- Das Datum auf allen Seiten

**Wechselt nie (Design ist TABU):**
- Raster, Spaltenzahl, Spaltenbreiten, Positionen
- Schriftgrößen, Schriftart, Zeilenabstände
- Farben, Flächen, Balken, Trennlinien
- Hero-Bild, Kopfband, Fußzeile

**Die Regel in drei Sätzen:**
1. **Kopiere die Vorlage** (Layout, Farben, Schriftgrößen — alles)
2. **Ersetze nur die Texte** (News, Tabellen, Quellen, Datum)
3. **Der Newsletter sieht optisch identisch aus wie der von gestern** — nur die Inhalte sind neu.

### 12.5 Archiv

Alle bisherigen Ausgaben bleiben im Ordner `Output` und dienen als Archiv und für den Abgleich mit den letzten 5 Tagen. **Sie sind kein Design-Maßstab** — der Maßstab ist ausschließlich die Vorlage-PDF aus 12.1.
# Mail Design — Tägliche Versand-Mail zum Financial Services Consulting Newsletter

> **Zweck dieser Datei:** Standardisierte Arbeitsanweisung für die Begleitmail, mit der der tägliche Newsletter versendet wird. Die Mail ist die Kurzfassung des Newsletters. Sie wird bei jedem Lauf nach dieser Datei erstellt. Der inhaltliche Ursprung ist immer die Newsletter-PDF des jeweiligen Tages, erstellt nach `Struktur/Struktur.md`.

---

## 1. Rolle

Du bist derselbe **Newsletter-Mediadesigner und Redakteur mit langjähriger Erfahrung in der Banking-Industrie** wie in `Struktur.md`.
Für die Mail nimmst du zusätzlich die Perspektive eines **Beraters ein, der einem Führungskreis in 60 Sekunden das Wichtigste des Tages gibt**. Die Mail ist keine Zusammenfassung um der Vollständigkeit willen, sondern eine Auswahl: nur das, was heute wirklich zählt.

---

## 2. Kontext

- **Produkt:** Begleitmail zum täglichen `Financial Services Consulting Newsletter`.
- **Newsletter-Grundlage:** Der Newsletter wird täglich auf Basis von **45+ Top-Quellen recherchiert** (s. `Struktur/Struktur.md` Abschnitt 6 und `Recherche-Gerüst/02_Quellen-Matrix`). Die Mail extrahiert die Top 3 Insights pro Rubrik aus dieser breiten, fundierten Recherche.
- **Empfänger:** eine einzige feste Adresse (Abschnitt 4, Punkt 1). Es gibt keine Kopie-Empfänger.
- **Lesesituation:** Morgens, oft am Handy, oft zwischen zwei Terminen. Die Mail muss in unter einer Minute erfassbar sein.
- **Verhältnis zum Newsletter:** Die Mail **ersetzt den Newsletter nicht**. Sie macht neugierig und liefert die drei wichtigsten Erkenntnisse je Rubrik. Die Tiefe steht in der PDF.
- **Erstellung und Versand:** Beides läuft bei jedem Lauf **vollautomatisch**. Es wird **kein Entwurf** gespeichert und keine Freigabe eingeholt.
- **Datum:** Das Datum der Mail und das Datum der PDF müssen **identisch** und **täglich aktualisiert** sein. Wenn heute der 11.08.2026 ist, steht überall 11.08.2026. Wenn morgen der 12.08.2026 ist, steht überall 12.08.2026.
- **Versandweg:** über den **Zapier-Connector** mit der Gmail-Aktion *Send Email* (Abschnitt 10).
- **Zeitplan:** Wann der Lauf startet, wird **ausschließlich in den Claude Routines** festgelegt und ist nicht Teil dieser Datei. Im Mailtext erscheint **keine Uhrzeit**.
- **Anhang:** die Newsletter-PDF des Tages (`YYYYMMDD_Financial Services Consulting Newsletter.pdf`), abgerufen aus dem öffentlichen GitHub-Repository (Abschnitt 10.2).
- **Absender:** Marc Haak über das Gmail-Konto `marc.haak77@gmail.com`.

---

## 3. Aufgabe

Erstelle zur fertigen Newsletter-PDF des Tages die passende Versand-Mail. Ablauf:

0. **🔴 DATUM-KONTROLLPUNKT ZUERST!** — Welches Datum hat die Newsletter-PDF? (z.B. `20260812_...` für 12.08.2026?) Dieses exakte Datum muss in Mail-Betreff, Mail-Text und Anhang-Dateinamen wiederkommen. Wenn das Datum falsch ist, NICHT fortfahren — erst Newsletter-Datum korrigieren!

1. **Newsletter lesen** — die heutige Ausgabe vollständig durchgehen.
2. **Top 3 je Rubrik auswählen** — aus jeder der drei Rubriken die drei wichtigsten Insights extrahieren.
3. **Mail aufbauen** — nach der festen Reihenfolge in Abschnitt 4. **Betreff und Einleitungssatz müssen das aktuelle Datum haben!**
4. **Ton und Sprache prüfen** — höflich, freundlich, professionell (Abschnitt 6).
5. **Checkliste durchgehen** (Abschnitt 9).
6. **Anhang prüfen und versenden** — die PDF-Adresse mit korrektem heutigem Datum abrufen, dann die Mail über Zapier verschicken (Abschnitt 10).

---

## 4. Fester Aufbau der Mail

Die Reihenfolge ist immer gleich. Kein Element entfällt, keins wird umgestellt.

**1. Empfänger**

> **🔴 DIE REGEL IN EINEM SATZ:** Die Mail wird **täglich** von `marc.haak77@gmail.com` an **ausschließlich** `marc.haak@students.ebs.de` versendet. Cc und Bcc bleiben **leer**. Niemand sonst erhält die Mail.

Die Mail geht an **genau eine** Adresse. Sie ist bei jeder Ausgabe identisch.

**Absender (bleibt immer gleich):**
- `marc.haak77@gmail.com` (Gmail-Konto — ist **nur Absender**, niemals Adressat)

*An (einziger Empfänger):*

| Name | Adresse |
| --- | --- |
| Marc Haak | `marc.haak@students.ebs.de` |

Regeln zum Empfänger:

- **Absender:** `marc.haak77@gmail.com` — steht **nicht** im Feld `to`, `cc` oder `bcc`
- **An:** ausschließlich `marc.haak@students.ebs.de`
- **Cc:** bleibt **leer**
- **Bcc:** bleibt **leer**
- Es wird **kein** weiterer Empfänger ergänzt, solange diese Anweisung nicht geändert wird.
- Vor dem Versand wird die Adresse gegen diese Datei geprüft.

**2. Betreffzeile**
`Financial Services Consulting Newsletter — Ausgabe des DD.MM.YYYY`

⚠️ **KRITISCH — DATUM MUSS TÄGLICH WECHSELN!** Nicht immer "11.08.2026". Heute ist welcher Tag? Beispiel:
- Heute 12.08.2026 → `Financial Services Consulting Newsletter — Ausgabe des 12.08.2026`
- Heute 13.08.2026 → `Financial Services Consulting Newsletter — Ausgabe des 13.08.2026`

**3. Anrede**
Jede Mail startet mit:
`Hallo zusammen,`

**4. Einleitungssatz mit Datum**
Ein bis zwei freundliche Sätze, die immer **das AKTUELLE Datum der heutigen Newsletter-Ausgabe** nennen.
Muster: *„anbei findet ihr die heutige Ausgabe des Financial Services Consulting Newsletters vom DD.MM.YYYY. Nachfolgend die wichtigsten Erkenntnisse des Tages im Überblick."*

⚠️ **KRITISCH — DATUM MUSS TÄGLICH WECHSELN!** Nicht immer "11.08.2026". Das Datum im Einleitungssatz MUSS mit dem Newsletter-Datum übereinstimmen. Beispiel:
- Newsletter vom 12.08.2026 → Einleitungssatz muss sagen "...vom 12.08.2026"
- Newsletter vom 13.08.2026 → Einleitungssatz muss sagen "...vom 13.08.2026"

**5. Rubrik 1 — Marktübersicht**
Überschrift `Marktübersicht`, darunter **genau 3 Bullet Points** — die Main Top 3 Insights aus der Marktübersicht des Newsletters (Seite 1).

**6. Rubrik 2 — Marktrealität**
Überschrift `Marktrealität`, darunter **genau 3 Bullet Points** — die Main Top 3 Insights aus dem Status quo der Bankenindustrie (Seite 2).

**7. Rubrik 3 — Financial News**
Überschrift `Financial News`, darunter **genau 3 Bullet Points** — die Main Top 3 Insights aus den Financial Insights (Seite 3), jeweils mit Zahl.

**8. Hinweis auf die PDF**
Ein kurzer Satz, dass alle Details im angehängten Newsletter stehen.

**9. Professionelle Anmerkung zur Erscheinungsweise**
Ein kurzer, sachlicher Hinweis auf die **tägliche** Erscheinungsweise — **ohne jede Uhrzeit**.
Muster: *„Der Newsletter erscheint täglich."*

**10. Schlusssatz**
Jede Mail endet immer mit:
`Ich wünsche allen einen guten Start in den Arbeitstag.`

**11. Gruß**
Jede Mail endet final immer mit:

```
Viele Grüße
Marc
```

---

## 5. Inhaltsregeln für die neun Bullet Points

- **Genau 3 Bullets pro Rubrik**, also 9 insgesamt. Nicht mehr, nicht weniger.

**⚠️ NEUE MAIL-STRUKTUR (Weg vom starren Problem-Dienstleistung-Tools Format):**

- **Die starre „Problem → Dienstleistung → Tools" Struktur entfällt in der Mail** — sie wirkt zu statisch und monoton.
- **Neues Framework stattdessen:**
  1. **Kontext erklären** (leicht verständlich, Grundschüler-Level)
  2. **Action Points für Beratungshäuser aufzeigen**
  3. **Satzstruktur flexibel und dynamisch halten — Abwechslung im Aufbau**

**Beispiele für verschiedene, dynamische Satzstrukturen (NICHT immer das gleiche Muster):**

- ✅ **Variante A (Trend + Aktion):** "Die EZB hat neue Regeln für Künstliche Intelligenz gesetzt. Banken müssen ihre Modelle bis September einordnen. Beratungshäuser können dabei helfen, eine vollständige Liste aller Modelle zu erstellen und die Kontrollen zu prüfen. (EZB, 2026)"

- ✅ **Variante B (Lücke + Chancen):** "70% der Banken planen KI-Agenten, aber nur 11% setzen sie wirklich ein. Genau hier liegt die Chance für Berater. Sie können Betriebsmodelle aufbauen, Mitarbeiter schulen und den Einbau begleiten. (McKinsey, 2026)"

- ✅ **Variante C (Marktbewegung + Angebot):** "Wero hat inzwischen 43,5 Millionen Nutzer. Viele Häuser sind trotzdem noch nicht angeschlossen. Wer den Anschluss schafft, hält seine Kunden. (Fintech Radar, 2026)"

- ✅ **Variante D (Problem direkt + Lösungsansatz):** "Alte Bankensysteme binden 40% des IT-Budgets, Modernisierung fehlt Geld. Sidecar-Modelle bieten einen Ausweg ohne Komplettneubau. (Accenture, 2026)"

- ✅ **Variante E (Marktveränderung + Consulting-Hebel):** "Banken verdienen 57% ihrer Gewinne im Transaction Banking, aber nur 47% der Erträge kommen von dort. Provisionsmodelle neu bündeln ist das Thema. (Nomura, 2026)"
**Zentrale Regeln für Dynamik und Abwechslung:**

- **Abwechslung in Satzstruktur:** Nicht alle Sätze gleich beginnen. Mal kurz, mal länger. Mal mit Frage-Struktur, mal mit Aussage.
  - ❌ Falsch: "**Payments**: Das ist ein Problem. Wir bieten eine Lösung. Wir nutzen Tools."
  - ✅ Richtig: "**Zahlungsverkehr.** Die EZB hat neue Standards gesetzt. Banken müssen ihre Systeme deshalb umbauen. Berater können den Umbau planen und Schritt für Schritt begleiten."

- **Kontext first:** Der Leser versteht zuerst, worum es in der Branche gerade geht. Dann folgen die Chancen für Beratung.
  - Z.B. „Die EU hat neue Regeln für Banken-KI verabschiedet." oder „Der Markt wächst schnell, viele deutsche Häuser hängen hinterher."

- **Action Points SUPER KONKRET und VERSTÄNDLICH (für Beratungshäuser):** Nicht abstrakt „Beratung bieten" oder Fachbegriffe, sondern klar verständlich:
  - ❌ "Sidecar-Roadmap schreiben" (Was ist das?)
  - ✅ "Einen Plan schreiben, wie die alte Software neben der neuen läuft und langsam ersetzt wird"
  - ❌ "Governance-Modelle aufbauen"
  - ✅ "Aufschreiben, wer in der Bank welche Entscheidungen treffen darf und wie Regeln befolgt werden"
  - ❌ "Datenmigration planen"
  - ✅ "Planen, wie Kundendaten sicher von alten Computern zu neuen Computern übertragen werden"
  - **Action Points müssen verständlich sein, nicht fachlich beeindruckend!**

- **NUR generische, bekannte digitale Tools:** Cloud Computing, APIs, Automatisierung, Data Analytics, Compliance-Management, Cyber Security, RPA (Robotic Process Automation). KEINE Produktnamen oder Nische-Tools (MLflow, Databricks, Seldon, etc.) — Leser muss sofort verstehen, was gemeint ist.

- **Probleme präzise erklären:** Nicht „Systeme sind alt", sondern „Alte Bankensysteme binden die Hälfte des IT-Budgets, Modernisierung kostet Jahre und Geld". Grundschüler-Level verständlich, aber konkret und präzise.

- **Keine Monotonie:** Nicht jeder Bullet folgt dem gleichen Muster. Variiere zwischen:
  - Trend → Aktion
  - Problem → Chance
  - Lücke → Angebot
  - Marktbewegung → Geschäftsmodell-Shift
  - Wachstum → Consulting-Hebel

- **Banking-Fachbegriffe konkretisiert:** Nur Banking-spezifische, mit Erklärung in natürlicher Sprache.
  - ❌ Falsch: "**Core Banking** wichtig"
  - ✅ Richtig: "**Core Banking** also die zentrale Banking-Software braucht Modernisierung"

- **🔴 Satzzeichen, damit es menschlich klingt:**
  - **Bindestriche in zusammengesetzten Wörtern sind erlaubt** (`EU-KI-Gesetz`, `KI-Agenten`). Nicht künstlich auflösen.
  - **Kein Gedankenstrich im Fließtext.** Statt `Die Bank hat ein Problem — sie ist zu langsam` schreibe `Die Bank hat ein Problem. Sie arbeitet zu langsam`.
  - **Kein Doppelpunkt im Fließtext.** Statt `Das Problem: alt` schreibe `Das Problem sind die alten Systeme`.
  - **Beschriftungen mit Doppelpunkt bleiben erlaubt**, weil sie Struktur zeigen und nicht Teil eines Satzes sind.

- **Unternehmerische News (Partnerschaften, Product Launches) nur wenn wirklich gewichtig:** 
  - ❌ Nicht relevant: "Kleinbank X hat neue App gestartet"
  - ✅ Relevant: "Goldman Sachs und BlackRock arbeiten mit einem KI-Unternehmen zusammen und bieten gemeinsam Dienste an. Etablierte Häuser setzen also auf eigenes KI-Wissen. Beratungshäuser können den Einbau solcher Systeme planen und begleiten. (Anthropic, 2026)"

- **Rubrik „Financial News": jeder Bullet trägt eine Zahl** (Wachstumsrate, Marktvolumen, Marge) inklusive Einheit und Bezugsjahr.

- **Kurze Quellenangabe am Ende:** (Quelle, Jahr) — minimal, aber nachvollziehbar.

- **Keine neuen Inhalte:** Die Mail enthält nichts, was nicht auch im Newsletter des Tages steht.

- **Keine Dopplung:** Dieselbe Aussage erscheint nicht in zwei Rubriken (MECE gilt auch in der Mail).

- **Verständlichkeit für Laien:** Alle Banking-Fachbegriffe müssen auch für jemanden ohne Banking-Wissen verständlich sein. Erkläre immer in natürlicher Sprache.

**Zuordnung Newsletter → Mail**

| Mail-Rubrik | Quelle im Newsletter |
| --- | --- |
| Marktübersicht | Seite 2 — Wohin die Industrie sollte |
| Marktrealität | Seite 3 — Wie die Industrie wirklich steht |
| Financial News | Seite 4 — Zahlen und Geld im Markt |

---

## 6. Sprache und Ton — SUPER LEICHT VERSTÄNDLICH!

⚠️ **KRITISCH — GRUNDSCHÜLER-LEVEL DEUTSCH!**

- **Höfliches und freundliches Deutsch**, durchgängig.
- **Professionell aber LEICHT VERSTÄNDLICH:** Kein Insider-Jargon, kein Kauderwelsch. Vollständige Sätze, die Sinn ergeben.
- **❌ FALSCH:** "Die Wirkung des digitalen Euro auf die eigenen Einlagen ist gerechnet." (Niemand versteht das!)
- **✅ RICHTIG:** "Die europäische Zentralbank plant digitales Geld. Man kann es sich wie elektronisches Bargeld auf dem Handy vorstellen. Banken müssen sich darauf vorbereiten, damit ihre Kunden dieses digitale Geld nutzen können."
- **Vollständige, verständliche Sätze — immer!**
  - Nicht: "Regulatorik wird komplexer"
  - Sondern: "Es gibt immer mehr neue Regeln, die Banken beachten müssen. Eine neue Regel handelt von Datenschutz. Berater können Banken erklären, was sie ändern müssen, damit sie die neue Regel befolgen."
- **🔴 IMMER „%" SCHREIBEN, NIEMALS „Prozent" AUSSCHREIBEN:**
  - ❌ Falsch: `40 Prozent`, `40 %`, `vierzig Prozent`
  - ✅ Richtig: `40%`
  - Das gilt im gesamten Mailtext, in jedem der neun Bullets. Gleiche Regel wie im Newsletter (`Struktur.md` Abschnitt 9).
- **Satzzeichen, damit es menschlich klingt:**
  - Bindestriche in zusammengesetzten Wörtern sind **erlaubt**: `EU-KI-Gesetz`, `KI-Agenten`
  - Kein Gedankenstrich im Fließtext. Falsch: `Die Bank ist langsam — das kostet Kunden`. Richtig: `Die Bank ist langsam. Das kostet sie Kunden`
  - Kein Doppelpunkt im Fließtext. Falsch: `Das Problem: alt`. Richtig: `Das Problem sind die alten Systeme`
- **Fachbegriffe immer erklären:**
  - ❌ "APIs ermöglichen Integration" (Was sind APIs?)
  - ✅ "APIs sind technische Verbindungen zwischen Computerprogrammen. Sie funktionieren wie Leitungen, die Daten hin und her leiten"
  - ❌ "Core Banking Modernisierung"
  - ✅ "Die zentrale Software, die alle Bankkonten verwaltet, muss modernisiert werden"
- **Informativer Inhalt:** Der Leser soll DANACH wissen, was passiert — ohne woanders recherchieren zu müssen.
- **Wir-/Ihr-Ansprache** im kollegialen, respektvollen Ton. Konsistent über alle Ausgaben.
- **Keine Floskeln** über das hinaus, was in Abschnitt 4 als feste Formulierung vorgegeben ist.

---

## 7. Gestaltung und Format

- **Executive ready:** Die Mail ist auf einen Blick erfassbar, ohne Scrollen bis auf den ersten Bildschirm hinaus, sauber gegliedert, keine Textwüste.
- **Schriftart:** Arial, wie im Newsletter.
- **Rubriken-Überschriften:** fett, deutlich abgesetzt, in Dunkelblau entsprechend der Newsletter-Farbwelt.
- **Bullets:** einfache Punkte, gleichmäßige Abstände, keine Verschachtelung, keine Unterpunkte.
- **Farben und Bilder:** zurückhaltend. Kein Bildmaterial, keine Logos außer der Farbwelt des Newsletters. Die Mail bleibt textlich.
- **Länge:** insgesamt maximal rund **400 Wörter**. Das gibt Platz für detailliertere Aussagen pro Bullet und präzisere Kontexte.
- **Anhang:** `YYYYMMDD_Financial Services Consulting Newsletter.pdf` mit **HEUTIGEM DATUM**, nicht mit gestern. 
  - ❌ Falsch: `20260811_Financial Services Consulting Newsletter.pdf` (wenn heute der 12.08.2026 ist)
  - ✅ Richtig: `20260812_Financial Services Consulting Newsletter.pdf` (für heute, 12.08.2026)
  - Anhang wird immer an der Mail angehängt.

---

## 8. Nicht erlaubt

- **🔴 FALSCHES ODER ALTES DATUM!** Der Betreff, der Einleitungssatz und der Anhang MÜSSEN das heutige Datum haben. Ein gesternes oder vorgestriges Datum ist nicht erlaubt. Wenn heute der 12.08.2026 ist, darf NICHT "Ausgabe des 11.08.2026" stehen!
- **🔴 ADRESSATEN MÜSSEN KORREKT SEIN!** Die Mail geht an genau eine Adresse (Abschnitt 4):
  - **Absender:** `marc.haak77@gmail.com` — steht in **keinem** Empfängerfeld
  - **An:** ausschließlich `marc.haak@students.ebs.de`
  - **Cc und Bcc:** bleiben **leer**
  - Keine weiteren Empfänger hinzufügen, solange diese Anweisung nicht geändert wird
- Mehr oder weniger als 3 Bullets pro Rubrik
- Andere Rubriken oder eine andere Reihenfolge als Marktübersicht → Marktrealität → Financial News
- Fehlendes Datum der heutigen Ausgabe — das Datum MUSS im Betreff und im Einleitungssatz stehen, und es MUSS das heutige Datum sein
- **Bullets ohne 1–2 Sätze Kontext VORHER** — jeder Bullet braucht erst die Ausgangssituation erklärt
- Abweichungen von den festen Formulierungen: `Hallo zusammen,` / `Ich wünsche allen einen guten Start in den Arbeitstag.` / `Viele Grüße Marc`
- Inhalte, die nicht im Newsletter des Tages stehen
- Quellenangaben, Links oder Fußnoten in der Mail
- Lange Fließtextabsätze, Werbesprache, Ausrufezeichen
- **Gedankenstriche und Doppelpunkte im Fließtext.** `Die Bank hat ein Problem — sie ist zu langsam` nicht erlaubt → `Die Bank hat ein Problem. Sie arbeitet zu langsam` erlaubt. **Bindestriche in zusammengesetzten Wörtern wie `EU-KI-Gesetz` bleiben erlaubt.**
- **🔴 Jede Form von Wiederholung.** Keine Aussage, keine Zahl und kein Sachverhalt darf in der Mail zweimal vorkommen — auch nicht anders formuliert. Jeder der 9 Bullets sagt etwas **Eigenes**. Sagen zwei Bullets dasselbe, fliegt einer raus und wird durch ein neues Thema ersetzt.
- **🔴 Ungeprüfte Quellen und Falschaussagen.** Jede Zahl in der Mail muss so in der Quelle stehen und stammt aus dem Newsletter, der bereits geprüft wurde. Keine neuen, ungeprüften Zahlen in die Mail schreiben.
- **Banking-Fachbegriffe ohne Erklärung.** "APIs" allein ist nicht erlaubt. "APIs also technische Schnittstellen, die Systeme verbinden" ist erlaubt. "Core Banking" allein ist nicht erlaubt. "Core Banking also die zentrale Banking-Software" ist erlaubt.
- **Erklärungen für allgemein bekannte Begriffe.** "KI (Künstliche Intelligenz)" ist nicht erlaubt — das ist allgemein bekannt. "Automatisierung (automatische Prozesse)" ist nicht erlaubt — das ist klar.
- **Spezifische, unbekannte digitale Tools.** Produktnamen wie "MLflow", "Databricks", "Seldon", "Kubeflow" sind nicht erlaubt. NUR generische, bekannte Tools verwenden: Cloud Computing, APIs, Automatisierung, Data Analytics, Compliance-Management, Cyber Security, RPA.
- **Unpräzise Problembeschreibung.** "Systeme sind alt" ist nicht gut genug. "Alte Bankensysteme binden 40% des IT-Budgets für Wartung, Modernisierung braucht neue Ressourcen" ist präzise und wird verstanden.
- **Abstrakte Beratungsleistungen.** "Lösung bieten", "Optimierung", "Transformation" sind zu vage. Konkrete Action Points: "Compliance-Audits durchführen", "Governance-Modelle aufbauen", "Sidecar-Roadmaps schreiben", "Schulung geben", "Datenmigration planen"
- Fachbegriffe ohne konkrete Beispiele ("KI ist wichtig" ist falsch; "KI für Betrugserkennung, Berater kann das weiterverkaufen" ist richtig)
- **Unternehmerische Meldungen (Partnerschaften, Product Launches) ohne Consulting-Key-Takeaway.** "Goldman Sachs und BlackRock partnern mit einem KI-Unternehmen" allein ist nicht erlaubt. Es muss als **Kontext + konkrete Action Points** umgerahmt werden, damit Berater die Aktion kennen.
- **Unspannende unternehmerische Infos.** "Kleinbank X hat neue App gestartet" ist zu dünn, solange es keine echte Marktimplikation hat. Weglassen, wenn Platz knapp ist.
- Abstrakte Aussagen ohne Handlung ("Markt wächst" ist falsch; "Zahlungsverkehr wächst, Berater sollte mit Kunden über digitale Prozesse sprechen" ist richtig)
- Inhalte, die auch Laien ohne Banking-Wissen nicht verstehen — alle Banking-Fachbegriffe müssen konkretisiert sein
- **Jede Uhrzeitangabe im Mailtext** — weder im Fließtext noch in der Anmerkung zur Erscheinungsweise
- Die Mail als Entwurf speichern, statt sie zu versenden
- Eine andere Schriftart als Arial
- Versenden, ohne dass die PDF im Anhang hängt

---

## 9. Qualitäts-Checkliste vor dem Versand

⚠️ **KRITISCHES ERSTES SCREENING — DATUM-PRÜFUNG!**

**BEVOR du die Mail versendest, MUSS das Datum überprüft werden:**

- [ ] **🔴 DATUM MUSS TÄGLICH WECHSELN!** Welches Datum hat die Newsletter-PDF? (z.B. `20260812_...` für 12.08.2026?)
- [ ] **Betreff hat das aktuelle Datum:** `...Ausgabe des 12.08.2026` (NICHT `...Ausgabe des 11.08.2026`)
- [ ] **Mail-Einleitung hat das aktuelle Datum:** "...vom 12.08.2026" (identisch mit PDF-Datum)
- [ ] **Anhang hat das aktuelle Datum:** `20260812_Financial Services Consulting Newsletter.pdf` (identisch mit PDF-Datum)
- [ ] **Alle drei Daten (Betreff, Einleitung, Anhang) sind IDENTISCH!** NICHT gemischt!

---

- [ ] **Absender:** `marc.haak77@gmail.com` (nur Absender, steht in keinem Empfängerfeld)
- [ ] **An:** ausschließlich `marc.haak@students.ebs.de`
- [ ] **Cc:** leer
- [ ] **Bcc:** leer
- [ ] **🔴 DIE FELDER IN DER ZAPIER-AKTION SELBST GEPRÜFT** (Abschnitt 10.1): Dort stehen keine gespeicherten Alt-Adressen in `to`, `cc` oder `bcc`. Bei Fund → **nicht versenden**, erst bereinigen ✓
- [ ] Betreff enthält Titel und `Ausgabe des DD.MM.YYYY` (mit heutigem Datum)
- [ ] Mail startet mit `Hallo zusammen,`
- [ ] Das Datum der heutigen Newsletter-Ausgabe ist im Einleitungstext genannt (mit heutigem Datum)
- [ ] Drei Rubriken in der Reihenfolge Marktübersicht, Marktrealität, Financial News
- [ ] Genau 3 Bullet Points je Rubrik, insgesamt 9
- [ ] **Keine starre Problem-Dienstleistung-Tools Struktur in der Mail** — stattdessen flexibles Framework (Kontext + Action Points)
- [ ] **Abwechslung in Satzstruktur:** Nicht alle Bullets sehen gleich aus. Variiere zwischen Trend→Aktion, Problem→Chance, Lücke→Angebot, Marktbewegung→Hebel
- [ ] **Action Points konkret:** Spezifische Tätigkeiten für Beratungshäuser (Inventuren, Audits, Modellentwicklung, Schulung, etc.) — nicht abstrakt „Beratung bieten"
- [ ] Jeder Bullet beginnt mit einem fetten Schlagwort
- [ ] **Kontext leicht verständlich:** Grundschüler-Level, damit Leser sofort versteht, worum es geht
- [ ] Jeder Bullet der Rubrik Financial News enthält eine Zahl mit Einheit und Bezugsjahr
- [ ] **Jeder Bullet hat eine kurze Quellenangabe am Ende** (z.B. „McKinsey, 2026" oder „Financial Times, August 2026")
- [ ] **🔴 KEIN „Prozent" AUSGESCHRIEBEN — nur „%"** im gesamten Mailtext (z.B. `40%`, nicht `40 Prozent`) ✓
- [ ] **🔴 SATZZEICHEN im gesamten Mailtext:**
  - [ ] **Kein Gedankenstrich im Fließtext** → stattdessen zwei ganze Sätze ✓
  - [ ] **Kein Doppelpunkt im Fließtext** → stattdessen ein vollständiger Satz ✓
  - [ ] **Bindestriche in zusammengesetzten Wörtern sind erlaubt** (`EU-KI-Gesetz`) und wurden nicht aufgelöst ✓
- [ ] **🔴 KEINERLEI WIEDERHOLUNGEN:** Alle 9 Bullets nebeneinandergelegt. **Keine zwei sagen dasselbe**, auch nicht anders formuliert. Keine Zahl kommt zweimal vor ✓
- [ ] **🔴 QUELLENPRÜFUNG:** Jede Zahl in der Mail stammt aus dem bereits geprüften Newsletter. Keine neuen, ungeprüften Zahlen ergänzt ✓
- [ ] **Nur Banking-Fachbegriffe erklären**, nicht allgemeine Begriffe wie KI oder Automatisierung
- [ ] Hinweis auf die angehängte PDF vorhanden
- [ ] Professionelle Anmerkung zur täglichen Erscheinungsweise vorhanden — **ohne Uhrzeit**
- [ ] Im gesamten Mailtext steht keine einzige Uhrzeit
- [ ] Schlusssatz `Ich wünsche allen einen guten Start in den Arbeitstag.` vorhanden
- [ ] Mail endet final mit `Viele Grüße` / `Marc`
- [ ] Ton durchgängig höflich, freundlich und professionell
- [ ] **Die Mail liest sich dynamisch und nicht monoton** — verschiedene Satzstrukturen, Abwechslung in Aufbau, kein starres Schema
- [ ] **Action Points klar:** Jeder Bullet zeigt konkrete Tätigkeiten für Beratung auf (keine abstrakten „Lösungen")
- [ ] **Nur Banking-Fachbegriffe (Core Banking, APIs, DORA, Transaction Banking) haben eine Erklärung in natürlicher Sprache**
- [ ] **Nur wirklich gewichtige unternehmerische Meldungen sind aufgenommen** (Partnerschaften mit Marktimplikation, relevante Launches). Bei Platzproblemen: Unspannendes wurde weglassen.
- [ ] **Alle aufgenommenen unternehmerischen Meldungen (Partnerschaften, Product Launches) haben ein Consulting-Key-Takeaway als Kontext + konkrete Action Points**
- [ ] Keine Banking-Fachbegriffe ohne konkrete Erklärung oder Beispiel
- [ ] Keine abstrakten Aussagen (z.B. "Markt wächst") — nur konkrete Aussagen mit Berater-Aktion (z.B. "Zahlungsverkehr wächst, sprechen Sie mit Firmenkunden über Modernisierung")
- [ ] **Die Sprache ist so einfach und menschlich, dass ein Grundschüler alles versteht** — keine Insider-Jargon ohne Erklärung
- [ ] **Quellenangaben sichtbar:** Jeder Bullet hat eine kurze Quellenangabe am Ende zur Nachvollziehbarkeit. Volle Referenzen sind auf Seite 5 der PDF
- [ ] Arial, saubere Gliederung, maximal rund **400 Wörter** (genug Platz für Kontext + Detailtiefe + Quellenangaben)
- [ ] Die öffentliche Adresse der PDF wurde abgerufen und liefert wirklich eine PDF
- [ ] Die PDF hängt an der versendeten Mail mit **heutigem Datum**: `YYYYMMDD_Financial Services Consulting Newsletter.pdf` (z.B. `20260811_...` für 11.08.2026, `20260812_...` für 12.08.2026). **Das Datum muss täglich wechseln.**
- [ ] Die Mail wurde versendet, es wurde **kein** Entwurf gespeichert

---

## 10. Automatischer Versand über Zapier

⚠️ **ZAPIER IST DER EINZIGE VERSANDWEG.** Kein GitHub-Actions-Workflow, kein SMTP-Skript, kein zweiter Automatismus. Ein früher vorhandener Actions-Workflow wurde entfernt, weil er andere Dateinamen erwartete und dadurch nie versendet hat.

Die fertige Mail wird **sofort versendet**. Es wird **kein Entwurf** gespeichert und keine Freigabe abgewartet.

### 10.1 Versandweg

Der Versand läuft über den **Zapier-Connector** mit der Gmail-Aktion **Send Email**.

| Einstellung | Wert |
| --- | --- |
| Werkzeug | `execute_zapier_write_action` |
| App | `GoogleMailV2CLIAPI` |
| Aktion | `message`, `tool_name` = `gmail_send_email` |
| Absenderkonto | `marc.haak77@gmail.com` |

Die Felder werden so belegt:

| Feld | Inhalt |
| --- | --- |
| `from` | `marc.haak77@gmail.com` (nur Absender) |
| `to` | `marc.haak@students.ebs.de` (einziger Empfänger) |
| `cc` | **leer** |
| `bcc` | **leer** |

⚠️ **🔴 PFLICHTPRÜFUNG VOR JEDEM VERSAND — DIE ZAPIER-FELDER SELBST KONTROLLIEREN.**

Diese Datei legt fest, was die Routine einträgt. Die **Zapier-Aktion kann jedoch eigene, dauerhaft gespeicherte Werte** in den Feldern `to`, `cc` und `bcc` haben. Stehen dort noch Adressen aus einer früheren Konfiguration, versendet Zapier **trotzdem an sie** — unabhängig davon, was hier steht.

**Deshalb vor jedem Versand prüfen:**

| Feld in der Zapier-Aktion | Sollwert | Bei Abweichung |
| --- | --- | --- |
| `from` | `marc.haak77@gmail.com` | korrigieren |
| `to` | **ausschließlich** `marc.haak@students.ebs.de` | alle anderen Adressen **entfernen** |
| `cc` | **vollständig leer** | alle Einträge **entfernen** |
| `bcc` | **vollständig leer** | alle Einträge **entfernen** |

**Steht in `cc` oder `bcc` irgendeine Adresse: NICHT versenden.** Erst die Zapier-Aktion bereinigen, dann versenden. Es darf **niemand außer `marc.haak@students.ebs.de`** eine Mail erhalten.

**Der Versand erfolgt täglich** an genau diese eine Adresse, an jedem Wochentag, ohne Ausnahme.
| `subject` | `Financial Services Consulting Newsletter — Ausgabe des DD.MM.YYYY` |
| `body` | der fertige Mailtext als HTML |
| `body_type` | `html` |
| `from_name` | `Marc Haak` |
| `file` | die öffentliche Adresse der PDF aus Abschnitt 10.2 — **mit heutigem Datum** (Beispiel für 11.08.2026: `…/20260811_Financial%20Services%20Consulting%20Newsletter.pdf`, für 12.08.2026: `…/20260812_Financial%20Services%20Consulting%20Newsletter.pdf`) |

### 10.2 Herkunft der PDF

Das Feld `file` nimmt **keinen lokalen Dateipfad** an. Zapier läuft auf fremden Servern und kann ausschließlich eine **öffentlich abrufbare Adresse** herunterladen. Ein Dateipfad würde stillschweigend als Text behandelt und als `.txt` angehängt — die Mail wäre ohne Newsletter unterwegs.

Die PDF wird deshalb aus dem öffentlichen GitHub-Repository geholt.

⚠️ **DIE REPO-ADRESSE KOMMT AUS DER ROUTINE.** Sie wird in der Claude Routine hinterlegt und bei jedem Lauf mitgegeben. **Sie hat Vorrang vor jeder Angabe in dieser Datei.** Die unten genannte Adresse ist nur der Standardwert, falls die Routine keine angibt.

| Angabe | Wert |
| --- | --- |
| Repository | **Adresse aus der Routine.** Standardwert: `Daily-Banking-Newsletter` (öffentlich) |
| Pfad im Repository | `Output/` |
| Dateiname | `YYYYMMDD_Financial Services Consulting Newsletter.pdf` mit dem **heutigen Datum — jeden Tag neu**. Das Datum wechselt täglich:
  - 11. August 2026: `20260811_Financial Services Consulting Newsletter.pdf`
  - 12. August 2026: `20260812_Financial Services Consulting Newsletter.pdf`
  - 13. August 2026: `20260813_Financial Services Consulting Newsletter.pdf` |

Daraus ergibt sich die Adresse:

```
https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Output/YYYYMMDD_Financial%20Services%20Consulting%20Newsletter.pdf
```

Beispiel für 11. August 2026:

```
https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Output/20260811_Financial%20Services%20Consulting%20Newsletter.pdf
```

Diese Adresse ist **die gleiche** wie die lokale PDF, nur dass sie öffentlich im Repository liegt.

Das Leerzeichen im Ordnernamen wird als `%20` geschrieben. Heißt der Zweig nicht `main`, wird er entsprechend ersetzt.

### 10.3 Reihenfolge — zwingend einzuhalten

1. Die PDF wird ins öffentliche Repository committet und **direkt auf Branch `main` gepusht** (Dateiname `YYYYMMDD_Financial Services Consulting Newsletter.pdf` mit heutigem Datum). Eine lokale Archivkopie erfolgt nur, wenn die Umgebung Zugriff auf den Mac hat — in der Cloud-Routine entfällt sie und ist **kein Fehler** (siehe `Struktur.md` Abschnitt 11.1).
2. Die Adresse aus 10.2 wird **abgerufen und geprüft**: Der Server muss mit Status 200 antworten und der Inhalt muss mit `%PDF` beginnen.
3. Antwortet der Server mit 404, ist die Datei noch nicht ausgeliefert. Kurz warten und erneut prüfen, höchstens fünf Versuche.
4. **Erst nach erfolgreicher Prüfung** wird die Mail versendet — an die Adresse aus Abschnitt 4, Punkt 1 (`marc.haak@students.ebs.de`, Cc und Bcc leer).
5. Bleibt die Prüfung erfolglos, wird **nicht versendet**. Der Kurzbericht des Laufs weist deutlich auf das Problem hin.

Eine Mail ohne funktionierenden Anhang ist wertlos. Lieber kein Versand als eine Mail mit leerem oder falschem Anhang.

---

## 11. Mustermail

> **Von:** Marc Haak &lt;marc.haak77@gmail.com&gt;
> **An:** marc.haak@students.ebs.de
> **Betreff:** Financial Services Consulting Newsletter — Ausgabe des 11.08.2026
> **Anhang:** `20260811_Financial Services Consulting Newsletter.pdf`
>
> Hallo zusammen,
>
> anbei findet ihr die heutige Ausgabe des Financial Services Consulting Newsletters vom 11.08.2026. Nachfolgend die wichtigsten Erkenntnisse des Tages im Überblick.
>
> **Marktübersicht**
> - **Payments:** Kurzaussage zur wichtigsten Entwicklung im Zahlungsverkehr.
> - **KI & Automatisierung:** Kurzaussage zum neuen Marktstandard.
> - **Regulatorik:** Kurzaussage zur relevantesten Vorgabe aus Europa.
>
> **Marktrealität**
> - **Core Banking:** Kurzaussage, wo deutsche Häuser heute tatsächlich stehen.
> - **Process Management:** Kurzaussage zur größten Hürde im Tagesgeschäft.
> - **Datenqualität:** Kurzaussage zur Lücke zwischen Anspruch und Umsetzung.
>
> **Financial News**
> - **Consulting-Markt:** Wachstum von X % im Segment Y (2025).
> - **Marktvolumen:** Segment Z erreicht A Mrd. EUR (2025).
> - **Rückläufig:** Bereich B verliert C % gegenüber dem Vorjahr.
>
> Alle Details, Zahlen und Quellen findet ihr im angehängten Newsletter.
>
> Der Newsletter erscheint täglich.
>
> Ich wünsche allen einen guten Start in den Arbeitstag.
>
> Viele Grüße
> Marc
# Wochenstruktur — Fokus-Themenfelder Mo–So

> **Zweck:** Diese Datei definiert für jeden Wochentag einen eigenständigen Fokus-Themenbereich. Der tägliche Recherche-Prompt wird auf diesen Fokus zugeschnitten. So entsteht eine Woche mit breiter, durchmischter Abdeckung statt täglich gleicher Struktur.

---

## Montag — STRATEGISCHE TRENDS & ZUKUNFTSPERSPEKTIVE

**Frage an die Woche:** Wohin bewegt sich die Banking-Industrie langfristig?

**Fokus-Themenfelder (Priorisierung Mo):**
1. **Mega-Trends (Global-Level)** — Was verschiebt sich in den nächsten 12–36 Monaten?
2. **Executive Decisions** — Was entscheiden C-Suites gerade? Strategische Weichenstellungen?
3. **Digitalisierungs-Roadmaps** — Modernisierung, Transformation, New Banking Models
4. **Fintech-Integrationen & Partnerschaften** — Ökosystem-Entwicklung
5. **Regulatorische Vorausblicke** — Was kommt in den nächsten Monaten?
6. **Markt-Konsolidierung & M&A-Perspektive** — Wer kauft wen? Wohin geht der Markt?

**Perspektive:** Top-Down (C-Suite-Level, Boardroom-Sicht)  
**Geographisch:** Global, mit Fokus auf EU + USA + Innovationszentren (Singapore, Hong Kong)  
**Nachrichtentyp:** Long-term Trends, Strategic Outlooks, Research Reports  
**Beratungs-Hebel:** Strategie & Transformation  

---

## Dienstag — OPERATIVE REALITÄT & PROJEKT-REALITÄT

**Frage an die Woche:** Was tun Banken WIRKLICH? Wo kämpfen sie?

**Fokus-Themenfelder (Priorisierung Di):**
1. **Projekt-Realität** — Welche IT-/Modernisierungs-Projekte laufen? Welche scheitern?
2. **Operative Probleme** — Welche alltäglichen Herausforderungen gibt es?
3. **Cost Pressure & Effizienz** — Wo wird gespart? Welche Funktionen werden outgesourced?
4. **Legacy-System-Kämpfe** — Alte Systeme bremsen — konkrete Beispiele
5. **Skill Gaps & Recruitment** — Wo können Banken nicht rekrutieren? Talent-Lücken?
6. **Internal Transformations (Change Management)** — Wie schaffen es Banken, sich zu verändern?

**Perspektive:** Bottom-Up (Team-Level, Alltag, Operational Challenges)  
**Geographisch:** Deutschland + Europa (fokussiert auf wirkliche Operationen)  
**Nachrichtentyp:** Case Studies, Project Reports, Operational Data, War Stories  
**Beratungs-Hebel:** Operations & Modernization  

---

## Mittwoch — REGULIERUNG, COMPLIANCE & GOVERNANCE

**Frage an die Woche:** Was schreibt der Staat vor? Welche Standards?

**Fokus-Themenfelder (Priorisierung Mi):**
1. **Neue Regulierung** — EZB, EU, BaFin, Basel, AML, EBA-Guidelines
2. **Digital Operational Resilience (DORA)** — IT-Sicherheit, Cyber-Anforderungen
3. **AI Regulation & Governance** — Neue KI-Rules, was ändert sich?
4. **ESG & Nachhaltigkeits-Anforderungen** — Green Banking, Taxono­mie, Reporting
5. **Data Privacy & Compliance** — GDPR, neue Daten-Standards
6. **Governance Models** — Board-Komposition, 3 Lines of Defence, Risk Management

**Perspektive:** Compliance & Risk-View (Was ändert sich für die Bank?)  
**Geographisch:** EU/EZB (primär), dann USA/UK für Vergleiche  
**Nachrichtentyp:** Offizielle Guidelines, Regulatorische Ankündigungen, Compliance Reports  
**Beratungs-Hebel:** Risk & Compliance, Governance Transformation  

---

## Donnerstag — MÄRKTE, GESCHÄFTSMODELLE & FINANZEN

**Frage an die Woche:** Wie verdienen Banken Geld? Was funktioniert?

**Fokus-Themenfelder (Priorisierung Do):**
1. **Geschäftsmodell-Shifts** — Welche Bereiche wachsen? Welche schrumpfen?
2. **Profitabilität & Margen** — Wo ist das Geld? Provisionsmodelle?
3. **M&A Activity & Consolidation** — Wer kauft wen? Strategische Zukäufe?
4. **Retail vs. Corporate vs. Investment Banking** — Wo verdienen Top-Player?
5. **Market Share & Competitive Dynamics** — Wer gewinnt? Wer verliert?
6. **Digital Banking & Customer Economics** — Wie rentabel ist Fintech-Konkurrenz?

**Perspektive:** Financial & Investor-View (Was funktioniert wirtschaftlich?)  
**Geographisch:** Global Markets (USA, Europe, APAC-Fokus auf Growth)  
**Nachrichtentyp:** Financial Reports, M&A News, Market Analysis, Earnings Calls  
**Beratungs-Hebel:** Business Model Innovation, M&A Strategy  

---

## Freitag — INNOVATION, TECHNOLOGIE & ZUKUNFT

**Frage an die Woche:** Wer baut die Zukunft? Was entsteht gerade Neues?

**Fokus-Themenfelder (Priorisierung Fr):**
1. **AI & Machine Learning** — KI in Banking, Use Cases, Implications
2. **Fintech Startups & Unicorns** — Wer sind die neuen Player?
3. **Open Banking & APIs** — Ökosystem-Entwicklung, Third-Party Integration
4. **Blockchain & Crypto** — Digital Assets, CBDCs, Tokenisierung
5. **New Technologies** — Cloud, Edge Computing, Quantum, Web3
6. **Partnerships & Collaborations** — Tech Giants (Google, Amazon) im Banking?

**Perspektive:** Innovation & Forward-Looking (Was wird Standard?)  
**Geographisch:** Global Innovation Hubs (USA, Singapore, London, Berlin)  
**Nachrichtentyp:** Startup News, Tech Research, Partnership Announcements, Venture Funding  
**Beratungs-Hebel:** Digital Innovation, Technology Strategy  

---

## Samstag — KUNDENPERSPEKTIVE, RETAIL & EXPERIENCE

**Frage an die Woche:** Was wollen Kunden? Wie ändern sich ihre Erwartungen?

**Fokus-Themenfelder (Priorisierung Sa):**
1. **Customer Behavior Shifts** — Wie verändern sich Kundenbedürfnisse?
2. **Omnichannel & Digital Customer Experience** — Welche CX-Modelle funktionieren?
3. **Retail Banking Innovation** — Welche Banken gewinnen Retail-Kunden?
4. **Youth Banking & Next-Gen** — Wie banken sich Gen Z und Millennials?
5. **Financial Wellness & Advice** — Kundenerlebnis, Self-Service vs. Advice
6. **Payments & Everyday Banking** — Instant Payments, Mobile Wallets, User Adoption

**Perspektive:** Customer-Centric View (Was wünschen sich Kunden?)  
**Geographisch:** Deutschland + EU (Retail-fokussiert)  
**Nachrichtentyp:** Customer Research, Case Studies, User Experience Reports  
**Beratungs-Hebel:** Customer Experience & Digital Transformation  

---

## Sonntag — PEOPLE, ORGANIZATION & CULTURE

**Frage an die Woche:** Wie organisieren sich Banken neu? Wer arbeitet dort?

**Fokus-Themenfelder (Priorisierung So):**
1. **Talent & Recruitment** — Wo können Banken nicht genug finden?
2. **Skills & Learning** — Was müssen neue Bankiers können? Upskilling-Programme?
3. **Organizational Design** — Wie sehen neue Banking-Strukturen aus?
4. **Culture & Engagement** — Wie schaffen es Banken, Leute zu motivieren?
5. **Remote Work & Hybrid Models** — Wie arbeiten Banker heute?
6. **Diversity, Equity & Inclusion** — Wer führt Banken? Wer arbeitet dort?

**Perspektive:** People & Organizational View (Wer arbeitet im Banking der Zukunft?)  
**Geographisch:** Deutschland + Europa + Global Vergleiche  
**Nachrichtentyp:** HR Reports, Employee Research, Culture Case Studies, Leadership News  
**Beratungs-Hebel:** Organization & Talent Transformation  

---

## Überblick: Wochenabdeckung

| Tag | Primärer Fokus | Sekund. Fokus | Tertiar Fokus | Perspektive | Konsultation-Hebel |
| --- | --- | --- | --- | --- | --- |
| **Mo** | Strategische Trends | Fintech-Partnerschaften | M&A & Konsolidierung | Top-Down, Executive | Strategy & Vision |
| **Di** | Operative Realität | Legacy-System-Probleme | Effizienz & Cost | Bottom-Up, Teams | Operations & Modernization |
| **Mi** | Regulierung & Compliance | Cyber/DORA | AI-Governance | Risk & Compliance | Risk & Governance |
| **Do** | Geschäftsmodelle & Märkte | Profitabilität | M&A News | Financial & Investor | Business Model & M&A |
| **Fr** | Innovation & Technologie | Startups & Fintech | Neue Standards | Forward-Looking | Digital Innovation |
| **Sa** | Kundenperspektive | CX & Experience | Retail-Innovation | Customer-Centric | Customer Experience |
| **So** | People & Organization | Talent & Skills | Culture & Structure | HR & People | Organization & Culture |

---

## Schnittstelle zur Recherche

Diese Struktur wird TÄGLICH in den Recherche-Prompt eingebunden:
- Der Prompt variiert pro Wochentag
- Die Quellen werden auf den Fokus abgestimmt (s. Quellen-Gerüst)
- Die 6 News auf Seite 1 werden aus diesem Fokus-Themenfeld gezogen
- Die Seiten 2–4 folgen der Fokus-Perspektive des Tages
- Beratungs-Hebel werden auf den Fokus zugeschnitten
# Quellen-Matrix — Aktuelle Quellen + Erweiterung

> **Zweck:** Diese Datei katalogisiert alle verfügbaren Quellen, ordnet sie nach Themenfeld/Fokus und zeigt, welche Quellen täglich durchmischt werden. Sie ist eine lebende Liste — regelmäßig prüfen, Quellen hinzufügen.

---

## TIER 1 — KERNQUELLEN (PREMIUM, REGELMÄSSIG NUTZEN)

Diese Quellen werden bereits genutzt. **Täglich prüfen** — sie gehören zur Pflichtbasis, nicht zur Auswahl. Die 20 Kernquellen im Abschnitt „TÄGLICHE KERNQUELLEN" gelten an jedem Tag.

### Strategische Beratung & Research (Mo, Fr, Do)
- **McKinsey Global Institute** — strategy, trends, reports
- **Boston Consulting Group (BCG)** — industry reports, transformation
- **Bain & Company** — financial services research, M&A insights
- **Accenture Banking Reports** — fintech, transformation, technology
- **Deloitte Global Banking** — regulatory, market analysis
- **EY Banking & Capital Markets** — strategy, risk, governance
- **KPMG Financial Services** — insights, trends, transformation
- **Strategy& (PwC)** — thinking, strategy, business models
- **Roland Berger** — industry insights, German/European focus

### Nachrichten & Breaking News (Mo, Di, Do)
- **Financial Times** — banking news, global markets
- **Bloomberg** — financial data, market news
- **Reuters** — breaking news, global perspective
- **Handelsblatt** — German banking news
- **Wirtschaftswoche** — German business/banking
- **Wall Street Journal** — US focus, finance

### Regulierung & Compliance (Mi)
- **ECB (Europäische Zentralbank)** — press releases, guidelines, policy
- **EBA (European Banking Authority)** — banking standards, guidelines
- **BaFin (Bundesanstalt für Finanzdienstleistungsaufsicht)** — German regulations
- **EU-Kommission** — regulatory announcements
- **BIZ (Bank für Internationalen Zahlungsausgleich)** — standards, quarterly review

---

## TIER 2 — SPEZIALISIERTE QUELLEN (NEU HINZUFÜGEN, GEZIELT NUTZEN)

Diese Quellen sind spezialisiert auf einzelne Themenfelder. Sie werden über die **Tagesliste des jeweiligen Wochentags** eingebunden, die 42 Quellen umfasst und vollständig abgearbeitet wird.

### Digitale Transformation & Technology (Mo, Fr, Di)
- **Gartner Magic Quadrant** — technology reports, rankings
- **Forrester Wave** — fintech evaluation, tech trends
- **IDC Banking Tech** — digital banking analysis
- **TechCrunch** — startup news, tech innovations
- **The Block** — crypto/blockchain news
- **Fintech Magazine** — fintech industry coverage
- **InfoQ Banking Tech** — technical architecture, innovations
- **PwC Tech Trends** — emerging tech in finance

### Fintech & Startup Ecosystem (Fr, Mo, Do)
- **Crunchbase** — funding news, startup database
- **PitchBook** — venture capital, startup tracking
- **AngelList** — startup ecosystem, funding
- **Fintech Israel** — global startup trends
- **e27 (Fintech Asia)** — Asian fintech innovation
- **CB Insights** — fintech trends, innovation reports
- **Craft.co** — company data, startup intelligence

### Kundenverhalten & Retail Banking (Sa, Do)
- **Accenture Consumer Banking Study** — customer behavior
- **Capgemini World Retail Banking Report** — consumer trends
- **Morning Consult** — consumer research data
- **Statista Banking Data** — market size, consumer statistics
- **eMarketer** — digital banking adoption
- **Harris Insights & Analytics** — financial services consumer research

### Geschäftsmodelle & Markt (Do, Mo)
- **Oliver Wyman Banking & Financial Services** — industry reports, M&A
- **Booz Allen Hamilton** — strategy, transformation
- **A.T. Kearney** — market analysis, competitive landscape
- **Opimas** — financial services research
- **Euromoney** — institutional banking news
- **Global Trade Finance** — corporate banking trends

### Regulierung & Compliance — ERWEITERT (Mi, all days)
- **Politico EU** — regulatory news, policy developments
- **SIFMA (Securities Industry)** — US regulatory perspective
- **Global Financial Innovation Network** — regulatory sandboxes
- **Regulatory Intelligence (Thomson Reuters)** — compliance updates
- **IIF (Institute of International Finance)** — banking standards
- **EFAMA (European Fund Association)** — asset management regulation

### Innovation & AI (Fr, Mo)
- **Stanford AI Index Report** — annual AI trends
- **MIT Media Lab** — emerging technology research
- **AI Magazine** — AI trends in finance
- **Brookings Institution** — fintech & AI policy research
- **World Economic Forum** — global trends, finance/tech
- **WIPO (World IP Organization)** — patent trends, AI innovation
- **ACM Digital Library** — academic research on banking tech

### Talentmarkt & Organisation (So, Di)
- **LinkedIn Talent Solutions Blog** — hiring trends
- **Great Place to Work** — company culture rankings
- **CIPD (Chartered Institute Personnel Development)** — HR research
- **CEB/Gartner HR Insights** — organizational trends
- **Mercer Talent Reports** — compensation, organization design
- **Korn Ferry** — executive search, leadership insights
- **Executive Briefing** — C-suite perspectives

### Zahlungsverkehr & Transaction Banking (Do, Fr, Sa)
- **Nilson Report** — payments industry data
- **SWIFT** — global payments news, standards
- **Europarl** — instant payments regulation
- **Mastercard Insights** — payments trends
- **Visa Investor Relations** — payments market data
- **Federal Reserve Payments Study** — US payments data

### Cybersecurity & Operational Resilience (Mi, Di, Fr)
- **Gartner Cybersecurity Research** — security trends
- **Forrester Security** — security market analysis
- **Infosecurity Magazine** — cyber threats, banking security
- **Dark Reading** — cybersecurity news
- **CSA (Cloud Security Alliance)** — cloud/cyber standards
- **NIST (National Institute of Standards)** — security frameworks

### ESG & Nachhaltigkeits-Banking (Mi, Mo)
- **UN Principles for Responsible Banking** — ESG framework
- **Bloomberg ESG Data** — sustainability ratings
- **Sustainalytics** — ESG research
- **Carbon Trust** — sustainability reporting
- **GRI (Global Reporting Initiative)** — sustainability standards
- **Eurosif** — sustainable finance research

### M&A & Corporate Finance (Do, Mo)
- **Mergers & Acquisitions Journal** — M&A trends
- **Thomson Reuters Deals** — M&A news, data
- **pitchbook** — M&A analysis
- **Dealogic** — deal tracking, market analysis
- **Goldman Sachs Equity Research** — M&A perspective

### Akademische & Forschungsinstitute (All days)
- **Harvard Business School** — case studies, business research
- **LSE Banking Centre** — academic banking research
- **Oxford Saïd Business School** — fintech research
- **SSRN** — academic papers, pre-prints (finance)
- **ECBE (European Committee for Banking Ethics)** — banking ethics research

### Geografische Diversifikation — Länder-Reports
**Deutschland & deutschsprachig:**
- Institut der Deutschen Wirtschaft (IW)
- Bundesverband Deutscher Banken (BdB)
- Deutscher Sparkassenverband
- Genossenschaftsverband e.V.

**UK & Englischsprachig:**
- Bank of England Press Releases
- FCA (Financial Conduct Authority) Reports
- The City UK — financial center news

**USA:**
- Federal Reserve Economic Data (FRED)
- OCC (Office of the Comptroller)
- Federal Reserve Board Announcements
- Congressional Research Service — Banking Reports

**EU-weit:**
- EBA Public Consultations
- ESMA (European Securities Markets Authority)
- EIOPA (European Insurance Occupational Pensions)
- ECB Economic Bulletin

**APAC (Asia-Pacific) & Global:**
- Bank of Singapore Insights
- Hong Kong Monetary Authority
- Reserve Bank of Australia
- Financial Services Agency (Japan)
- Singapore's Monetary Authority

---

## TIER 3 — SPEZIALISIERTE NISCHEN-QUELLEN (MONATLICH NUTZEN)

Für Tiefe-Stories, wenn relevant. Nicht täglich, aber monatlich einstreuen.

### Spezialisiert auf Retail Banking
- **American Banker** — retail banking focused
- **Digital Banking Report** — retail/consumer banking
- **S&P Global Market Intelligence** — banking data

### Spezialisiert auf Corporate/Institutional Banking
- **Global Trade Finance** — trade finance trends
- **Insurance Journal** — insurance-banking convergence
- **Investment Management Digest** — wealth management

### Spezialisiert auf Blockchain/Crypto
- **Cointelegraph** — crypto/blockchain news
- **CoinDesk** — crypto markets, regulation
- **Messari** — crypto intelligence

### Spezialisiert auf Personalisierten Banking-Podcast
- **FinTech Insider Podcast** — fintech trends
- **The Banking Podcast** — banking topics
- **MPowered Podcast** — financial inclusion

---

## NUTZUNGSLOGIK NACH WOCHENTAG — 45+ QUELLEN TÄGLICH

> **WICHTIG:** Pro Tag recherchierst du in MINDESTENS 45 unterschiedlichen Top-Quellen, nicht nur 6–8. Die Quellen unten sind priorisiert (welche zuerst checken), aber ALLE gehören zur täglichen Recherche!

⚠️ **HARTE UNTERGRENZE — 45 QUELLEN AUF SEITE 5, NACH OBEN OFFEN:**
>
> Am Ende der Recherche werden die Einträge auf Seite 5 **gezählt**. Sind es weniger als 45, ist die Ausgabe **nicht fertig** und wird **nicht gespeichert** — dann werden weitere Quellen ausgewertet.
>
> **45 ist der Boden, nicht das Ziel.** Es gibt **keine Obergrenze**. 50, 60 oder 70 geprüfte Quellen sind besser als 45. Höre nicht auf, sobald 45 erreicht sind, sondern wenn der Themenfokus des Tages wirklich ausgeschöpft ist.
>
> Jede Tagesliste unten enthält **42 Quellen**. Dazu kommen die **Kernquellen**, die an jedem Tag gelten (siehe direkt darunter). Zusammen stehen damit **rund 60 Quellen pro Tag** zur Verfügung.

---

### 🔴 TÄGLICHE KERNQUELLEN — GELTEN AN JEDEM TAG, UNABHÄNGIG VOM FOKUS

Diese Quellen werden **an jedem einzelnen Wochentag** geprüft, zusätzlich zur Tagesliste. Der Themenfokus wechselt, diese Basis nicht. Damit ist sichergestellt, dass die Qualität der Datenlage an einem Mittwoch genauso hoch ist wie an einem Montag.

**Strategieberatung (die großen Häuser, jeden Tag):**
1. McKinsey & Company — Banking & Financial Services Insights
2. Boston Consulting Group (BCG) — Financial Institutions
3. Bain & Company — Banking Reports
4. PwC / Strategy& — Financial Services Thinking
5. Deloitte — Financial Services Insights
6. EY — Banking & Capital Markets
7. KPMG — Banking Insights
8. Roland Berger — Financial Services
9. Accenture — Banking Transformation
10. Oliver Wyman — Financial Services

**Wirtschaftsmedien (jeden Tag):**
11. Financial Times — Banking Section
12. Bloomberg — Finance & Markets
13. Reuters — Business & Finance
14. Handelsblatt — Banken & Finanzen
15. Wirtschaftswoche — Finanzen
16. Wall Street Journal — Financial Services

**Aufsicht und Institutionen (jeden Tag):**
17. EZB / ECB — Pressemitteilungen und Bankenaufsicht
18. BaFin — Meldungen und Aufsichtsmitteilungen
19. EBA (European Banking Authority) — Guidelines und Konsultationen
20. Deutsche Bundesbank — Publikationen und Statistiken

⚠️ **Diese 20 Kernquellen sind Pflicht an jedem Tag.** Sie ersetzen die Tagesliste nicht, sondern kommen hinzu. Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen pro Tag.** Damit sind 45 als Untergrenze bequem zu erreichen und deutlich mehr ist der Normalfall.

**Wenn eine Kernquelle heute nichts Relevantes meldet:** Das ist normal und kein Fehler. Sie wurde geprüft und liefert heute nichts. Weiter zur nächsten. Nur was tatsächlich verwendet wird, landet auf Seite 5.

---

### Montag — Strategische Trends (45+ QUELLEN TÄGLICH)

**Priorisiert (check diese ZUERST):**
1. McKinsey Global Institute
2. BCG Industry Report
3. Strategy& / PwC Thinking
4. Financial Times (global trends)
5. Oliver Wyman (strategy)
6. World Economic Forum (global trends)

**Danach auch (parallel recherchieren):**
7. Bain & Company Banking Reports
8. Accenture Banking Transformation
9. Deloitte Financial Services
10. EY Banking Strategy
11. KPMG Banking Insights
12. Roland Berger Banking
13. Bloomberg (strategy section)
14. Reuters (business/strategy)
15. Handelsblatt (Bankenstrategie)
16. Wirtschaftswoche (Banking)
17. Wall Street Journal (business)
18. Brookings Institution (finance)
19. Gartner Banking Reports
20. Forrester Banking Research
21. IDC Banking Tech
22. Oliver Wyman (additional reports)
23. Opimas (banking strategy)
24. Goldman Sachs Equity Research
25. A.T. Kearney Banking
26. Boston Consulting Group (additional)
27. Harvard Business Review (banking)
28. Stanford Business Insights
29. LSE Banking Centre
30. SSRN Finance (academic)
31. Global Financial Innovation Network
32. Europarlament Banking Reports
33. ECB Economic Bulletin
34. EBA Insights
35. BIZ Quarterly Review
36. IIF Institute Reports
37. World Bank Finance Reports
38. IMF Financial Stability Reports
39. Politico EU (banking policy)
40. Financial Conduct Authority (strategy)
41. Federal Reserve Economic Data
42. Regulatory Intelligence

**Resultat:** Du recherchierst täglich in 45+ Top-Quellen, not nur 6

### Dienstag — Operative Realität (45+ QUELLEN TÄGLICH)

**Priorisiert:**
1. Financial Times (operational stories)
2. Bloomberg (business news)
3. Handelsblatt (German operations)
4. Accenture Banking Reports
5. Wall Street Journal
6. Reuters (operational case studies)

**Danach auch (parallel):**
7. Capgemini Transformation Reports
8. Deloitte Operations
9. EY Operational Excellence
10. KPMG Banking Operations
11. McKinsey Operations
12. BCG Transformation
13. Bain Operations
14. Wirtschaftswoche (Betriebe)
15. Bankenverband Reports
16. Bundesbank Berichte
17. IDC Banking Operations
18. Gartner Operations Reports
19. Oliver Wyman (operations)
20. Financial Conduct Authority (operations)
21. ECB Banking Supervision Reports
22. EBA Operational Reports
23. BaFin Inspektionsberichte
24. Reuters Tech Operations
25. Bloomberg Operations
26. Harvard Business Review (operations)
27. MIT Sloan (operations)
28. Stanford Business (operations)
29. LSE Business Reports
30. SSRN Operational Papers
31. European Central Bank (supervision)
32. Financial Services Council Reports
33. Institute of Banking & Finance
34. Banking Standards Board
35. Payments UK (operational)
36. Open Banking Implementation Entity
37. Berlin Institut für Digitalisierung
38. European Banking Federation
39. Association for Financial Professionals
40. Institute of International Finance (operations)
41. Cambridge Centre for Risk Studies
42. Oxford Internet Institute

### Mittwoch — Regulierung & Compliance (45+ QUELLEN TÄGLICH)

**Priorisiert:**
1. ECB Press Releases
2. EBA Guidelines & Consultations
3. BaFin Announcements
4. EU-Kommission (regulatory)
5. BIZ Standards
6. Politico EU (policy)

**Danach auch (parallel):**
7. Regulatory Intelligence (Thomson Reuters)
8. CSA / NIST (cybersecurity)
9. UN Principles Banking
10. Federal Reserve Regulations
11. OCC Banking Supervision
12. Financial Conduct Authority (UK)
13. PRA (Prudential Regulation)
14. ESMA (Securities Regulation)
15. EIOPA (Insurance Regulation)
16. European Commission DG FISMA
17. ECB Banking Supervision
18. EBA Regulatory Technical Standards
19. Global Financial Innovation Network
20. Regulatory Affairs Institute
21. International Association of Banking
22. Basel Committee on Banking Supervision
23. Financial Action Task Force (AML)
24. FATF Guidance
25. Europol Financial Crime
26. Interpol Banking
27. World Bank Finance Standards
28. IMF Financial Stability Reports
29. WTO Financial Services
30. OECD Banking Guidelines
31. Council of Europe Finance
32. US Treasury FinCEN (AML)
33. Transparency International (Compliance)
34. World Bank Governance
35. Harvard Law School (Regulatory)
36. Oxford Centre for Regulatory Studies
37. LSE Centre for Regulatory Studies
38. Stanford Law (Regulatory)
39. Yale Law (Finance Regulation)
40. McKinsey Regulatory Insights
41. Deloitte Regulatory Updates
42. EY Regulatory Tracking

### Donnerstag — Märkte & Geschäftsmodelle (45+ QUELLEN TÄGLICH)

**Priorisiert:**
1. Bloomberg Markets
2. Financial Times (finance)
3. Reuters (financial news)
4. Thomson Reuters Deals
5. Goldman Sachs Equity Research
6. Oliver Wyman / Opimas

**Danach auch (parallel):**
7. Wall Street Journal (markets)
8. Handelsblatt (Finanzen)
9. Euromoney (institutional)
10. Mastercard Insights
11. Visa Investor Relations
12. S&P Global Market Intelligence
13. Morningstar (market data)
14. FactSet Research
15. Bloomberg Terminal Data
16. The Financial Times Markets
17. Reuters Financial Data
18. MarketWatch
19. Seeking Alpha (analysis)
20. Yahoo Finance (data)
21. Investing.com
22. Trading Economics
23. Statista Financial
24. McKinsey Financial Services
25. BCG Financial Services
26. Bain Financial Services
27. Accenture Finance
28. Deloitte Financial Markets
29. EY Financial Services
30. KPMG Finance
31. Oliver Wyman (additional M&A)
32. A.T. Kearney (markets)
33. Booz Allen Hamilton (markets)
34. Opimas (additional reports)
35. Pitchbook (M&A tracking)
36. Dealogic (M&A database)
37. Capital IQ (M&A)
38. Federal Reserve Financial Data
39. World Bank Financial Data
40. IMF Financial Statistics
41. BIS Statistical Bulletin
42. ECB Statistical Data Warehouse

### Freitag — Innovation & Technologie (45+ QUELLEN TÄGLICH)

**Priorisiert:**
1. TechCrunch (fintech)
2. Gartner Magic Quadrant
3. Forrester Wave
4. The Block (blockchain)
5. CB Insights
6. Stanford AI Index

**Danach auch (parallel):**
7. Crunchbase (funding data)
8. PitchBook (venture data)
9. AngelList (startups)
10. e27 (Asia fintech)
11. Fintech Magazine
12. Forbes (technology)
13. Wired (technology)
14. MIT Technology Review
15. Harvard Business Review (tech)
16. McKinsey Technology
17. BCG Technology
18. Accenture Technology
19. Deloitte Tech Trends
20. EY Technology
21. KPMG Tech Innovation
22. Gartner (additional)
23. IDC Technology
24. Forrester (additional)
25. InfoQ (tech architecture)
26. O'Reilly (tech learning)
27. Stack Overflow (developer trends)
28. GitHub Trends
29. ArXiv (AI research)
30. ACM Digital Library (research)
31. Stanford HAI (AI)
32. MIT Media Lab
33. Berkeley AI Research Lab
34. CMU AI Centre
35. Oxford Internet Institute
36. Cambridge Centre for Risk
37. World Economic Forum (tech)
38. Brookings Institution (tech)
39. RAND Corporation (tech)
40. Atlantic Council (fintech)
41. Open Banking Implementation Entity
42. SWIFT Innovation Reports

### Samstag — Kundenperspektive & Retail (45+ QUELLEN TÄGLICH)

**Priorisiert:**
1. Capgemini World Retail Banking Report
2. Accenture Consumer Banking Study
3. Morning Consult (consumer)
4. Statista Banking Data
5. eMarketer (adoption)
6. Harris Insights & Analytics

**Danach auch (parallel):**
7. Financial Times (consumer)
8. Bloomberg (consumer)
9. Reuters Consumer
10. Handelsblatt (Verbraucher)
11. Wirtschaftswoche (Consumer)
12. McKinsey Consumer Insights
13. BCG Consumer Study
14. Bain Consumer Research
15. Accenture Consumer (additional)
16. Deloitte Consumer
17. EY Consumer Research
18. KPMG Consumer
19. Forrester Consumer
20. Gartner Consumer
21. IDC Consumer Research
22. eMarketer (additional)
23. Pew Research Center
24. Pew Internet & Technology
25. Gallup Surveys
26. Nielsen Consumer Data
27. comScore Digital
28. Comscore Banking
29. Forrester Digital
30. J.D. Power Studies
31. American Customer Satisfaction Index
32. Net Promoter Institute
33. Forrester Customer Experience
34. McKinsey Customer Experience
35. Harvard Business Review (CX)
36. Stanford Business (CX)
37. Customer Experience Professionals Association
38. Forrester Voice of Customer
39. UserTesting Insights
40. SurveyMonkey Research
41. Qualtrics Research
42. Statista Consumer

### Sonntag — People & Organisation (45+ QUELLEN TÄGLICH)

**Priorisiert:**
1. LinkedIn Talent Solutions Blog
2. CIPD HR Research
3. Mercer Talent Reports
4. Great Place to Work Rankings
5. Korn Ferry (leadership)
6. Harvard Business Review (people)

**Danach auch (parallel):**
7. Financial Times (careers)
8. Bloomberg (careers)
9. Reuters Careers
10. Handelsblatt (Karriere)
11. Wirtschaftswoche (HR)
12. McKinsey People & Org
13. BCG Organizational
14. Bain Organization
15. Accenture Talent
16. Deloitte People
17. EY People & Culture
18. KPMG People Strategy
19. Gartner HR Research
20. Forrester HR
21. IDC HR Tech
22. Society for Human Resource Management (SHRM)
23. CIPD (additional)
24. People Analytics Institute
25. Conference Board (HR)
26. Gartner Learning
27. LinkedIn Learning Research
28. Udacity Insights
29. Coursera Impact
30. Harvard Kennedy School (leadership)
31. Stanford Graduate School (business)
32. MIT Sloan (organization)
33. Wharton School (management)
34. INSEAD (leadership)
35. IMD (leadership)
36. London Business School
37. Oxford Saïd Business
38. Harvard Law Forum (governance)
39. Yale School of Management
40. Northwestern Kellogg
41. Great Place to Work (additional)
42. Employee Benefit Research Institute

---

## QUELLEN-VERWALTUNG — LEBENDE LISTE

### Wöchentliche Prüfung
- [ ] Welche Quellen waren diese Woche noch nicht präsent?
- [ ] Gibt es neue Reports von Tier-1-Providern?
- [ ] Welche Tier-2-Quellen passen zu dieser Woche?

### Monatliche Prüfung
- [ ] Sind alte Quellen noch relevant?
- [ ] Gibt es neue Quellen-Anbieter in den Themenfeldern?
- [ ] Sollten neue Tier-2-Quellen in Tier-1 aufgestuft werden?

### Quartal-Review
- [ ] Welche Quellen-Kategorien sind unterrepräsentiert?
- [ ] Gibt es neue akademische Reports?
- [ ] Sollten geografische Quellen diversifiziert werden?

---

## TECHNISCHE INTEGRATION

Diese Quellen werden in den täglichen **Recherche-Prompt** (s. 03_Master_Recherche_Prompt) integriert:
- **Täglich werden 45+ Top-Quellen parallel recherchiert** — nicht nur 6–8, sondern alle 45+
- Die Quellen sind priorisiert (welche zuerst checken), aber ALLE gehören zur Tagesrecherche
- Quellen rotieren basierend auf Wochentag-Fokus (Mo: Strategie-Quellen, Di: Operativ-Quellen, etc.)
- Der Prompt erzeugt einen **durchmischten, breiten Überblick** aus 45+ Quellen statt täglich gleicher Perspektive
- Die besten 6 News des Tages werden aus den Findings der 45+ Quellen selektiert
# Master Recherche-Prompt — Template mit Tages-Variationen

> **Zweck:** Dieser Prompt ist das Herzstück der täglichen Recherche. Er wird täglich neu ausgefüllt, basierend auf dem Wochentag und den Fokus-Themenfeldern. Der Prompt variiert drastisch je nach Tag — nicht immer die gleiche Frage!

---

## ALLGEMEINE STRUKTUR DES PROMPTS

Der tägliche Prompt folgt dieser Logik:

```
1. ROLLENKLÄRUNG (kürzer, ändert sich je Tag)
2. TAGESFOKUS (welches Themenfeld steht im Fokus?)
3. GEOGRAPHISCHE FOKUSSIERUNG
4. QUELLENPRIORISIERUNG (welche Quellen heute nutzen?)
5. NACHRICHTENTYP (welche Art von News suchen wir?)
6. KONKRETE SUCHKRITERIEN (was genau interessiert uns?)
7. ERGEBNIS-FORMAT (6 News mit Struktur)
8. QUALITÄTSKRITERIEN
```

Jeder Tag hat eine einzigartige Ausprägung dieser Struktur.

---

## MONTAG — STRATEGISCHE TRENDS & ZUKUNFTSPERSPEKTIVE

```
DU bist ein Senior Analyst mit 15+ Jahren Erfahrung in Banking Strategy & Transformation.
Deine Aufgabe: Identifiziere die 6 strategischen Mega-Trends der kommenden Woche für die Banking-Industrie global.

FOKUS HEUTE — STRATEGISCHE TRENDS:
Die 6 News sollten beantworten:
- Wohin bewegt sich die Banking-Industrie langfristig? (12–36 Monate)
- Was entscheiden C-Suites und Vorstände gerade?
- Welche strategischen Weichenstellungen sind zu sehen?
- Welche Mega-Trends verschaffen wettbewerbliche Vorteile?
- Was wird zum neuen Banking-Standard?
- Welche Fintech-Partnerschaften entstehen?

GEOGRAPHISCHER FOKUS:
Priorisierung: EU (50%) → USA (30%) → APAC Innovation-Hubs Singapore/Hong Kong (15%) → Sonstige (5%)

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. McKinsey Global Institute (letzte 2 Wochen)
2. BCG — Industry Reports & Perspectives (Banking)
3. Strategy& (PwC) — Banking Thinking
4. Financial Times — Global Trends Section
5. Oliver Wyman — Strategy & Transformation Reports
6. World Economic Forum — Global Risks Report (Finance Section)

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
7–42. Alle Quellen aus Datei 02 (Quellen-Matrix), Montag-Abschnitt: Bain, Accenture, Deloitte, EY, KPMG, Roland Berger, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, WSJ, Brookings, Gartner, Forrester, IDC, Opimas, Goldman Sachs, A.T. Kearney, Harvard Business Review, Stanford, LSE, SSRN, Global Financial Innovation Network, ECB, EBA, BIZ, IIF, World Bank, IMF, Politico, FCA, Federal Reserve, Regulatory Intelligence

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN (gelten an JEDEM Tag, unabhängig vom Fokus):**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

→ Siehe Datei 02 (Quellen-Matrix), Abschnitt „TÄGLICHE KERNQUELLEN". Diese 20 kommen zur Tagesliste HINZU, sie ersetzen sie nicht.
→ Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen heute.**

**Ergebnis:** Du recherchierst täglich in 60+ Top-Quellen parallel. 45 auf Seite 5 sind die Untergrenze, nach oben offen!

NACHRICHTENTYP:
- Research Reports & Whitepapers (aktuell)
- Executive Interviews & Statements
- Strategic Announcements von Top Banks
- Think-Tank Artikel (Brookings, WEF, etc.)
- NOT: Operational News, Small-scale Announcements

KONKRETE SUCHFRAGEN:
- "Top banking trends Q3 2026"
- "Digital transformation in banking 2026"
- "Future of banking business models"
- "Banking mergers & consolidation strategy"
- "Fintech partnerships major banks 2026"
- "Regulatory changes shaping banking strategy"

ERGEBNIS-FORMAT (NUR FÜR COVER PAGE — SEITE 1):
Für jede der 6 News — SUPER LEICHT VERSTÄNDLICH, VOLLSTÄNDIGE SÄTZE!

- **Titel** (5 Worte max, aufreißend)
- **Kontext** (1–2 vollständige Sätze, Grundschüler-Level: Was passiert? Jemand ohne Bank-Wissen muss es verstehen!)
  - ❌ FALSCH: "Die Wirkung des digitalen Euro auf die eigenen Einlagen ist gerechnet"
  - ✅ RICHTIG: "Die europäische Zentralbank plant einen digitalen Euro — das ist elektronisches Geld, das man auf dem Handy hat. Viele Menschen werden das nutzen wollen."
- **Bedeutung für Beratungsdienstleistung:** (STANDARDISIERT — immer dieser Begriff! 3 KONKRETE, VERSTÄNDLICHE Tätigkeiten, nicht Fachbegriffe!)
  - ❌ FALSCH: "Sidecar-Roadmaps entwickeln", "Governance-Modelle entwerfen"
  - ✅ RICHTIG: "Einen Plan schreiben, wie die alte und neue Software zusammen laufen", "Aufschreiben, wer in der Bank welche Entscheidungen treffen darf", "Team-Training durchführen, damit Mitarbeiter die neuen Regeln verstehen"
- **Quellenangabe** (Quelle, Monat 2026, Jahr)
- **Satzstruktur flexibel** (nicht jeder Punkt gleich aufgebaut; Variation zwischen den 6 News, aber Wording "Bedeutung für Beratungsdienstleistung:" bleibt IDENTISCH)

QUALITÄTS-CHECKS:
✅ Jede News hat eine echte strategische Implikation (nicht: "Kleine Bank hat App gestartet")
✅ Beratungs-Hebel sind konkret — nicht abstrakt "Transformation bieten"
✅ Quellen sind seriös (Top Tier nur)
✅ Grundschüler-Level verständlich
✅ Alle 6 News sind unterschiedliche Themen (MECE)
✅ Keine Quellen-Wiederholung über mehrere Tage
```

---

## DIENSTAG — OPERATIVE REALITÄT & PROJEKT-REALITÄT

```
DU bist ein Operations Manager mit 15+ Jahren Banking-IT & Transformation.
Deine Aufgabe: Identifiziere die 6 operativen Herausforderungen und Real-World-Probleme, mit denen Banken JETZT kämpfen.

FOKUS HEUTE — OPERATIVE PROBLEME:
Die 6 News sollten beantworten:
- Was tun Banken WIRKLICH? Welche Projekte laufen?
- Wo scheitern Modernisierungs-Projekte?
- Welche Alltags-Probleme haben Banken?
- Wo ist der Cost Pressure am höchsten?
- Wo suchen Banken Talente und können nicht finden?
- Was sind die "Real World Pain Points"?

GEOGRAPHISCHER FOKUS:
Priorisierung: Deutschland (40%) → Rest EU (35%) → USA (20%) → Sonstige (5%)
[Grund: Operative Probleme sind oft lokal/regional]

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. Financial Times — Business & Operations
2. Bloomberg — Business News
3. Handelsblatt — Deutsche Banken & ihre Probleme
4. Accenture Banking — Transformation Case Studies
5. Reuters — Operational Stories
6. Capgemini — Digital Transformation Reports (Banking)

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
7–42. Alle weiteren Quellen aus Datei 02 (Quellen-Matrix), Dienstag-Abschnitt: Capgemini Transformation Reports, Deloitte Operations, EY Operational Excellence, KPMG Banking Operations, McKinsey Operations, BCG Transformation, Bain Operations, Wirtschaftswoche (Betriebe), Bankenverband Reports, Bundesbank Berichte, IDC Banking Operations, Gartner Operations Reports, Oliver Wyman (operations), Financial Conduct Authority (operations), ECB Banking Supervision Reports, EBA Operational Reports, BaFin Inspektionsberichte, Reuters Tech Operations, Bloomberg Operations, Harvard Business Review (operations), MIT Sloan (operations), Stanford Business (operations), LSE Business Reports, SSRN Operational Papers, European Central Bank (supervision), Financial Services Council Reports, Institute of Banking & Finance, Banking Standards Board, Payments UK (operational), Open Banking Implementation Entity, Berlin Institut für Digitalisierung, European Banking Federation, Association for Financial Professionals, Institute of International Finance (operations), Cambridge Centre for Risk Studies, Oxford Internet Institute

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN (gelten an JEDEM Tag, unabhängig vom Fokus):**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

→ Siehe Datei 02 (Quellen-Matrix), Abschnitt „TÄGLICHE KERNQUELLEN". Diese 20 kommen zur Tagesliste HINZU, sie ersetzen sie nicht.
→ Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen heute.**

**Ergebnis:** Du recherchierst täglich in 60+ Top-Quellen parallel. 45 auf Seite 5 sind die Untergrenze, nach oben offen!

NACHRICHTENTYP:
- Project Case Studies (was funktioniert, was nicht?)
- Interviews mit Banking-Operatoren
- Geschäftsbericht-Auszüge & Earnings Calls Transskripte
- War Stories: "Bank X hat Projekt Y stoppt"
- Cost Reduction / Efficiency News
- Recruitment & Skill Gap Reports

KONKRETE SUCHFRAGEN:
- "Banking project delays 2026"
- "German bank modernization challenges"
- "Legacy systems burden European banks"
- "IT cost reduction in banking"
- "Fintech talent shortage banking"
- "Failed banking transformation projects"

ERGEBNIS-FORMAT:
Für jede der 6 News:
- **Titel** (5 Worte max, konkret & anschaulich)
- **Problem** (1–2 Sätze: Was ist das konkrete Problem bei Banken?)
- **Action Points für Beratungshäuser** (3 Tätigkeiten: z.B. "Projekt-Health-Check durchführen", "Stilllegungsplan schreiben", "Schulungsprogramm entwickeln")
- **Quellenangabe** (Quelle, Monat 2026, Jahr)
- **Satzstruktur flexibel** (nicht monoton)

QUALITÄTS-CHECKS:
✅ Jede News beschreibt ein echtes, operatives Problem (nicht strategisch-abstrakt)
✅ Beratungs-Hebel sind konkrete Tätigkeiten (Audits, Roadmaps, etc.)
✅ Quellen sind glaubwürdig & aktuell
✅ Grundschüler-Level verständlich
✅ Alle 6 sind unterschiedliche Probleme (MECE)
```

---

## MITTWOCH — REGULIERUNG, COMPLIANCE & GOVERNANCE

```
DU bist ein Senior Regulatory Advisor mit 20 Jahren Banking-Regulierung & Compliance.
Deine Aufgabe: Identifiziere die 6 wichtigsten neuen oder kommenden Regulierungen, Standards & Compliance-Anforderungen.

FOKUS HEUTE — REGULIERUNG & GOVERNANCE:
Die 6 News sollten beantworten:
- Welche neuen Regeln, Standards oder Guidelines gibt es?
- Was zwingt Banken zur Veränderung?
- Welche Compliance-Anforderungen entstehen?
- Wie ändern sich Governance-Anforderungen?
- Welche Risiko-Standards sind neu?
- Welche Cyber/IT-Resilienz-Anforderungen entstehen?

GEOGRAPHISCHER FOKUS:
Priorisierung: EU/EZB (60%) → USA (20%) → UK (10%) → Sonstige (10%)

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. ECB (Europäische Zentralbank) — Press Releases & Guidelines
2. EBA (European Banking Authority) — Consultations & Final Guidelines
3. BaFin (Bundesanstalt) — Regulatory Announcements
4. EU-Kommission — Regulatory Proposals
5. BIZ (Bank für Internationalen Zahlungsausgleich) — Standards & Quarterly Review
6. Politico EU — Regulatory & Policy News
7. Regulatory Intelligence (Thomson Reuters)
8. CSA / NIST — Cybersecurity Standards (DORA-fokussiert)

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
9–42. Alle weiteren Quellen aus Datei 02 (Quellen-Matrix), Mittwoch-Abschnitt: UN Principles Banking, Federal Reserve Regulations, OCC Banking Supervision, Financial Conduct Authority (UK), PRA (Prudential Regulation), ESMA (Securities Regulation), EIOPA (Insurance Regulation), European Commission DG FISMA, ECB Banking Supervision, EBA Regulatory Technical Standards, Global Financial Innovation Network, Regulatory Affairs Institute, International Association of Banking, Basel Committee on Banking Supervision, Financial Action Task Force (AML), FATF Guidance, Europol Financial Crime, Interpol Banking, World Bank Finance Standards, IMF Financial Stability Reports, WTO Financial Services, OECD Banking Guidelines, Council of Europe Finance, US Treasury FinCEN (AML), Transparency International (Compliance), World Bank Governance, Harvard Law School (Regulatory), Oxford Centre for Regulatory Studies, LSE Centre for Regulatory Studies, Stanford Law (Regulatory), Yale Law (Finance Regulation), McKinsey Regulatory Insights, Deloitte Regulatory Updates, EY Regulatory Tracking

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN (gelten an JEDEM Tag, unabhängig vom Fokus):**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

→ Siehe Datei 02 (Quellen-Matrix), Abschnitt „TÄGLICHE KERNQUELLEN". Diese 20 kommen zur Tagesliste HINZU, sie ersetzen sie nicht.
→ Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen heute.**

**Ergebnis:** Du recherchierst täglich in 60+ Top-Quellen parallel. 45 auf Seite 5 sind die Untergrenze, nach oben offen!

NACHRICHTENTYP:
- Offizielle Regulatory Statements & Press Releases
- EBA Guidelines & Consultations
- Regulatory Roadmaps & Pipeline
- Compliance Requirement Updates
- Governance Best Practice Updates
- Cybersecurity & Operational Resilience (DORA) News

KONKRETE SUCHFRAGEN:
- "New EZB guidelines 2026"
- "EBA compliance requirements banking"
- "EU regulation banking AI 2026"
- "DORA cybersecurity requirements"
- "ESG regulatory requirements banks"
- "AML5 implementation news"
- "ECB governance expectations"

ERGEBNIS-FORMAT:
Für jede der 6 News:
- **Titel** (5 Worte max, regulatorisch klar)
- **Anforderung** (1–2 Sätze: Was ist die neue Anforderung? Wann tritt sie in Kraft?)
- **Implikation für Banken** (konkret: z.B. "Compliance-Audit erforderlich", "Governance-Modell anpassen", "Cyber-Investition nötig")
- **Action Points für Beratungshäuser** (3 konkrete Tätigkeiten: z.B. "Compliance Gap-Analyse durchführen", "Governance-Roadmap schreiben", "Audit-Programm aufbauen")
- **Quellenangabe** (Quelle, Monat 2026, Jahr)

QUALITÄTS-CHECKS:
✅ Jede News ist eine echte Regulatory Requirement (nicht spekulativ)
✅ Quelle ist offiziell (ECB, EBA, BaFin, EU — nicht Sekundärquellen)
✅ Implementierungs-Zeitlinie ist klar
✅ Auswirkungen auf Banken sind konkret beschrieben
✅ Grundschüler-Level verständlich
✅ Alle 6 sind unterschiedliche Regulierungen (MECE)
```

---

## DONNERSTAG — MÄRKTE, GESCHÄFTSMODELLE & FINANZEN

```
DU bist ein Financial Analyst & Banking Strategist mit 18 Jahren M&A & Market Intelligence.
Deine Aufgabe: Identifiziere die 6 wichtigsten Markt-Entwicklungen, M&A-News & Geschäftsmodell-Shifts.

FOKUS HEUTE — MÄRKTE & BUSINESS MODELS:
Die 6 News sollten beantworten:
- Wie verdienen Banken Geld? Welche Bereiche wachsen/schrumpfen?
- Welche M&A-Aktivitäten gibt es?
- Welche Geschäftsmodell-Verschiebungen entstehen?
- Wo sind die Margen heute?
- Welche neuen Wettbewerber gewinnen Marktanteile?
- Welche Profitabilitäts-Trends sind zu sehen?

GEOGRAPHISCHER FOKUS:
Priorisierung: Global (50%) → EU (25%) → USA (20%) → APAC (5%)

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. Bloomberg — Financial Markets & M&A News
2. Financial Times — Markets & Deals Section
3. Oliver Wyman / Opimas — Banking Market Reports
4. Thomson Reuters Deals / Dealogic — M&A Tracking
5. Goldman Sachs Equity Research
6. Euromoney — Institutional Banking News
7. Mastercard / Visa Investor Relations (Payments)

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
8–42. Alle weiteren Quellen aus Datei 02 (Quellen-Matrix), Donnerstag-Abschnitt: Handelsblatt (Finanzen), Euromoney (institutional), Mastercard Insights, Visa Investor Relations, S&P Global Market Intelligence, Morningstar (market data), FactSet Research, Bloomberg Terminal Data, The Financial Times Markets, Reuters Financial Data, MarketWatch, Seeking Alpha (analysis), Yahoo Finance (data), Investing.com, Trading Economics, Statista Financial, McKinsey Financial Services, BCG Financial Services, Bain Financial Services, Accenture Finance, Deloitte Financial Markets, EY Financial Services, KPMG Finance, Oliver Wyman (additional M&A), A.T. Kearney (markets), Booz Allen Hamilton (markets), Opimas (additional reports), Pitchbook (M&A tracking), Dealogic (M&A database), Capital IQ (M&A), Federal Reserve Financial Data, World Bank Financial Data, IMF Financial Statistics, BIS Statistical Bulletin, ECB Statistical Data Warehouse

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN (gelten an JEDEM Tag, unabhängig vom Fokus):**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

→ Siehe Datei 02 (Quellen-Matrix), Abschnitt „TÄGLICHE KERNQUELLEN". Diese 20 kommen zur Tagesliste HINZU, sie ersetzen sie nicht.
→ Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen heute.**

**Ergebnis:** Du recherchierst täglich in 60+ Top-Quellen parallel. 45 auf Seite 5 sind die Untergrenze, nach oben offen!

NACHRICHTENTYP:
- M&A Announcements & Deal News
- Quarterly Earnings (wenn relevant für Trends)
- Market Share & Competitive Dynamics Reports
- Business Model Innovation News
- Profitability & Margin Analysis
- Market Consolidation Stories

KONKRETE SUCHFRAGEN:
- "Banking M&A deals 2026"
- "Fintech acquisitions by banks"
- "Banking profitability trends Q2 2026"
- "Digital banking business model shift"
- "Market consolidation European banking"
- "Retail vs corporate banking profitability"
- "Payment systems market growth"

ERGEBNIS-FORMAT:
Für jede der 6 News:
- **Titel** (5 Worte max, markt-fokussiert)
- **Geschäftsmodell/Markt-Entwicklung** (1–2 Sätze: Was ändert sich?)
- **Finanzielle Implikation** (konkret: "XYZ Bereich verdient jetzt Y% Marge")
- **Action Points für Beratungshäuser** (3 Tätigkeiten: z.B. "M&A-Due-Diligence durchführen", "Business Model Rebalancing entwerfen", "Pricing-Strategie überarbeiten")
- **Quellenangabe** (Quelle, Monat 2026, Jahr)

QUALITÄTS-CHECKS:
✅ Jede News hat finanzielle oder Markt-Relevanz
✅ Zahlen sind konkret & zeitlich verortet
✅ M&A-Deals sind größere, strategische Moves (nicht: Kleinbank kauft App)
✅ Geschäftsmodell-Shifts sind real & substanziell
✅ Grundschüler-Level verständlich
✅ Alle 6 sind unterschiedliche Märkte/Deals (MECE)
```

---

## FREITAG — INNOVATION, TECHNOLOGIE & ZUKUNFT

```
DU bist ein Technology Strategist & Innovation Scout mit 20 Jahren FinTech-Expertise.
Deine Aufgabe: Identifiziere die 6 wichtigsten Innovationen, neuen Technologien & aufstrebenden Player.

FOKUS HEUTE — INNOVATION & TECH:
Die 6 News sollten beantworten:
- Wer baut die Zukunft des Bankings? Welche Startups sind relevant?
- Welche neuen Technologien entstehen (AI, Blockchain, etc.)?
- Welche Fintech-Partnerschaften entstehen gerade?
- Welche Tech-Giants betreten das Banking?
- Welche neuen Standards entstehen (Open Banking, APIs, etc.)?
- Was wird in 2 Jahren der Standard sein?

GEOGRAPHISCHER FOKUS:
Priorisierung: Global Innovation Hubs (40%) → USA (30%) → EU (20%) → APAC Startups (10%)
[Grund: Innovationen entstehen global]

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. TechCrunch — Fintech Startups & Funding
2. Gartner Magic Quadrant / Wave — Tech Rankings & Trends
3. The Block — Blockchain & Crypto News
4. Forrester Wave — Fintech Evaluation & Trends
5. CB Insights — Fintech Trends & Intelligence
6. Stanford AI Index — AI Trends Report
7. MIT Media Lab — Emerging Tech Research
8. Crunchbase — Funding News & Startup Tracking

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
9–42. Alle weiteren Quellen aus Datei 02 (Quellen-Matrix), Freitag-Abschnitt: AngelList (startups), e27 (Asia fintech), Fintech Magazine, Forbes (technology), Wired (technology), MIT Technology Review, Harvard Business Review (tech), McKinsey Technology, BCG Technology, Accenture Technology, Deloitte Tech Trends, EY Technology, KPMG Tech Innovation, Gartner (additional), IDC Technology, Forrester (additional), InfoQ (tech architecture), O'Reilly (tech learning), Stack Overflow (developer trends), GitHub Trends, ArXiv (AI research), ACM Digital Library (research), Stanford HAI (AI), MIT Media Lab, Berkeley AI Research Lab, CMU AI Centre, Oxford Internet Institute, Cambridge Centre for Risk, World Economic Forum (tech), Brookings Institution (tech), RAND Corporation (tech), Atlantic Council (fintech), Open Banking Implementation Entity, SWIFT Innovation Reports

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN (gelten an JEDEM Tag, unabhängig vom Fokus):**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

→ Siehe Datei 02 (Quellen-Matrix), Abschnitt „TÄGLICHE KERNQUELLEN". Diese 20 kommen zur Tagesliste HINZU, sie ersetzen sie nicht.
→ Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen heute.**

**Ergebnis:** Du recherchierst täglich in 60+ Top-Quellen parallel. 45 auf Seite 5 sind die Untergrenze, nach oben offen!

NACHRICHTENTYP:
- Startup Funding & Unicorn News
- Technology Release Announcements
- Fintech-Bank Partnerships
- Academic Breakthroughs (AI, Blockchain, etc.)
- Innovation Trend Reports
- Patent Trends & Tech Innovations

KONKRETE SUCHFRAGEN:
- "Fintech startups funding 2026"
- "AI in banking breakthroughs"
- "Open banking API developments"
- "Blockchain banking use cases 2026"
- "Fintech unicorns banking partnerships"
- "Quantum computing finance implications"
- "Cloud banking infrastructure trends"

ERGEBNIS-FORMAT:
Für jede der 6 News:
- **Titel** (5 Worte max, zukunftsorientiert)
- **Innovation/Technologie** (1–2 Sätze: Was ist neu? Warum ist das wichtig?)
- **Implikation für Banken** (konkret: "Das wird zum Standard weil...")
- **Action Points für Beratungshäuser** (3 Tätigkeiten: z.B. "Technology Assessment durchführen", "Innovation Roadmap schreiben", "Partnership-Strategie entwickeln")
- **Quellenangabe** (Quelle, Monat 2026, Jahr)

QUALITÄTS-CHECKS:
✅ Jede News ist eine echte Innovation (nicht: "New app released")
✅ Technologien sind für Banking relevant (nicht: random tech)
✅ Startups sind real & gut finanziert (nicht: Zwei-Personen-Garage)
✅ Innovations-Implikation ist klar
✅ Grundschüler-Level verständlich
✅ Alle 6 sind unterschiedliche Technologien/Player (MECE)
```

---

## SAMSTAG — KUNDENPERSPEKTIVE, RETAIL & EXPERIENCE

```
DU bist ein Customer Experience Director & Retail Banking Expert mit 15 Jahren Kundenfokus.
Deine Aufgabe: Identifiziere die 6 wichtigsten Erkenntnisse über Kundenbedürfnisse, Verhalten & Erwartungen.

FOKUS HEUTE — KUNDENPERSPEKTIVE & EXPERIENCE:
Die 6 News sollten beantworten:
- Wie ändern sich Kundenbedürfnisse & -erwartungen?
- Welche neuen Customer Experience Modelle funktionieren?
- Wie banken sich Gen Z & Millennials? Was wollen sie?
- Welche Retail-Banken gewinnen Kunden dazu?
- Wie nutzen Kunden Zahlungen & Services heute?
- Welche Omnichannel-Strategien funktionieren?

GEOGRAPHISCHER FOKUS:
Priorisierung: Deutschland (40%) → Rest EU (40%) → USA (15%) → APAC (5%)
[Grund: Customer Behavior ist lokal]

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. Capgemini World Retail Banking Report
2. Accenture Consumer Banking Study
3. Morning Consult — Consumer Research Data
4. Statista Banking Data & Statistics
5. eMarketer — Digital Banking Adoption
6. Financial Times — Consumer Banking Section
7. Harris Insights & Analytics

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
8–42. Alle weiteren Quellen aus Datei 02 (Quellen-Matrix), Samstag-Abschnitt: Bloomberg (consumer), Reuters Consumer, Handelsblatt (Verbraucher), Wirtschaftswoche (Consumer), McKinsey Consumer Insights, BCG Consumer Study, Bain Consumer Research, Accenture Consumer (additional), Deloitte Consumer, EY Consumer Research, KPMG Consumer, Forrester Consumer, Gartner Consumer, IDC Consumer Research, eMarketer (additional), Pew Research Center, Pew Internet & Technology, Gallup Surveys, Nielsen Consumer Data, comScore Digital, Comscore Banking, Forrester Digital, J.D. Power Studies, American Customer Satisfaction Index, Net Promoter Institute, Forrester Customer Experience, McKinsey Customer Experience, Harvard Business Review (CX), Stanford Business (CX), Customer Experience Professionals Association, Forrester Voice of Customer, UserTesting Insights, SurveyMonkey Research, Qualtrics Research, Statista Consumer

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN (gelten an JEDEM Tag, unabhängig vom Fokus):**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

→ Siehe Datei 02 (Quellen-Matrix), Abschnitt „TÄGLICHE KERNQUELLEN". Diese 20 kommen zur Tagesliste HINZU, sie ersetzen sie nicht.
→ Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen heute.**

**Ergebnis:** Du recherchierst täglich in 60+ Top-Quellen parallel. 45 auf Seite 5 sind die Untergrenze, nach oben offen!

NACHRICHTENTYP:
- Consumer Research Reports & Studies
- Customer Behavior Analysis
- Digital Adoption Trends
- Retail Banking Case Studies
- Customer Experience Innovation News
- Payment & Service Usage Trends

KONKRETE SUCHFRAGEN:
- "Customer expectations banking 2026"
- "Gen Z banking behavior"
- "Digital banking adoption rates 2026"
- "Omnichannel retail banking strategies"
- "Customer experience banking trends"
- "Mobile banking usage Europe"
- "Open banking customer adoption"

ERGEBNIS-FORMAT:
Für jede der 6 News:
- **Titel** (5 Worte max, kundenfokussiert)
- **Kundenbedürfnis/Verhalten** (1–2 Sätze: Was wollen Kunden? Wie verhalten sie sich?)
- **Implikation für Banken** (konkret: "Das bedeutet Banken müssen XYZ anpassen")
- **Action Points für Beratungshäuser** (3 Tätigkeiten: z.B. "CX-Assessment durchführen", "Omnichannel-Strategie entwickeln", "Digital Roadmap schreiben")
- **Quellenangabe** (Quelle, Monat 2026, Jahr)

QUALITÄTS-CHECKS:
✅ Jede News basiert auf echter Kundenforschung (nicht Spekulation)
✅ Kundenbedürfnisse sind konkret & datengestützt
✅ Implikationen für Banken sind klar
✅ Beratungs-Hebel sind kundenorientiert
✅ Grundschüler-Level verständlich
✅ Alle 6 sind unterschiedliche Customer Segments/Needs (MECE)
```

---

## SONNTAG — PEOPLE, ORGANIZATION & CULTURE

```
DU bist ein Chief Human Resources Officer & Organization Designer mit 20 Jahren Banking-HR.
Deine Aufgabe: Identifiziere die 6 wichtigsten Entwicklungen in Talent, Organization & Culture.

FOKUS HEUTE — PEOPLE & ORGANISATION:
Die 6 News sollten beantworten:
- Wo können Banken nicht rekrutieren? Welche Skill Gaps gibt es?
- Wie organisieren sich zukunftsfähige Banken neu?
- Welche Culture & Engagement Trends gibt es?
- Wie arbeiten Banker heute (Remote/Hybrid)?
- Wer führt Banken? Diversity & Leadership Trends?
- Welche Skills werden zum Standard (Upskilling)?

GEOGRAPHISCHER FOKUS:
Priorisierung: Deutschland (35%) → EU (40%) → Global (20%) → USA (5%)

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. LinkedIn Talent Solutions Blog
2. CIPD (Chartered Institute Personnel Development) — HR Research
3. Mercer Talent Reports
4. Great Place to Work Rankings
5. Korn Ferry — Leadership & Executive Search
6. Financial Times — Careers & Leadership Section
7. Harvard Business School — Case Studies & Research
8. Gartner HR Insights

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
9–42. Alle weiteren Quellen aus Datei 02 (Quellen-Matrix), Sonntag-Abschnitt: Reuters Careers, Handelsblatt (Karriere), Wirtschaftswoche (HR), McKinsey People & Org, BCG Organizational, Bain Organization, Accenture Talent, Deloitte People, EY People & Culture, KPMG People Strategy, Gartner HR Research, Forrester HR, IDC HR Tech, Society for Human Resource Management (SHRM), CIPD (additional), People Analytics Institute, Conference Board (HR), Gartner Learning, LinkedIn Learning Research, Udacity Insights, Coursera Impact, Harvard Kennedy School (leadership), Stanford Graduate School (business), MIT Sloan (organization), Wharton School (management), INSEAD (leadership), IMD (leadership), London Business School, Oxford Saïd Business, Harvard Law Forum (governance), Yale School of Management, Northwestern Kellogg, Great Place to Work (additional), Employee Benefit Research Institute

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN (gelten an JEDEM Tag, unabhängig vom Fokus):**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

→ Siehe Datei 02 (Quellen-Matrix), Abschnitt „TÄGLICHE KERNQUELLEN". Diese 20 kommen zur Tagesliste HINZU, sie ersetzen sie nicht.
→ Rechnung: **20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen heute.**

**Ergebnis:** Du recherchierst täglich in 60+ Top-Quellen parallel. 45 auf Seite 5 sind die Untergrenze, nach oben offen!

NACHRICHTENTYP:
- HR & Recruitment Trends
- Organizational Design Reports
- Leadership & Culture Studies
- Skills Gap Analysis
- Compensation & Benefits Trends
- Employee Engagement Research
- Executive Leadership News

KONKRETE SUCHFRAGEN:
- "Banking talent shortage 2026"
- "Skills gap in banking technology"
- "Organizational redesign European banks"
- "Banking culture and engagement trends"
- "Remote work in financial services"
- "Leadership diversity in banking"
- "Upskilling programs banking industry"

ERGEBNIS-FORMAT:
Für jede der 6 News:
- **Titel** (5 Worte max, talentfokussiert)
- **People/Organization Trend** (1–2 Sätze: Welcher Trend ist zu sehen?)
- **Implikation für Banken** (konkret: "Das bedeutet Banken müssen ihre Org anders aufbauen")
- **Action Points für Beratungshäuser** (3 Tätigkeiten: z.B. "Organization Assessment durchführen", "Change Management Programm entwerfen", "Talent Acquisition Strategie schreiben")
- **Quellenangabe** (Quelle, Monat 2026, Jahr)

QUALITÄTS-CHECKS:
✅ Jede News basiert auf echter HR/Org-Forschung
✅ Talent Gaps & Organization Shifts sind konkret & datengestützt
✅ Implikationen sind klar
✅ Beratungs-Hebel sind HR/Org-fokussiert
✅ Grundschüler-Level verständlich
✅ Alle 6 sind unterschiedliche People/Org Themen (MECE)
```

---

## IMPLEMENTIERUNG

Jeder Tag folgt seinem einzigartigen Prompt. Die Prompts sind:
- **Spezifisch** für den Wochentag
- **Unterschiedliche Perspektive** (nicht jeden Tag gleich)
- **Unterschiedliche Quellen-Priorisierung** (nicht täglich McKinsey + FT)
- **Unterschiedliche Nachrichtentypen** (nicht immer Top-6-Breaking-News)
- **Unterschiedliche Suchfragen** (konkret & fokussiert pro Tag)

**Ergebnis:** Ein Newsletter, der täglich unterschiedliche, breite und interessante Nachrichtenlagen liefert — nicht täglich das gleiche!
# Implementierungs-Leitfaden — Wie die Gerüste zusammenhängen

> **Zweck:** Dieses Dokument zeigt, wie die drei Gerüste (Wochenstruktur, Quellen-Matrix, Master-Prompt) TÄGLICH zusammenspielen. Es ist die operative Anleitung.

---

## ÜBERBLICK: DIE TÄGLICH NEUE RECHERCHELOGIK

**Statt:** Jeden Tag den gleichen Prompt verwenden → gleiche News → gleicher Newsletter  
**Neu:** Jeden Tag einen neuen, fokussierten Prompt → unterschiedliche News → breiter Newsletter

**Die Zutaten:**
1. **Wochenstruktur (Datei 01)** → Sagt, welcher Fokus heute ist
2. **Quellen-Matrix (Datei 02)** → Sagt, welche Quellen heute nutzen
3. **Master-Prompt (Datei 03)** → Sagt, wie man mit Fokus + Quellen recherchiert
4. **Implementierungs-Leitfaden (DIESE Datei)** → Zeigt, wie es zusammenspielt

---

## TÄGLICHER WORKFLOW — SCHRITT FÜR SCHRITT

### Schritt 0: Welcher Wochentag ist heute?

Prüfe: Heute ist **[Wochentag]**

→ Gehe zu **01_Wochenstruktur_Fokus-Themenfelder.md**, Abschnitt **[Wochentag]**

Notiere:
- Primärer Fokus (z.B. Mo = Strategische Trends)
- Sekundäre Fokus-Themenfelder (2–3 Nebenbereiche)
- Perspektive des Tages (z.B. Top-Down, Bottom-Up, etc.)
- Beratungs-Hebel des Tages (z.B. Strategy & Transformation)

### Schritt 1: Alle 45+ Quellen für heute auswählen

Öffne **02_Quellen-Matrix_Aktuell_und_Erweiterung.md**, Abschnitt "NUTZUNGSLOGIK NACH WOCHENTAG — 45+ QUELLEN TÄGLICH"

Finde den Eintrag für heute.

**Beispiel Montag:**
```
MONTAG — 45+ QUELLEN TÄGLICH:

Priorisiert (check diese ZUERST):
1. McKinsey Global Institute
2. BCG Industry Report
3. Strategy& / PwC Thinking
4. Financial Times (global trends)
5. Oliver Wyman (strategy)
6. World Economic Forum (global trends)

Danach auch (parallel recherchieren):
7–42. Bain & Company, Accenture, Deloitte, EY, KPMG, Roland Berger, 
Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, WSJ, Brookings, 
Gartner, Forrester, IDC, Oliver Wyman (zusätzlich), Opimas, 
Goldman Sachs, A.T. Kearney, BCG (zusätzlich), Harvard Business Review, 
Stanford, LSE Banking Centre, SSRN Finance, Global Financial Innovation 
Network, Europarlament, ECB, EBA, BIZ, IIF, World Bank, IMF, Politico, 
FCA, Federal Reserve, Regulatory Intelligence, + weitere Top-Quellen
```

**Das bedeutet:** Du recherchierst täglich in **ALLEN 45+ Quellen parallel**, nicht nur in 6–8!
- **Priorisierte Quellen (1–6):** Check diese ZUERST, vielleicht am ausführlichsten
- **Danach (7–42):** Scan auch alle anderen 45+ Quellen
- **Die besten 6 News** werden aus den Findings aller 45+ Quellen selektiert

### Schritt 2: Den täglichen Recherche-Prompt adaptieren

Öffne **03_Master_Recherche_Prompt_Template.md**, Abschnitt **[Wochentag]**

Kopiere den **kompletten Prompt** für heute.

Der Prompt ist bereits an den Wochentag angepasst — du veränderst ihn **minimal**:
- Ersetze `2026` mit aktuellem Jahr (falls nötig)
- Ersetze `Q2 2026` mit aktuellem Quartal
- Ersetze `Diese Woche` mit aktuellem Datumsbereich
- Sonst: Prompt bleibt wie geschrieben

**Beispiel (Montag, angepasst):**
```
[... komplett wie in 03_Master_Recherche_Prompt_Template.md, aber mit heutigem Datum ...]

QUELLEN — RECHERCHIERE IN 45+ QUELLEN TÄGLICH (NICHT NUR 6–8!):

**Priorisiert (check diese ZUERST):**
1. McKinsey Global Institute (letzte 2 Wochen)
2. BCG — Industry Reports & Perspectives (Banking)
3. Strategy& (PwC) — Banking Thinking
[... Position 4 bis 6 wie dort ...]

**Danach AUCH (parallel recherchieren — ALLE gehören dazu):**
7–42. Alle weiteren Quellen aus Datei 02, Montag-Abschnitt

**IMMER ZUSÄTZLICH — DIE 20 TÄGLICHEN KERNQUELLEN:**
McKinsey, BCG, Bain, PwC/Strategy&, Deloitte, EY, KPMG, Roland Berger,
Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt,
Wirtschaftswoche, WSJ, EZB/ECB, BaFin, EBA, Deutsche Bundesbank

KONKRETE SUCHFRAGEN:
- "Top banking trends August 2026"
[... updated mit aktuellem Datum ...]
```

⚠️ **Achtung — dieser Kopf ist Pflicht.** Steht im Tagesprompt nur `QUELLEN — NUTZE VOR ALLEM:` mit einer kurzen Liste von sechs bis acht Quellen, ist der Prompt **defekt**. Genau dieser Defekt führte am Mittwoch, 12.08.2026 zu nur 27 statt 45 Quellen. In dem Fall die vollständige Tagesliste aus Datei 02 verwenden.

### Schritt 3: Recherche in 45+ Quellen durchführen

Nutze den angepassten Prompt. **Die Recherche wird täglich völlig unterschiedlich**:

- **Montag:** Recherchiere in 45+ Quellen zur Strategie (McKinsey, BCG, FT, Oliver Wyman, usw. bis Regulatory Intelligence) → Selektiere die besten 6 strategischen Trends
- **Dienstag:** Recherchiere in 45+ Quellen zu Operationen (FT, Bloomberg, Handelsblatt, Accenture, usw. bis Cambridge Centre) → Selektiere die besten 6 operativen Probleme
- **Mittwoch:** Recherchiere in 45+ Quellen zu Regulierung (ECB, EBA, BaFin, EU, usw. bis EY Regulatory) → Selektiere die besten 6 Anforderungen
- **Donnerstag:** Recherchiere in 45+ Quellen zu Märkten (Bloomberg, Reuters, Goldman Sachs, usw. bis BIS Bulletin) → Selektiere die besten 6 M&A/Market News
- **Freitag:** Recherchiere in 45+ Quellen zu Innovation (TechCrunch, Gartner, The Block, usw. bis SWIFT Innovation) → Selektiere die besten 6 Technologien
- **Samstag:** Recherchiere in 45+ Quellen zu Kunden (Capgemini, Accenture, Statista, usw. bis Statista Consumer) → Selektiere die besten 6 Customer Insights
- **Sonntag:** Recherchiere in 45+ Quellen zu People/Org (LinkedIn, CIPD, Mercer, usw. bis Employee Benefit Research) → Selektiere die besten 6 Talent/Org News

**WICHTIG:** Du checkst ALLE 45+ Quellen, nicht nur 6–8!  
**Ergebnis:** 6 News pro Tag, aber aus **45+ Quellen täglich selektiert**, nicht aus nur 6–8!  
Das erzeugt eine **viel breiter fundierte, bessere, vielfältigere Nachrichtenauswahl**!

### Schritt 4: News strukturieren (COVER PAGE — SEITE 1)

Jede der 6 News auf der Cover Page (Seite 1) muss folgende STANDARDISIERTE Struktur haben:
```
[Nummer-Badge 01–06]
KATEGORIE (1–3 Wörter, Großbuchstaben)
Headline (max. 5 Wörter, max. 2 Zeilen)

Kontext: [2–3 vollständige Sätze, 200–320 Zeichen, Grundschüler-Level]

BEDEUTUNG FÜR BERATUNGSDIENSTLEISTUNG:
– [Konkrete Tätigkeit 1 — 60–110 Zeichen, vollständiger Satz]
– [Konkrete Tätigkeit 2 — 60–110 Zeichen, vollständiger Satz]
– [Konkrete Tätigkeit 3 — 60–110 Zeichen, vollständiger Satz]

(Quelle, Jahr)
```

⚠️ **DIE ZEICHENGRENZEN SIND PFLICHT.** Das Cover hat **3 schmale Spalten × 2 Reihen** (je ca. 155 pt breit). Längerer Text sprengt das Raster und erzwingt ein falsches 2-Spalten-Layout. **Text kürzen, niemals das Raster ändern.**

⚠️ **WICHTIG — NUR SEITE 1!**
- **"Bedeutung für Beratungsdienstleistung:" ist STANDARDISIERT auf der Cover Page** — immer dieser Begriff!
- Diese Wording ist **NUR auf Seite 1 (Cover Page)**
- Auf Seiten 2–4 wird NUR "Problem" + "Beratungsdienstleistung" ohne diese Überschrift verwendet
- Der Fokus pro Tag ist unterschiedlich (Mo: Strategisch, Di: Problem, Mi: Compliance, Do: Finanz, Fr: Innovation, Sa: Customer, So: People), aber die Wording "Bedeutung für Beratungsdienstleistung:" bleibt IDENTISCH

### Schritt 5: Qualitätsprüfung

Prüfe für jede News:
- ✅ Passt zum **Fokus des Tages**? (z.B. Mo: Strategisch? Di: Operativ?)
- ✅ **Keine Wiederholung von gestrigen Themen?**
- ✅ **6 unterschiedliche Themen** (MECE)?
- ✅ Grundschüler-Level verständlich?
- ✅ Action Points sind konkret (nicht abstrakt)?
- ✅ **Zeichengrenzen eingehalten** (Kontext 200–320, je Punkt 60–110)?

**Und dann die zwei harten Zählprüfungen:**
- 🔴 **Sind es mindestens 45 Quellen auf Seite 5?** Gezählt, nicht geschätzt. Bei weniger → zurück zu Schritt 3 und weitere Quellen aus der Tagesliste (42 Stück) auswerten.
- 🔴 **Ist jede der 5 Seiten randvoll?** Jede Seite ansehen. Sichtbarer Leerraum unten = Seite nicht fertig → weitere Blöcke ergänzen.

### Schritt 6: Newsletter zusammenbauen

Die 6 News bilden **Seite 1 (Cover Page)** des Newsletters.

Seiten 2–4 folgen der **Fokus-Perspektive des Tages** (s. Tabelle am Ende von Datei 01).

---

## BESONDERHEITEN PRO WOCHENTAG

### MONTAG — Breite strategische Sicht
```
Quellen-Mix: McKinsey + BCG + Strategy& + FT Global
Nachrichtentyp: Research Reports, Executive Statements, Think-Tank
Perspektive: Top-Down, C-Suite-Level
Ergebnis: 6 Trends, die langfristig die Industrie bewegen
```

### DIENSTAG — Operative Tiefe
```
Quellen-Mix: FT Business + Bloomberg + Handelsblatt + Reuters
Nachrichtentyp: Case Studies, Interviews, Operational Data
Perspektive: Bottom-Up, Teams, Alltag
Ergebnis: 6 reale operative Herausforderungen
```

### MITTWOCH — Regulatorische Genauigkeit
```
Quellen-Mix: ECB + EBA + BaFin + EU + Politico
Nachrichtentyp: Offizielle Richtlinien, Compliance Updates
Perspektive: Risk & Compliance Officer
Ergebnis: 6 neue Anforderungen, die Banken beachten müssen
```

### DONNERSTAG — Finanzielle Klarheit
```
Quellen-Mix: Bloomberg + Reuters + Goldman Sachs + Dealogic + Opimas
Nachrichtentyp: M&A News, Quarterly Data, Market Analysis
Perspektive: Investor & CFO
Ergebnis: 6 Geschäftsmodell-Shifts und Markt-Moves
```

### FREITAG — Zukunftsblick
```
Quellen-Mix: TechCrunch + Gartner + CB Insights + The Block + Stanford
Nachrichtentyp: Startup Funding, Tech Breakthroughs, Trends
Perspektive: Innovation Officer, Forward-Looking
Ergebnis: 6 neue Technologien/Player, die Standard werden
```

### SAMSTAG — Kundenzentriert
```
Quellen-Mix: Capgemini + Accenture + Statista + Morning Consult
Nachrichtentyp: Consumer Research, CX Case Studies, Behavior Data
Perspektive: Customer-Centric, User View
Ergebnis: 6 Customer Insights, die Banken verstehen müssen
```

### SONNTAG — People-fokussiert
```
Quellen-Mix: LinkedIn + CIPD + Mercer + Great Place to Work
Nachrichtentyp: HR Research, Leadership News, Culture Studies
Perspektive: CHRO, Organizational Design
Ergebnis: 6 Talent/Org Trends, die die Industrie verändern
```

---

## WOCHENRHYTHMUS — WAS IST DAS RESULTAT?

**Eine Woche sieht so aus:**

| Tag | Fokus | Perspektive | 6 News-Typen | Beratungs-Hebel |
| --- | --- | --- | --- | --- |
| **Mo** | Strategische Trends | Top-Down, Executive | Mega-Trends, Partnerschaften, M&A-Strategie | Strategy & Vision |
| **Di** | Operative Probleme | Bottom-Up, Alltag | Projekt-Scheitern, Effizienzprobleme, Talent-Lücken | Operations & Modernization |
| **Mi** | Regulierung & Governance | Risk & Compliance | Neue Guidelines, Compliance-Anforderungen, Cyber-Standards | Risk & Governance |
| **Do** | Märkte & Finanzen | Investor & CFO | M&A-Deals, Profitabilität, Geschäftsmodell-Shifts | Business Model & M&A |
| **Fr** | Innovation & Tech | Forward-Looking | Startups, AI, Blockchain, neue Standards | Digital Innovation |
| **Sa** | Kundenperspektive | Customer-Centric | Customer Behavior, CX-Trends, Omnichannel | Customer Experience |
| **So** | People & Organisation | CHRO, HR | Talent Gaps, Org-Design, Culture Trends | Organization & Talent |

**Effekt über eine Woche:**
- **Unterschiedliche Nachrichten:** Jeder Tag ein neues Themenfeld
- **Breiter Überblick:** Die ganze Industrie wird abgedeckt
- **Unterschiedliche Perspektiven:** Executive / Operativ / Risk / Investor / Innovation / Customer / HR
- **Unterschiedliche Quellen:** Nicht täglich die gleichen Anbieter
- **Interessanter für Reader:** Nicht täglich ähnliche Struktur
- **Actionable für Berater:** Jeder Tag hat seinen Beratungs-Fokus

---

## QUELLEN-DURCHMISCHUNG — KONKRETE BEISPIELE

### Woche 1 — Quellen-Fokus

**Montag:** McKinsey + BCG + Strategy& + FT + Oliver Wyman + WEF  
**Dienstag:** FT + Bloomberg + Handelsblatt + Accenture + Reuters + Capgemini  
**Mittwoch:** ECB + EBA + BaFin + EU + BIZ + Politico + CSA  
**Donnerstag:** Bloomberg + Reuters + Goldman Sachs + Dealogic + Euromoney + Mastercard  
**Freitag:** TechCrunch + Gartner + CB Insights + The Block + Stanford + Crunchbase  
**Samstag:** Capgemini + Accenture + Statista + Morning Consult + eMarketer + Harris  
**Sonntag:** LinkedIn + CIPD + Mercer + Great Place to Work + Korn Ferry + Harvard  

→ **Resultat:** Woche 1 nutzt 45+ unterschiedliche Quellen, niemals zweimal die gleiche Kombination

### Woche 2 — Quellen-Fokus (leicht anders)

**Montag:** BCG + Strategy& + WEF + McKinsey Global Institute + Oliver Wyman  
(Kleine Verschiebung: Focus auf BCG statt McKinsey, WEF statt FT)

**Dienstag:** Bloomberg + Reuters + Accenture + Financial Times + Capgemini  
(Kleine Verschiebung: Focus auf Accenture statt Handelsblatt)

**Mittwoch:** ECB + EBA + Politico + BaFin + BIZ + Regulatory Intelligence  
(Kleine Verschiebung: stärker auf Regulatory Intelligence, weniger Politico)

Etc.

→ **Resultat:** Quellen rotieren, aber thematischer Fokus pro Tag bleibt konsistent

---

## INTEGRATION MIT STRUKTUR.MD & MAIL DESIGN.MD

Diese Gerüste (01–04) **ersetzen nicht** die bestehenden MD-Dateien.

Sie **informieren und steuern** die tägliche Recherche:

```
Daily Routine (Claude Routine) →
  Liest Wochentag aus →
  Wählt Fokus aus (Datei 01) →
  Wählt Quellen aus (Datei 02) →
  Adaptiert Prompt (Datei 03) →
  Führt Recherche durch →
  Erstellt 6 News →
  Baut Newsletter nach Struktur.md →
  Erstellt Mail nach Mail Design.md
```

Das heißt:
- **Struktur.md** bleibt wie es ist (Design, Seiten-Aufbau, Checklisten, etc.)
- **Mail Design.md** bleibt wie es ist (Mail-Format, Versand, Checklisten, etc.)
- **NEUE Gerüste** (01–04) steuern nur die **Inhaltliche Recherche & Auswahl**

---

## ERSTE WOCHE — KONKRETE ANWENDUNG

**Montag, 12.08.2026:**
- Wochenstruktur: Strategische Trends
- Quellen: McKinsey, BCG, Strategy&, FT, Oliver Wyman, WEF
- Prompt: Master-Prompt Montag, angepasst auf 12.08.2026
- Recherche: Top Banking Trends August 2026
- Resultat: 6 strategische News (nicht operative, nicht regulatorisch)
- Newsletter: Seite 1 Cover mit 6 strategischen Trends + Seiten 2–4 "Wohin die Industrie geht"

**Dienstag, 13.08.2026:**
- Wochenstruktur: Operative Realität
- Quellen: FT, Bloomberg, Handelsblatt, Accenture, Reuters, Capgemini
- Prompt: Master-Prompt Dienstag, angepasst auf 13.08.2026
- Recherche: Banking Project Reality, Operational Challenges
- Resultat: 6 operative Probleme (nicht strategisch, nicht regulatorisch)
- Newsletter: Seite 1 Cover mit 6 operativen Problemen + Seiten 2–4 "Wie die Industrie wirklich kämpft"

Etc.

**Resultat nach einer Woche:**
- 7 unterschiedliche Newsletter
- Jeder Tag eine andere Perspektive
- 7 × 6 = 42 News aus unterschiedlichen Quellen
- Leser hat breites Bild über ganze Industrie
- Beratungs-Hebel sind täglich unterschiedlich
- **Newsletter ist nicht mehr "täglich ähnlich" — er ist täglich unterschiedlich!**

---

## HÄUFIGE FRAGEN

**Q: Ändert sich die Seiten-Struktur von Struktur.md?**  
A: Nein. Seiten-Layout, Design, Checklisten bleiben gleich. Nur die **Inhaltsauswahl** wird durch die Wochenstruktur gelenkt.

**Q: Muss ich alle 45+ Quellen täglich checken?**  
A: Nein. Du nutzt täglich **6–8 priorisierte Quellen** (s. Abschnitt "NUTZUNGSLOGIK NACH WOCHENTAG"). Die restlichen sind Backup/Auswahl.

**Q: Was ist, wenn am Montag keine strategischen Trends da sind?**  
A: Dann nimm die besten verfügbaren strategischen News. Du recherchierst mit Fokus, aber nicht dogmatisch — wenn es heute keine perfekten Strategie-News gibt, nimm gute verfügbare.

**Q: Wie lange dauert eine Recherche mit diesem System?**  
A: Ähnlich wie heute — etwa 2–3 Stunden. Der Prompt ist fokussiert, die Quellen sind klar, es geht schneller.

**Q: Wird der Newsletter zu vielfältig? Verlieren wir den roten Faden?**  
A: Nein. Der rote Faden ist "Financial Services Consulting Newsletter" — jeden Tag aus einer anderen Perspektive. Das ist **Qualität & Breite**, nicht Chaos.

---

## SUMMARY

Diese 4 Gerüst-Dateien schaffen:

1. ✅ **Wochenstruktur (Mo–So mit unterschiedlichen Fokus-Themenfeldern)**
2. ✅ **Quellen-Rotation (täglich unterschiedliche Quellen, gleich hohe Qualität)**
3. ✅ **Master-Prompt-System (täglich ein anderer, fokussierter Recherche-Prompt)**
4. ✅ **Operativer Leitfaden (Schritt-für-Schritt, wie es zusammenspielt)**

**Resultat:** Ein Newsletter, der täglich unterschiedlich, interessant, breit und beratungsorientiert ist — nicht täglich das gleiche!

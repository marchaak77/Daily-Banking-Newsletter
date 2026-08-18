# Financial Services Consulting Newsletter — Tägliche Erstellungs-Routine

> **Zweck dieser Datei:** Standardisierte Arbeitsanweisung für die tägliche Erstellung des Newsletters. Diese Datei wird bei jedem Lauf vollständig gelesen und befolgt. Es darf keine der hier genannten Anforderungen ausgelassen werden.

---

## 0. Welche Datei regelt was (MECE)

Jede Anweisung hat **genau eine** zuständige Datei. Wer etwas ändern will, ändert es dort — und nur dort.

| Bereich | Zuständige Datei (Quelle der Wahrheit) |
| --- | --- |
| **Ablauf, Inhalt, Sprache, Design, Speichern** | **Diese Datei** (`Banking Newsletter/Struktur/Struktur.md`) |
| **Aufbau und Text der Versand-Mail** | `Banking Newsletter/Mail Design/Mail Design.md` |
| **Themenfeld je Wochentag (Details)** | `Banking Newsletter/Recherche-Gerüst/01_Wochenstruktur_Fokus-Themenfelder.md` |
| **Quellenlisten je Wochentag und die 20 Kernquellen** | `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix_Aktuell_und_Erweiterung.md` |
| **Recherche-Prompts je Wochentag** | `Banking Newsletter/Recherche-Gerüst/03_Master_Recherche_Prompt_Template.md` |
| **Operativer Tagesworkflow Schritt für Schritt** | `Banking Newsletter/Recherche-Gerüst/04_Implementierungs-Leitfaden.md` |
| **Maschinelle Endprüfung der fertigen PDF** | `Banking Newsletter/Struktur/qualitaetspruefung.py` |
| **Design-Layout (Raster, Farben, Maße)** | `Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf` — nur Layout, keine Inhaltsregeln (Abschnitt 12.1) |
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
1. **Recherchieren** — täglich 45+ Top-Quellen durchsuchen (Abschnitt 6, `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix`, Wochentag-Fokus aus `Banking Newsletter/Recherche-Gerüst/01_Wochenstruktur`)
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

⚠️ **DIE LÄNGENVORGABEN SIND PFLICHT.** Die Vorlage hat drei schmale Spalten mit den Textkanten x **45.3 / 222.8 / 391.0** (Spaltenabstand 177.5 bzw. 168.2 pt, nutzbare Textbreite je rund 155 pt). Längerer Text sprengt das Raster und zwingt zu einem falschen 2-Spalten-Layout. **Kürze den Text, nicht das Raster.**

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
| **Seite 2** | **Kernaussage-Box mit 3 Punkten** (nur auf dieser Seite!). Spaltenüberschriften `NACHRICHTENLAGE` links und `BEDEUTUNG FÜR DAS BANKING-CONSULTING` rechts. Links **mindestens 8 News-Blöcke** (je Kategorie + Headline + 3–5 Sätze). Rechts **mindestens 7 Beratungsblöcke** (je Balken-Überschrift + Problem + Beratungsdienstleistung). Am Ende rechts die Box `FRONTRUNNER-MESSLATTE: WO EINE BANK HEUTE STEHEN MÜSSTE` mit **mindestens 6 Punkten**. |
| **Seite 3** | **Keine Kernaussage-Box** — die Spalten beginnen direkt unter dem Seitenband. Spaltenüberschriften `NACHRICHTENLAGE` links und `BEDEUTUNG FÜR DAS BANKING-CONSULTING` rechts. Links **mindestens 8 News-Blöcke**. Rechts **mindestens 7 Beratungsblöcke**. Zusätzlich die **Gap-Tabelle mit mindestens 6 Zeilen**. |
| **Seite 4** | **Keine Kernaussage-Box.** Spaltenüberschriften **`ZAHLEN DES TAGES`** links (nicht `NACHRICHTENLAGE`) und `BEDEUTUNG FÜR DAS BANKING-CONSULTING` rechts. Links **mindestens 8 Zahlen-Blöcke** (jeder mit Zahl, Einheit, Jahr, Begründung). Rechts **mindestens 7 Beratungsblöcke**. Zusätzlich **Rangliste** (mind. 5 Zeilen) und **Negativliste** (mind. 4 Zeilen). |
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

2. **Linke Spalte = blanke News mit „So What?" Erklärung** (Seiten 2–4). Die linke Spalte zeigt reine Fakten aus den Nachrichten mit klarer Erklärung, was das bedeutet. Wichtig: Das „So What?" ist ZENTRAL — jede Zahl, jedes Zitat muss erklärt werden, warum es wichtig ist. Die linke Spalte reicht von x **31.2** bis x **261.8**, Breite **230.6 pt** (38.7 % der Seite) — Wert aus Abschnitt 12.2, nicht schätzen.

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

3. **Rechte Spalte = Beratungshebel — NUR Problem + Beratungsdienstleistung, KEINE Tools!** (Seiten 2–4). Die rechte Spalte zeigt **konkrete, praktische Beratungsansätze für Beratungshäuser**. **DIGITALE TOOLS SIND HIER NICHT RELEVANT.** Die rechte Spalte reicht von x **261.8** bis x **564.0**, Breite **302.2 pt** (50.8 % der Seite) — Wert aus Abschnitt 12.2, nicht schätzen.

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
   - Sind es **weniger als 45** → **zurück in die Recherche.** Weitere Quellen aus `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix` auswerten.
   - **45 ist der Boden, nicht das Ziel. Es gibt keine Obergrenze.** 50, 60 oder 70 geprüfte Quellen sind besser als 45. Höre nicht auf, sobald 45 erreicht sind, sondern wenn der Themenfokus des Tages wirklich ausgeschöpft ist.

   **Gleichbleibend hohe Qualität an jedem Wochentag:**
   - Zusätzlich zur Tagesliste gelten **20 Kernquellen, die an jedem Tag geprüft werden** — unabhängig vom Themenfokus. Dazu zählen McKinsey, BCG, Bain, PwC, Deloitte, EY, KPMG, Roland Berger, Accenture, Oliver Wyman, Financial Times, Bloomberg, Reuters, Handelsblatt, Wirtschaftswoche, Wall Street Journal, EZB, BaFin, EBA und Deutsche Bundesbank.
   - Sie stehen in `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix` im Abschnitt „TÄGLICHE KERNQUELLEN" und **kommen zur Tagesliste hinzu**, sie ersetzen sie nicht.
   - **Rechnung: 20 Kernquellen + 42 Quellen der Tagesliste = 62 verfügbare Quellen pro Tag.**
   - Dadurch ist die Datenlage an einem Mittwoch genauso gut wie an einem Montag. Der **Fokus** wechselt täglich, die **Qualitätsbasis** nicht.

   **Qualitätsanforderungen an jede Quelle:**
   - Autor oder Organisation ist eindeutig benannt
   - Veröffentlichungsdatum ist gesetzt
   - Zahlen sind überprüfbar
   - **Mindestens 10–12 Quellen** stammen aus anderen Ländern oder internationalen Publikationen
   - **Aktualität hat Vorrang:** Quellen der letzten 24–72 Stunden werden bevorzugt

   **So kommt man verlässlich auf 45+:**
   - `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix` listet je Wochentag **42 Quellen** (Abschnitt „NUTZUNGSLOGIK NACH WOCHENTAG"). Diese Liste wird **vollständig abgearbeitet**, nicht nur die ersten sechs bis acht.
   - `Banking Newsletter/Recherche-Gerüst/03_Master_Recherche_Prompt_Template` enthält je Wochentag den passenden Prompt. Jeder dieser sieben Prompts trägt die Überschrift **„RECHERCHIERE IN 45+ QUELLEN TÄGLICH"** und listet unter **„Danach AUCH"** die Quellen bis Position 42.
   - ⚠️ **Prüfe beim Start: Trägt der Prompt des heutigen Wochentags die 45+-Überschrift und den Abschnitt „Danach AUCH"?** Wenn dort nur eine kurze Liste mit sechs bis acht Quellen steht, ist der Prompt defekt — dann die vollständige Tagesliste aus Datei 02 verwenden. Genau dieser Defekt führte am Mittwoch, 12.08.2026 zu nur 27 Quellen.
   - Jede der vier Inhaltsseiten (1–4) zieht aus diesem Pool. Bei 6 News + 3×8 Blöcken links + 3×7 Blöcken rechts entstehen dabei zwangsläufig mehr als 40 Belege.
   - **Wenn am Ende weniger als 45 Quellen dastehen, wurde zu flach recherchiert** — nicht die Zahl schönen, sondern nacharbeiten.

3. **Täglich Neues bringen, nie wiederholen.** 
   - Vor dem Schreiben: Schau die Ausgaben der **letzten 5 Tage** an (Ordner `Banking Newsletter/Output`). Welche Themen sind schon behandelt worden? Führe eine Liste dieser Themen.
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
- **Abgleich mit alten Ausgaben:** Vor dem Schreiben werden die Ausgaben der letzten 5 Tage aus dem Ordner `Banking Newsletter/Output` angeschaut, um Wiederholungen zu vermeiden und Entwicklungen weiterzuführen.

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
      `Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf`

   **Schritt 0c — Vorlage sichten**

   Öffne die gefundene Datei und **sieh dir alle 5 Seiten an**. Die exakten Maße stehen in Abschnitt 12.2. Präge dir ein: **Cover = 3 Spalten × 2 Reihen in einer weißen Karte.** Seiten 2–4 = zweizeiliger Kopf, links weiß / rechts hellblau, **jeder linke Block endet mit einer Quellenangabe**. Seite 5 = zwei Spalten Quellen.

   **Schritt 0d — 🔴 REPOSITORY AUF VOLLSTÄNDIGKEIT PRÜFEN UND FEHLENDES HOCHLADEN**

   Das Repository heißt **immer gleich** (`Daily-Banking-Newsletter`), wird aber gelegentlich **gelöscht und neu angelegt**, wenn sich Regelwerke ändern. Nach einem solchen Neuaufbau ist es **leer**. Dieser Schritt stellt die Arbeitsgrundlage selbsttätig wieder her.

   **Die Pflichtliste — diese Dateien müssen im Repository liegen:**

   | # | Datei oder Ordner | Wofür sie gebraucht wird |
   | --- | --- | --- |
   | 1 | `Banking Newsletter/Struktur/Struktur.md` | dieses Regelwerk |
   | 2 | `Banking Newsletter/Struktur/qualitaetspruefung.py` | maschinelle Endprüfung (Schritt 13b) |
   | 3 | `Banking Newsletter/Mail Design/Mail Design.md` | Aufbau der Versand-Mail |
   | 4 | `Banking Newsletter/Recherche-Gerüst/01_Wochenstruktur_Fokus-Themenfelder.md` | Themenfeld je Wochentag |
   | 5 | `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix_Aktuell_und_Erweiterung.md` | Quellenlisten und Kernquellen |
   | 6 | `Banking Newsletter/Recherche-Gerüst/03_Master_Recherche_Prompt_Template.md` | Recherche-Prompts je Tag |
   | 7 | `Banking Newsletter/Recherche-Gerüst/04_Implementierungs-Leitfaden.md` | Tagesworkflow |
   | 8 | `Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf` | **die Design-Vorlage** |
   | 9 | `Banking Newsletter/Example Design/Newsletter_Wallpaper.jpeg` | Hero-Bild der Cover Page |
   | 10 | `Banking Newsletter/Output/` | Ablage der Ausgaben und Grundlage der 5-Tage-Sperrliste |

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

   - Details zum Fokus stehen in `Banking Newsletter/Recherche-Gerüst/01_Wochenstruktur_Fokus-Themenfelder.md`.
   - Die passende Quellenliste steht in `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix`, Abschnitt „NUTZUNGSLOGIK NACH WOCHENTAG".
   - Der passende Recherche-Prompt steht in `Banking Newsletter/Recherche-Gerüst/03_Master_Recherche_Prompt_Template`.

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

   Schau in den Ordner `Banking Newsletter/Output` auf die **letzten 5 Tage** und notiere **jedes dort behandelte Thema**. Diese Liste ist die **Sperrliste** für den heutigen Lauf.

   - **🔴 Mindestens 80 % der heutigen Themen müssen neu sein.** Bei rund 30 Blöcken dürfen **höchstens 6** von der Sperrliste stammen.
   - Ein gesperrtes Thema darf nur zurückkommen, wenn es eine **echte neue Entwicklung** gibt. Dann wird **ausschließlich das Neue** berichtet.
   - Die Sperrliste wird während der Recherche (Schritte 3 bis 6) **laufend abgeglichen**, nicht erst am Ende.

   ⚠️ **Auch hier gilt die Kopplung aus Abschnitt 5, Punkt 7b:** Ein wegen der Sperrliste verworfenes Thema wird durch ein **neues ersetzt**, nicht ersatzlos gestrichen. Am Ende stehen weiterhin **45+ Quellen** und **volle Seiten**.

3. **Recherche für Seite 1 (Cover Page) — in 45+ Quellen.**

   ⚠️ **Voraussetzung:** Schritt 1c ist abgeschlossen. Datum, Wochentag und Themenfeld liegen fest. Sonst hier **nicht** beginnen.

   Nutze das in Schritt 1b bestimmte Themenfeld (Details in `Banking Newsletter/Recherche-Gerüst/01_Wochenstruktur`) und recherchiere in 45+ Top-Quellen (Tagesliste in `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix`, Prompt in `Banking Newsletter/Recherche-Gerüst/03_Master_Recherche_Prompt_Template`). Finde die 6 gewichtigsten News des Tages aus den 45+ Quellen. Diese müssen Executive-Level sein und klare Consulting-Implikationen haben.

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
    | **Kopfband-Höhe** Seiten 2–5 | **63 pt** (± 2,5) — nicht 90 |
    | **Seitenband-Ende** Seiten 2–5 | **81,8 pt** (± 2,5) |
    | **Titel-Schriftgröße** Seiten 2–5 | **12,5 pt** (± 2,5) — nicht 19 |
    | **Kernaussage-Titel** | `KERNAUSSAGE DES TAGES` auf Seite 2 vorhanden |
    | **Spaltenüberschriften** | links `NACHRICHTENLAGE` (S4: `ZAHLEN DES TAGES`), rechts `BEDEUTUNG FÜR DAS BANKING-CONSULTING` |
    | Füllung je Seite | höchstens 40 pt Leerraum (Seite 5: 80 pt) |
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
      - Ziel: Repository `Daily-Banking-Newsletter`, Ordner `Banking Newsletter/Output/`, Branch **`main`**
      - **Direkt auf `main` committen und pushen.** Kein Feature-Branch, kein Pull Request — sonst ist die öffentliche Adresse nicht erreichbar und der Mailversand scheitert.
      - Prüfen: Liefert die öffentliche Adresse Status 200 und beginnt der Inhalt mit `%PDF`? Falls NEIN → Fehler melden, **nicht** versenden.

    - **Schritt 2 — Lokale Archivkopie (nur wenn technisch möglich):**
      - Läuft der Newsletter **lokal auf dem Mac**: zusätzlich in `/Users/marchaak/Desktop/Banking Newsletter/Output/` ablegen.
      - Läuft er in der **Cloud-Routine**: Dieser Schritt entfällt ersatzlos. Das ist **kein Fehler** und **kein Grund**, den Mailversand zu stoppen. Das GitHub-Repository ist dann das Archiv.

    - **Merksatz:** GitHub `main` ist Pflicht und Voraussetzung für die Mail. Die lokale Kopie ist eine Zugabe, wenn die Umgebung sie zulässt.

15. **Mail automatisch versenden.** Folge den Anweisungen in `Banking Newsletter/Mail Design/Mail Design.md`. Nach erfolgreichem Push auf `main`:
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
- **Jede Abweichung vom Design-Muster:** Der gesamte Newsletter (Seiten 1–5) exakt nach `Banking Newsletter/Example Design/Main Example_Financial Services Consulting Newsletter.pdf`. Keine visuellen Varianten. Jeder Newsletter sieht optisch identisch aus.
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
- **🔴 Layoutmaße schätzen statt aus der Vorlage übernehmen.** Kopfband **63 pt**, Seitenband-Ende **81,8 pt**, Titel **12,5 pt** — das sind gemessene Werte, keine Richtwerte. Ein Kopfband mit 90 pt und ein Titel mit 19 pt zerstören das gesamte Seitenbild, obwohl Farben und Raster stimmen. Genau so entstand die fehlerhafte Ausgabe vom 13.08.2026.
- **Eigene Farben erfinden.** In der Ausgabe vom 13.08.2026 tauchten `#C7DCE6`, `#D8E4EA`, `#F2F8FC` und sogar ein Rot `#C0392B` auf — keine davon steht in der Palette (Abschnitt 12.3). **Nur die dort gelisteten Farben verwenden.**

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
- [ ] **🔴 LAYOUTMASSE GEGEN DIE VORLAGE GEPRÜFT** (Abschnitt 12.2) — gemessen, nicht geschätzt:
  - [ ] Kopfband Seiten 2–5 endet bei **63 pt** (nicht 90) ✓
  - [ ] Seitenband endet bei **81,8 pt** ✓
  - [ ] Titel `Financial Services / Consulting Newsletter` ist **12,5 pt**, zweizeilig (nicht 19 pt) ✓
  - [ ] Datum rechts ist **19 pt**, Untertitel in **`#AFD7EB`** ✓
  - [ ] `KERNAUSSAGE DES TAGES` steht **nur auf Seite 2** — Seiten 3 und 4 haben keine solche Box ✓
  - [ ] Spaltenüberschriften vorhanden: links `NACHRICHTENLAGE` bzw. `ZAHLEN DES TAGES` (Seite 4), rechts `BEDEUTUNG FÜR DAS BANKING-CONSULTING` ✓
  - [ ] **Keine Farbe außerhalb der Palette** aus Abschnitt 12.3 ✓
- [ ] **🔴 SPEICHERUNG — GITHUB `main` IST PFLICHT:**
  - [ ] Die PDF ist im Repository `Daily-Banking-Newsletter`, Ordner `Banking Newsletter/Output/`, **direkt auf Branch `main`** gepusht ✓
  - [ ] **Kein Feature-Branch, kein offener Pull Request** — sonst liefert die öffentliche Adresse 404 ✓
  - [ ] **DATUM-KONTROLLPUNKT:** Der Dateiname trägt das **heutige** Datum (z.B. `20260812_` für 12.08.2026, nicht `20260811_`) ✓
  - [ ] Lokale Archivkopie in `/Users/marchaak/Desktop/Banking Newsletter/Output/` — **nur wenn die Umgebung Zugriff auf den Mac hat.** In der Cloud-Routine entfällt dieser Punkt und ist **kein Fehler** ✓
- [ ] **Öffentliche Adresse geprüft:** `https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Banking%20Newsletter/Output/YYYYMMDD_Financial%20Services%20Consulting%20Newsletter.pdf` liefert Status 200 und PDF-Header (`%PDF`)
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
| Pfad im Repository | `Banking Newsletter/Output/` |
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
2. **Auf `main` pushen** (Repository `Daily-Banking-Newsletter`, Ordner `Banking Newsletter/Output/`) ✓
3. **Verifikation:** Öffentliche Adresse liefert 200 + `%PDF`? Falls nein → FEHLER, STOP ✓
4. **Lokale Kopie**, falls die Umgebung es zulässt — sonst überspringen (kein Fehler) ✓
5. Weiter zum Mailversand ✓

### 11.2 Mail automatisch versenden — nach erfolgreichem Push auf `main`

⚠️ **ES GIBT GENAU EINEN VERSANDWEG: ZAPIER.**

Kein GitHub-Actions-Workflow, kein SMTP-Skript, kein zweiter Automatismus. Ein früher vorhandener Actions-Workflow wurde entfernt, weil er andere Dateinamen erwartete (`Newsletter_JJJJ-MM-TT.pdf`) als dieses Regelwerk vorgibt (`JJJJMMTT_Financial Services Consulting Newsletter.pdf`) — dadurch wurde nie versendet. **Es gilt ausschließlich der Dateiname aus Abschnitt 11.**

Der Mailversand erfolgt **nur nach erfolgreichem Push auf `main` und bestandener URL-Prüfung**. Der Versand läuft vollautomatisch — es wird **kein Entwurf** gespeichert.

**Ablauf (strenge Reihenfolge):**

1. **Push abgeschlossen:** PDF liegt auf `main` im öffentlichen Repository und die Adresse liefert 200 + `%PDF` ✓

2. **Mail-Text erstellen** nach `Banking Newsletter/Mail Design/Mail Design.md`:
   - Betreff: `Financial Services Consulting Newsletter — Ausgabe des DD.MM.YYYY`
   - Aufbau: Hallo zusammen → 3 Rubriken à 3 Bullets → Hinweis auf PDF → Newsletter erscheint täglich → Schlusssatz → Gruß
   - Jeder Bullet: Kontext + konkrete Action Points für die Beratung (keine Tools)
   - Sprache: Menschlich, einfach, Banking-Begriffe erklärt

3. **Öffentliche Adresse der PDF abrufen und prüfen:**
   - Adresse: `https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Banking%20Newsletter/Output/YYYYMMDD_Financial%20Services%20Consulting%20Newsletter.pdf`
   - Status-Code muss 200 sein (Datei vorhanden)
   - Datei-Header muss mit `%PDF` beginnen (echte PDF, nicht HTML/Text)
   - Falls Prüfung fehlschlägt: **Nicht versenden**, Fehler melden, warten auf Korrektur

4. **Mail über Zapier versenden.** Die vollständige Feldbelegung steht in `Banking Newsletter/Mail Design/Mail Design.md`, Abschnitt 10.1. Kurzfassung:
   - Werkzeug: `execute_zapier_write_action`, `tool_name` = `gmail_send_email`
   - `from`: `marc.haak77@gmail.com`
   - `to`: `marc.haak@students.ebs.de` — **genau diese eine Adresse**
   - `cc` und `bcc`: **gar nicht übergeben** (nicht leer setzen, sondern weglassen)
   - `subject`: `Financial Services Consulting Newsletter — Ausgabe des DD.MM.YYYY` mit **heutigem** Datum
   - `body`: fertiger Mailtext als HTML, dazu `body_type`: `html`
   - `file`: die geprüfte **öffentliche URL** der PDF, kein lokaler Pfad

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

### 12.0 🔴 DAS OBERSTE DESIGN-GEBOT — 1:1, OHNE AUSNAHME

> **Jede Ausgabe muss optisch und im Aufbau exakt so aussehen wie `Main Example_Financial Services Consulting Newsletter.pdf`. Legt man beide nebeneinander, dürfen sich nur die Texte, Zahlen und das Datum unterscheiden — sonst nichts.**

Das gilt für **alle fünf Seiten, einschließlich der Cover Page**.

**Was das konkret bedeutet:**

| Bereich | Regel |
| --- | --- |
| **Maße** | Jede Position, jede Höhe, jede Breite wird aus Abschnitt 12.2 übernommen. **Kein Wert wird geschätzt, gerundet oder „ungefähr" gesetzt.** |
| **Schriftgrößen** | Exakt wie in 12.2. 12,5 pt bleibt 12,5 pt — nicht 12, nicht 13, nicht 19. |
| **Farben** | Ausschließlich die Palette aus 12.3. **Keine einzige Farbe darüber hinaus**, auch keine „ähnliche". |
| **Flächenaufbau** | Wie in der Vorlage. Cover = 3 Flächen. Nichts nachbauen, was als Bild gehört. |
| **Elemente** | Kein Element weglassen (Kernaussage-Box, Spaltenüberschriften, Trennlinien) und keines hinzufügen. |

**Die drei Fragen vor dem Speichern:**

1. **Habe ich die Vorlage offen daneben gehabt?** Nicht aus dem Gedächtnis gebaut, sondern verglichen.
2. **Stammt jeder Zahlenwert aus Abschnitt 12.2?** Oder habe ich irgendwo geschätzt?
3. **Würde ein Leser die beiden Ausgaben für dasselbe Layout halten?** Bei jeder einzelnen Seite.

⚠️ **Bei jedem Zweifel gilt die Vorlage, nicht die eigene Einschätzung.** Wenn eine Angabe in diesem Regelwerk unklar ist oder zu fehlen scheint, wird **in der Vorlage-PDF nachgemessen** — nicht geschätzt und nicht „sinnvoll ergänzt".

**Warum diese Schärfe:** Am 13.08.2026 stimmten Farben, Raster und Inhalte. Trotzdem war das Ergebnis unbrauchbar, weil das Kopfband 90 statt 63 pt hoch war, der Titel 19 statt 12,5 pt groß und der Bildverlauf aus 30 gestapelten Rechtecken nachgebaut wurde. **Ein paar Punkte Abweichung an der richtigen Stelle zerstören das gesamte Seitenbild.** Deshalb ist „ungefähr richtig" hier gleichbedeutend mit falsch.

---

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
| **2 (Spiegel)** | `Banking Newsletter/Example Design/` im Repository **aus der Routine** (Standardwert `Daily-Banking-Newsletter`) | Nur wenn Priorität 1 nicht erreichbar ist (Cloud-Lauf ohne Mac-Zugriff). Die Repo-Kopie ist **immer nur ein Spiegel** des Desktop-Ordners und wird in Schritt 0d täglich aufgefrischt. |
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
- ❌ Ausgaben aus dem Ordner `Banking Newsletter/Output` (sind Ergebnisse, keine Vorlagen)

**Einzige Bilddatei, die verwendet wird:** `Banking Newsletter/Example Design/Newsletter_Wallpaper.jpeg` als Hero-Bild auf der Cover Page.

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
| **Weiße Karte** (Container der 6 News) | **x 31.5–564.0** (Breite **532.5**), **y 408.0–771.8** (Höhe **363.8**) | — | Weiß, leichter Schatten, ragt über das Hero-Bild |
| Karten-Titel `DIE 6 WICHTIGSTEN MELDUNGEN DES TAGES` | x 45.3, y 423 | 8.6 pt | Arial Bold, `#05415A`, Großbuchstaben |
| Karten-Hinweis rechts | x 351.6, y 424 | 6.9 pt | Arial, grau |
| Fußzeile | y 793 / 804 | 7.0 pt | zentriert, auf dunklem Grund |

**Die 6 News auf Seite 1 — festes 3-Spalten-Raster (3 Spalten × 2 Reihen):**

| | Spalte 1 | Spalte 2 | Spalte 3 |
| --- | --- | --- | --- |
| Textkante x | **45.3** | **222.8** | **391.0** |
| Nummer-Badge x | 50.2 | 227.6 | 395.8 |
| Nutzbare Textbreite | rund 155 pt | rund 155 pt | rund 155 pt |

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

**🔴 DER AUFBAU DES COVERS — GENAU DREI FLÄCHEN, NICHT MEHR**

Die Vorlage baut das Cover aus **genau drei Zeichenflächen** auf:

| # | Fläche | Maße |
| --- | --- | --- |
| 1 | Weißer Seitenhintergrund | x 0–595.5, y 0–842.2 |
| 2 | Dunkelblaue Fläche `#05415A` über die **ganze Seite** | x 0–595.5, y 0–842.2 |
| 3 | **Weiße Karte** für die 6 News | x **31.5–564.0**, y **408.0–771.8** |

Darüber liegt **ein einziges eingebettetes Bild** (`Newsletter_Wallpaper.jpeg`), das den oberen Bereich füllt.

⚠️ **DEN BILDVERLAUF NICHT NACHBAUEN.** In der Ausgabe vom 13.08.2026 wurden **30 gestapelte Rechtecke** à 13,4 pt übereinandergelegt, um einen Verlauf zu simulieren. Ergebnis: ein dunkles, streifiges Bild statt der hellen Stadtansicht. **Das Bild wird als Bild eingebettet, mit der dunkelblauen Fläche dahinter — keine gestapelten Streifen, keine simulierten Verläufe.**

**Faustregel:** Mehr als **acht** Zeichenflächen auf dem Cover bedeuten, dass etwas nachgebaut wurde, das als Bild gehört. Die Vorlage kommt mit drei aus.

**Seiten 2–4 — Zwei-Spalten-Layout (ALLE WERTE AUS DER VORLAGE GEMESSEN, NICHT GESCHÄTZT):**

⚠️ **DIESE MASSE SIND EXAKT EINZUHALTEN. KEIN „ungefähr", KEIN „ca.".** Wurden sie geschätzt statt übernommen, kippt das gesamte Seitenbild — genau so entstand die fehlerhafte Ausgabe vom 13.08.2026 mit einem 90 pt hohen Kopfband statt 63 pt.

| Element | Exakter Wert |
| --- | --- |
| **Kopfband** | Fläche `#05415A`, x 0–595.5, **y 0.0–63.0** (Höhe **63 pt**, nicht 90) |
| **Titel** `Financial Services` / `Consulting Newsletter` | **zweizeilig**, x **31.2**, y **11.9** und **25.4**, **12.5 pt** Arial Bold, weiß |
| **Untertitel** `TÄGLICHER MARKTÜBERBLICK FÜR BANKING-CONSULTANTS` | x **31.2**, y **43.6**, **7.4 pt**, Farbe **`#AFD7EB`** (helles Blau, **nicht** weiß), gesperrt |
| **`AUSGABE DES`** rechts | x **504.6**, y **22.7**, **7.2 pt**, Farbe **`#AFD7EB`**, gesperrt |
| **Datum** `TT.MM.JJJJ` rechts | x **470.1**, y **31.6**, **19.0 pt** Arial Bold, weiß |
| **Seitenband** | Fläche `#008CC8`, **y 63.0–81.8** (Höhe **18.8 pt**) |
| Seitenband links `SEITE X — …` | x **31.2**, y **67.2**, **8.6 pt** Arial Bold, weiß |
| Seitenband rechts (Kurzhinweis) | x **404.2**, y **67.8**, **8.0 pt**, Farbe **`#DCEBFA`** |
| **Kernaussage-Box** | Fläche `#DCEBFA`, x **31.5–564.0** (Breite **532.5**), **y 89.2–171.8** (Höhe **82.5 pt**) |
| Box-Titel `KERNAUSSAGE DES TAGES` | x **48.7**, y **94.4**, **7.6 pt** Arial Bold, `#008CC8` — **dieser Titel ist Pflicht** |
| **Spaltenüberschrift links** `NACHRICHTENLAGE` | x **31.2**, y **179.1**, **6.8 pt** Arial Bold, `#05415A`, dahinter in `#4A5B66`: `— was heute gemeldet wird` |
| **Spaltenüberschrift rechts** | `BEDEUTUNG FÜR DAS BANKING-CONSULTING`, gleiche Höhe, gleiches Format |
| **Linke Spalte** | Textkante x **31.2**, weißer Grund |
| **Rechte Spalte** | Fläche `#DBEAF2`, x **261.8–564.0** (Breite **302.2**), **y 179.2–825.0** |
| **Blockbalken rechte Spalte** | Fläche `#05415A`, x **268.5–557.2** (Breite **288.8**), Höhe **12.8 pt** |
| **Fußzeile** | Datum `TT.MM.JJJJ`, x **529.6**, y **820.9**, **7.0 pt**, Farbe **`#4A5B66`** |

**Aufbau eines News-Blocks in der linken Spalte (Seiten 2–4) — vier Bausteine, immer vollständig:**

| Baustein | Exakte Größe | Stil |
| --- | --- | --- |
| Kategorie (z. B. `KI IM BETRIEB`) | **6.0 pt** | Arial Bold, `#008CC8`, gesperrt, Großbuchstaben |
| Headline | **7.6 pt** | Arial Bold, `#05415A` |
| Fließtext | **6.9 pt** | Arial regular, `#1E2B33`, Zahlen fett hervorgehoben |
| **Quellenangabe** | **6.1 pt** | **Arial kursiv, grau, in Klammern, eigene Zeile am Blockende** |
| Trennlinie darunter | 0.5 pt | hellgrau, volle Spaltenbreite |

🔴 **Die Quellenzeile ist Teil des Blocks, nicht optional.** Sie steht direkt unter dem Fließtext, vor der Trennlinie. Mehrere Quellen werden mit **Semikolon** getrennt: `(S&P Global & McKinsey, 2026; Hunton, 2026)`.

**Seite 5 — Quellenverzeichnis (gemessen):**

| Element | Exakter Wert |
| --- | --- |
| Kopfband | `#05415A`, **y 0.0–63.0** — identisch zu Seiten 2–4 |
| Seitenband | `#008CC8`, **y 63.0–81.8**, Text `SEITE 5 — QUELLENVERZEICHNIS` |
| Einleitungszeile | „Alphabetisch nach Autor oder Organisation…" |
| Layout | **2 Spalten**, Textkanten x **31.2** (links) und x **306.1** (rechts) |
| Hängender Einzug | Folgezeilen ab x **42.5** (links) und x **317.5** (rechts) |
| **Schriftgröße** | **7.5 pt** — durchgehend für alle Einträge |
| Format | APA-7, Titel kursiv, URL in `#008CC8` |
| Fußzeile | Datum, x **529.6**, y **820.9**, **7.0 pt**, `#4A5B66` |

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

Alle bisherigen Ausgaben bleiben im Ordner `Banking Newsletter/Output` und dienen als Archiv und für den Abgleich mit den letzten 5 Tagen. **Sie sind kein Design-Maßstab** — der Maßstab ist ausschließlich die Vorlage-PDF aus 12.1.

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

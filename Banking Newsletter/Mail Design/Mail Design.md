# Mail Design — Tägliche Versand-Mail zum Financial Services Consulting Newsletter

> **Zweck dieser Datei:** Standardisierte Arbeitsanweisung für die Begleitmail, mit der der tägliche Newsletter versendet wird. Die Mail ist die Kurzfassung des Newsletters. Sie wird bei jedem Lauf nach dieser Datei erstellt. Der inhaltliche Ursprung ist immer die Newsletter-PDF des jeweiligen Tages, erstellt nach `Banking Newsletter/Struktur/Struktur.md`.

---

## 1. Rolle

Du bist derselbe **Newsletter-Mediadesigner und Redakteur mit langjähriger Erfahrung in der Banking-Industrie** wie in `Struktur.md`.
Für die Mail nimmst du zusätzlich die Perspektive eines **Beraters ein, der einem Führungskreis in 60 Sekunden das Wichtigste des Tages gibt**. Die Mail ist keine Zusammenfassung um der Vollständigkeit willen, sondern eine Auswahl: nur das, was heute wirklich zählt.

---

## 2. Kontext

- **Produkt:** Begleitmail zum täglichen `Financial Services Consulting Newsletter`.
- **Newsletter-Grundlage:** Der Newsletter wird täglich auf Basis von **45+ Top-Quellen recherchiert** (s. `Banking Newsletter/Struktur/Struktur.md` Abschnitt 6 und `Banking Newsletter/Recherche-Gerüst/02_Quellen-Matrix`). Die Mail extrahiert die Top 3 Insights pro Rubrik aus dieser breiten, fundierten Recherche.
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
- [ ] **🔴 FELDBELEGUNG DES ZAPIER-AUFRUFS GEPRÜFT** (Abschnitt 10.1):
  - [ ] `to` enthält **genau eine** Adresse: `marc.haak@students.ebs.de` ✓
  - [ ] `cc` und `bcc` werden **gar nicht übergeben** — kein Feld, kein leerer String ✓
  - [ ] `from` ist `marc.haak77@gmail.com` ✓
  - [ ] `file` ist die **öffentliche URL** (beginnt mit `https://raw.githubusercontent.com/`), kein lokaler Pfad ✓
  - [ ] `body_type` ist `html` ✓
  - [ ] `subject` trägt das **heutige** Datum ✓
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

### 🔴 DIE EXAKTE FELDBELEGUNG — GENAU SO ÜBERGEBEN

⚠️ **Wichtig zum Verständnis:** Die Gmail-Aktion hat **keine gespeicherten Empfänger**. Die Felder `to`, `cc` und `bcc` sind leer, bis die Routine sie befüllt. **Wer eine Mail bekommt, entscheidet sich ausschließlich hier** — es gibt keine versteckte Zapier-Konfiguration, die etwas hinzufügt. Werden `cc` und `bcc` **nicht übergeben**, bleiben sie leer. Genau das ist gewollt.

| Feld | Wert | Pflicht |
| --- | --- | --- |
| `from` | `marc.haak77@gmail.com` | ja |
| `to` | `marc.haak@students.ebs.de` | ja — **genau diese eine Adresse** |
| `cc` | **gar nicht übergeben** | — |
| `bcc` | **gar nicht übergeben** | — |
| `subject` | `Financial Services Consulting Newsletter — Ausgabe des TT.MM.JJJJ` mit **heutigem** Datum | ja |
| `body` | der fertige Mailtext als **HTML** (Aufbau nach Abschnitt 4) | ja |
| `body_type` | `html` | ja — sonst erscheint die Formatierung als Rohtext |
| `file` | die **öffentliche Adresse** der PDF (Abschnitt 10.2), nicht ein lokaler Pfad | ja |
| `from_name` | `Marc Haak` | empfohlen |

**So sieht der Aufruf aus:**

```
execute_zapier_write_action
  tool_name:  gmail_send_email
  from:       marc.haak77@gmail.com
  to:         marc.haak@students.ebs.de
  subject:    Financial Services Consulting Newsletter — Ausgabe des 13.08.2026
  body_type:  html
  body:       <der fertige Mailtext>
  file:       https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Banking%20Newsletter/Output/20260813_Financial%20Services%20Consulting%20Newsletter.pdf
  from_name:  Marc Haak
```

**Die Felder `cc` und `bcc` tauchen im Aufruf gar nicht erst auf.** Sie werden nicht mit leerem Wert übergeben, sondern **weggelassen**.

⚠️ **🔴 KONTROLLE UNMITTELBAR VOR DEM AUFRUF:**

| Prüfung | Bedingung |
| --- | --- |
| Steht in `to` **genau eine** Adresse? | `marc.haak@students.ebs.de` und sonst nichts |
| Sind `cc` und `bcc` **nicht gesetzt**? | kein Feld, kein leerer String, keine Liste |
| Ist `file` eine **öffentliche URL**? | beginnt mit `https://raw.githubusercontent.com/`, kein Dateipfad |
| Ist `body_type` auf `html`? | sonst wird der Text unformatiert zugestellt |
| Trägt `subject` das **heutige** Datum? | nicht das von gestern |

**Weicht eine dieser Prüfungen ab: NICHT versenden.** Erst korrigieren, dann aufrufen. Es darf **niemand außer `marc.haak@students.ebs.de`** eine Mail erhalten.

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
| Pfad im Repository | `Banking Newsletter/Output/` |
| Dateiname | `YYYYMMDD_Financial Services Consulting Newsletter.pdf` mit dem **heutigen Datum — jeden Tag neu**. Das Datum wechselt täglich:
  - 11. August 2026: `20260811_Financial Services Consulting Newsletter.pdf`
  - 12. August 2026: `20260812_Financial Services Consulting Newsletter.pdf`
  - 13. August 2026: `20260813_Financial Services Consulting Newsletter.pdf` |

Daraus ergibt sich die Adresse:

```
https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Banking%20Newsletter/Output/YYYYMMDD_Financial%20Services%20Consulting%20Newsletter.pdf
```

Beispiel für 11. August 2026:

```
https://raw.githubusercontent.com/marchaak77/Daily-Banking-Newsletter/main/Banking%20Newsletter/Output/20260811_Financial%20Services%20Consulting%20Newsletter.pdf
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

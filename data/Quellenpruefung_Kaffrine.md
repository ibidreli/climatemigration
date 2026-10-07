# Quellenprüfung Kaffrine: Bevölkerung und Migration

Stand: 7. Oktober 2026. Auswertung der in dieser Unterhaltung bereitgestellten Dateien. Keine zusätzliche Internetrecherche. Die Original-CSV-Dateien, das Modell und das Notebook wurden nicht verändert.

## Ergebnis

Beide Datensätze lassen sich deutlich erweitern. Für die Bevölkerung sind zehn weitere historische Jahreswerte direkt in Bevölkerungsdarstellungen belegt, zusätzlich zwei vorsichtig zu behandelnde Werte aus Gesundheitskapiteln. Für 2024–2050 liegen 27 jährliche regionale Projektionen vor. Für die Migration gibt es zusätzliche Angaben zu Zuzug, Wegzug und Salden, internationale Migration sowie Vergleichswerte aus der Volkszählung 2013.

Es entsteht daraus **keine durchgehende beobachtete jährliche Zeitreihe**. Volkszählungswerte, ältere Schätzungen, Projektionen sowie verschiedene Migrationsfenster müssen unterscheidbar bleiben.

## 1. Geprüfte Quellen und ihr Beitrag

Die Seitenangaben beziehen sich auf die PDF-Seitenzählung ab der ersten Dateiseite. Bei SES 2013 liegt die aufgedruckte Seitenzahl fünf Seiten höher; beide Angaben werden dort genannt.

| Kürzel | Datei | Ergebnis für die beiden Datensätze |
|---|---|---|
| S10 | SES_Kaffrine_2010(1).pdf | Bevölkerung 2009 und 2010, räumliche und Altersgliederungen. S. 18 erklärt ausdrücklich, dass ältere Migrationsergebnisse die neue Regionsgliederung nicht berücksichtigen. |
| S12 | SES_Kaffrine-2012(1).pdf | Bevölkerungsschätzung 2012; indirekter Hinweis auf 2011 im Gesundheitskapitel. Keine zusätzliche für diese Auswertung gesicherte regionale Migrationszählung. |
| S13 | SES-Kaffrine-2013(1).pdf | Bevölkerung 2002 und 2013, Geburten- und Sterberaten, Binnenmigration mit 1-, 5- und 10-Jahresbezug, internationale Migration. |
| S17 | SES-Kaffrine - 2017-2018(1).pdf | Historische Bevölkerungsreihe 1976, 1988, 2002, 2013 sowie Projektionen 2017 und 2018. |
| S20 | SES-Kaffrine_2020-2021-rev(1).pdf | Bevölkerungsschätzungen/Projektionen 2020 und 2021 mit regionaler und räumlicher Gliederung. |
| S22 | SES-Kaffrine_2022-2023(1).pdf | Volkszählungsangaben 2023, demografische Raten und Migration; mehrere redaktionelle Widersprüche. Bevölkerungsnenner 2022 im Gesundheitskapitel. |
| M23 | Chapitre-6_MIGRATIONS-Rapport-def-RGPH-5(1).pdf | Hauptquelle für Migration 2023, Definitionen und rückblickende Lebenszeitmigration 2013. |
| P23 | Projections-demographiques_2023-2073-(1).pdf | Regionale Bevölkerung jährlich 2023–2050, nach Geschlecht und Stadt/Land; weitere räumliche Untergliederungen. 2023 ist Basis, 2024–2050 sind Projektionen. Der Gesamttitel bis 2073 darf nicht als regional verfügbare Reihe bis 2073 verstanden werden. |
| Ausgangsdaten | ansd_bevoelkerung_kaffrine.csv | Zwei Ausgangswerte: 2013 = 566’992; 2023 = 820’405. |
| Ausgangsdaten | ansd_migration_kaffrine_2023.csv | Zwei Ausgangswerte: Binnenwegzug 5 Jahre = 27’588; Lebenszeit = 80’171. Beide Zahlen sind in M23 belegt, die Beschreibungen brauchen Präzisierung. |
| Modell | model.py | Prüft den Verwendungszweck: Bevölkerungsbestand, natürlicher Zuwachs und Abwanderung. Zuzug ist bisher nicht modelliert. |
| Notebook | 01_LE2_Systemdynamik.ipynb | Enthält Aussagen über fehlende internationale Migration und Ertragsdaten, die durch die mitgegebenen Quellen überholt sind. |
| Übersicht | 00_LE2_Overview.md | Beschreibt Aufbau und Anforderungen, enthält keine zusätzlichen statistischen Originalwerte. |
| Projektmaterial | pasted.txt, pasted(1).txt, pasted(2).txt | Kursbeschreibung und weiterführende Methodenlinks, keine Kaffrine-Zeitreihen. Die verlinkten externen Inhalte wurden nicht separat abgerufen. |
| Aufgabenstellung | mss-Mini-Challenge-LE1-1753629155.pdf | Methodische Anforderungen an die Systemkartierung; keine zusätzlichen Kaffrine-Bevölkerungs- oder Migrationswerte. |

## 2. Ergänzungen zur Bevölkerungsdatei

### 2.1 Historische Werte und vorhandene Referenzwerte

Alle Werte beziehen sich auf die Region bzw. bei älteren Volkszählungen auf das in den Quellen rückblickend dargestellte Vorgängergebiet. Die heutige Region entstand 2008 aus dem früheren Département Kaffrine der Region Kaolack. Das frühere Département ist nicht mit dem heutigen, kleineren Département Kaffrine gleichzusetzen. Für detaillierte räumliche Vergleiche sind die Grenzen zusätzlich zu harmonisieren.

| Jahr | Personen | Datentyp | Fundstelle | Bewertung |
|---|---:|---|---|---|
| 1976 | 239’282 | Historischer Volkszählungswert, rückblickende Gebietszuordnung | S17, S. 33, Tab. II-1; S22, S. 18, Tab. II-1 | Neu; Gebietsbezug dokumentieren |
| 1988 | 323’029 | Historischer Volkszählungswert, rückblickende Gebietszuordnung | S17, S. 33; S22, S. 18 | Neu; Gebietsbezug dokumentieren |
| 2002 | 465’671 | Volkszählung des damaligen Départements | S13, PDF-S. 15 / Druck-S. 20; S17, S. 33 | Neu; Vorgängergebiet ausdrücklich erklärt |
| 2009 | 540’733 | Schätzung/Projektion | S10, S. 76, Tab. 85; auch S. 21 | Neu; keine Volkszählung |
| 2010 | 558’041 | Schätzung/Projektion | S10, S. 16, Tab. 3 und Fussnote 2; S. 78, Tab. 86 | Neu; keine Volkszählung |
| 2012 | 589’418 | Schätzung | S12, S. 15–16 | Neu; nicht direkt mit dem tieferen Volkszählungswert 2013 als reale Abnahme interpretieren |
| 2013 | 566’992 | Volkszählung RGPHAE 2013 | S13, PDF-S. 15–16 / Druck-S. 20–21 | Bereits vorhanden und bestätigt |
| 2017 | 655’121 | ANSD-Projektion | S17, S. 33, Tab. II-1 | Neu; kein unabhängiger beobachteter Backtest-Punkt |
| 2018 | 678’955 | ANSD-Projektion | S17, S. 33, Tab. II-1 | Neu; kein unabhängiger beobachteter Backtest-Punkt |
| 2020 | 728’948 | ANSD-Projektion | S20, S. 20, Tab. II-1 und S. 22, Tab. II-3 | Neu; kein unabhängiger beobachteter Backtest-Punkt |
| 2021 | 755’172 | ANSD-Projektion | S20, S. 19–22 | Neu; kein unabhängiger beobachteter Backtest-Punkt |
| 2023 | 820’405 | Als vorläufiges RGPH-5-Ergebnis bezeichnet | S22, S. 17–18 | Bereits vorhanden; abweichende Variante unten |
| 2023 | 820’404 | RGPH-5-Basiswert in neuer Projektionstabelle | P23, S. 33; auch S22, S. 20, Tab. II-2 | Quellenvariante; nicht als zweites unabhängiges Beobachtungsjahr behandeln |

**Zwei zusätzliche Kandidaten mit eingeschränkter Belegqualität:**

| Jahr | Personen | Fundstelle | Einschränkung |
|---|---:|---|---|
| 2011 | 572’736 | S12, S. 22 | Im Vergleich der Krankenhausversorgung verwendeter früherer Bevölkerungsnenner. Jahreszuordnung 2011 aus Kontext; keine sauber beschriftete regionale Bevölkerungstabelle. Als Kandidat kennzeichnen. |
| 2022 | 782’273 | S22, S. 65, Tab. XI-3 | Expliziter Bevölkerungsnenner im Gesundheitskapitel, Quelle Région médicale de Kaffrine 2024. Nicht als Volkszählung oder gesicherter ANSD-Projektionswert umetikettieren. |

Für 2014–2016 und 2019 wurde in dieser Prüfung kein ausreichend belegter regionaler Jahresgesamtwert für eine direkte Ergänzung identifiziert. Diese Lücken nicht still durch Interpolation auffüllen.

### 2.2 Jährliche Projektionen 2024–2050

Quelle aller folgenden Werte: P23, jeweilige Tabelle «PROJECTION DE LA POPULATION DE LA REGION KAFFRINE», Zeile «REGION KAFFRINE», Spalte «Ensemble». Einheit: Personen. Als `datentyp=projektion` ablegen. Die Reihe beruht auf 820’404 Personen im Jahr 2023.

| Jahr | Personen | PDF-Seite |
|---|---:|---:|
| 2024 | 848’581 | 33 |
| 2025 | 878’045 | 33 |
| 2026 | 908’865 | 71 |
| 2027 | 941’072 | 71 |
| 2028 | 974’684 | 71 |
| 2029 | 1’009’698 | 109 |
| 2030 | 1’046’119 | 109 |
| 2031 | 1’083’863 | 109 |
| 2032 | 1’122’910 | 146 |
| 2033 | 1’163’232 | 146 |
| 2034 | 1’204’796 | 146 |
| 2035 | 1’247’698 | 183 |
| 2036 | 1’291’891 | 183 |
| 2037 | 1’337’333 | 183 |
| 2038 | 1’383’977 | 219 |
| 2039 | 1’431’889 | 219 |
| 2040 | 1’481’129 | 219 |
| 2041 | 1’531’684 | 256 |
| 2042 | 1’583’542 | 256 |
| 2043 | 1’636’690 | 256 |
| 2044 | 1’691’273 | 293 |
| 2045 | 1’747’368 | 293 |
| 2046 | 1’805’033 | 293 |
| 2047 | 1’864’326 | 330 |
| 2048 | 1’925’305 | 330 |
| 2049 | 1’988’058 | 330 |
| 2050 | 2’052’681 | 330 |

Diese Werte eignen sich als externer Szenariovergleich für das Modell bis 2050. Sie sind keine zusätzlich gemessenen Bevölkerungswerte. Der Bericht erläutert auf S. 6 die Anpassung der Altersstruktur und auf S. 9–10 die Migrationsannahmen, darunter die Annahme eines konstanten Migrationssaldos. Eine Übereinstimmung des eigenen Modells mit dieser Reihe ist daher keine unabhängige empirische Validierung.

### 2.3 Weitere verfügbare Gliederungen

P23 enthält für dieselben Jahre auch Männer/Frauen, Stadt/Land und Werte für Départements, Arrondissements und Gemeinden. Historische Gliederungen finden sich unter anderem in S10, S. 16–17 und 76–79; S13, PDF-S. 16 / Druck-S. 21; S17, S. 35–36; S20, S. 22; S22, S. 20. Für das derzeitige Modell mit einem einzigen regionalen Bevölkerungsbestand sind regionale Gesamtwerte die passenden direkten Eingaben. Untergruppen sind zusätzliche Variablen und dürfen nicht als weitere Regionalgesamtwerte angehängt werden.

## 3. Ergänzungen zur Migrationsdatei

### 3.1 Volkszählung 2023

Zuzug und Wegzug beziehen sich jeweils auf Kaffrine. Salden sind Zuzug minus Wegzug. Die beiden bereits vorhandenen Wegzugswerte sind hier zum Vergleich enthalten.

| Raumbezug | Referenz | Zuzug | Wegzug | Saldo laut Quelle | Fundstelle |
|---|---|---:|---:|---:|---|
| Innerhalb Senegals | Lebenszeit: Geburtsregion vs. Wohnregion 2023 | 31’283 | 80’171 | −48’888 | M23, S. 20, Tab. VI-3; S. 22, Tab. VI-4 |
| Innerhalb Senegals | Wohnregion Mai 2018 vs. Volkszählung 2023 | 13’645 | 27’588 | −13’943 | M23, S. 23, Tab. VI-5 |
| Innerhalb Senegals | Wohnregion Mai 2022 vs. Volkszählung 2023 | 15’251 | 25’956 | −10’706* | M23, S. 26, Tab. VI-7 |
| International | Fünfjahresbezug der Erhebung 2023 | 238 | 2’447 | −2’209 | M23, S. 55, Tab. VI-35 |
| International | Einjahresbezug der Erhebung 2023 | 128 | 742 | −614 | M23, S. 56, Tab. VI-36 |

*Rechnerisch ergeben 15’251 − 25’956 = −10’705. Die Quelle druckt −10’706. Rohwert und selbst berechneten Saldo getrennt speichern; die Differenz von einer Person nicht still korrigieren.*

Weitere regionale Migrationsdaten in M23:

| Grösse | Personen | Fundstelle | Bedeutung |
|---|---:|---|---|
| Internationale Einwanderung, Lebenszeit | 1’797 | S. 35, Fortsetzung der Tabelle zu internationalen Lebenszeitimmigranten | Im Ausland geborene Personen, die in Kaffrine wohnen |
| Davon Männer / Frauen | 846 / 951 | S. 35 | Geschlechtergliederung des Bestands von 1’797 |
| Internationale Einwanderung, Fünfjahresbezug: Männer / Frauen | 135 / 103 | S. 40 | Summe = 238 |
| Internationale Einwanderung, Einjahresbezug: Männer / Frauen | 89 / 38 | S. 47 | Summe = 127, Gesamtsumme der Quelle = 128; Widerspruch markieren |
| Internationale Auswanderung, Fünfjahresbezug: Männer / Frauen | 2’255 / 192 | S. 52 | Summe = 2’447; 92,1 % bzw. 7,9 % |

M23 enthält ausserdem Nationalitätsgliederungen für internationale Zuwanderung, unter anderem auf S. 36, 43 und 48. Diese Untergliederungen wurden nicht als zusätzliche eigenständige Wanderungsflüsse in die obige Zusammenstellung aufgenommen.

### 3.2 Vergleichswerte aus der Volkszählung 2013

Die Erhebung ist 2013; der angegebene Zeitraum ist jeweils rückblickend. Fehlende Angaben sind **nicht null**.

| Raumbezug | Referenz | Zuzug | Wegzug | Saldo | Fundstelle |
|---|---|---:|---:|---:|---|
| Innerhalb Senegals | Lebenszeit | 35’053 | 74’671 | −39’618 | M23, S. 22, Tab. VI-4, Block RGPHAE 2013 |
| Innerhalb Senegals | Zehnjahresbezug | 18’588 | 34’353 | −15’765 | S13, PDF-S. 28 / Druck-S. 33, Tab. I.6 |
| Innerhalb Senegals | Fünfjahresbezug | 17’048 | 32’829 | −15’781 | S13, PDF-S. 28 / Druck-S. 33, Tab. I.6 |
| Innerhalb Senegals | Einjahresbezug | 10’185 | 30’925 | −20’740 | S13, PDF-S. 28 / Druck-S. 33, Tab. I.6 |
| International | Zehnjahresbezug | 1’842 | nicht ausgewiesen | nicht ausgewiesen | S13, PDF-S. 29 / Druck-S. 34, Tab. I.7 |
| International | Fünfjahresbezug | 1’318 | 1’936 | −618 | S13, PDF-S. 29 / Druck-S. 34, Tab. I.7 |
| International | Einjahresbezug | 580 | nicht ausgewiesen | nicht ausgewiesen | S13, PDF-S. 29 / Druck-S. 34, Tab. I.7 |

Diese Werte liefern zusätzliche Vergleichsfenster. Die ursprünglichen Frageformulierungen, Altersgrenzen und Gebietszuordnungen sind vor einem formalen Vergleich der Erhebungen zu harmonisieren. Die Zehnjahreswerte 2013 reichen zudem über die Regionsgründung 2008 zurück.

### 3.3 Was die Zahlen tatsächlich messen

Die Definitionen in M23, S. 15–16 und 23, sind für die Modellierung entscheidend:

- **Lebenszeitmigration ist ein Bestand nach Geburts- und aktuellem Wohnort.** 80’171 ist weder die Summe sämtlicher jemals erfolgter Wegzüge noch die Zahl von Netzwerkmitgliedern mit einer bekannten Verweildauer.
- **Binnenmigration mit Fünfjahresbezug vergleicht Wohnorte zweier Zeitpunkte** und betrifft mindestens fünfjährige Personen. Zwischenzeitliche Mehrfachumzüge und Rückkehrbewegungen sind daraus nicht vollständig erkennbar. 27’588 ist deshalb keine direkt gemessene Summe aller jährlichen Umzugsereignisse.
- Das Einjahresfenster bezieht sich auf Mai 2022 gegenüber der Volkszählung 2023, das Fünfjahresfenster auf Mai 2018 gegenüber 2023. Die Notebook-Beschriftung «2018–2022» ist dafür nur eine Modellannäherung und nicht der exakte Erhebungszeitraum.
- Ein- und Fünfjahreswerte dürfen nicht addiert werden. Sie sind auch nicht so zu interpretieren, dass der Einjahreswert zwingend ein Fünftel des Fünfjahreswertes sein müsste: Beobachtungsfenster, Altersauswahl und Wohnortübergänge unterscheiden sich.
- Internationale Auswanderung erfasst laut M23 aus Haushalten ins Ausland fortgezogene Mitglieder, die dort noch wohnen, mit einer Dauer von mindestens sechs Monaten. Internationale Einwanderung beruht auf vorherigem Auslandswohnsitz. Das ist keine lückenlose Grenzübertrittsstatistik.
- Binnen- und internationale Migration zunächst getrennt halten. Ein gemeinsamer Modellabfluss erfordert eine begründete Zuordnung und Prüfung möglicher Überschneidungen sowie der unterschiedlichen Erfassungsweisen.
- Die Grundgesamtheiten der Migrationstabellen sind nicht identisch mit der gesamten regionalen Einwohnerzahl. Beispielsweise nennt die Fünfjahrestabelle 679’677 erfasste Bewohner. Diese Zahl ist kein weiterer Bevölkerungswert für die Gesamtregion.

## 4. Quellenwidersprüche und Entscheidungsvorschläge

| Problem | Beleg | Umgang |
|---|---|---|
| Bevölkerung 2023: 820’405 vs. 820’404 | S22 S. 17–18 vs. S22 S. 20 und P23 S. 33 | Originalwert erhalten, Variante dokumentieren. Für den Vergleich mit P23 dessen Basis 820’404 verwenden. Keine unbestätigte Erklärung als Revision oder Rundung behaupten. |
| Binnenwegzug Einjahresbezug 2023: 25’529 vs. 25’956 | S22 S. 22 vs. S22 S. 21 und M23 S. 26 | 25’956 aus dem definitiven Migrationsbericht bevorzugen; 25’529 als abweichende Angabe vermerken. |
| Einjahressaldo 2023 um eine Person abweichend | M23 S. 26 | −10’706 als Quellenwert, −10’705 als berechneten Wert kennzeichnen. |
| Ein- und Auswanderungsrichtung bei Lebenszeitmigration im Fliesstext vertauscht | S22 S. 21 | Auf M23 S. 20 stützen: 31’283 Zuzug, 80’171 Wegzug. |
| Internationale Auswanderung als «1,5 % der Bevölkerung» beschrieben | S22 S. 21 | M23 S. 49: 1,5 % ist der Anteil Kaffrines an den landesweiten internationalen Auswanderern, nicht an der Bevölkerung Kaffrines. |
| Internationale Einwanderung Einjahr: Geschlechtersumme 127 vs. Total 128 | M23 S. 47; Total auch S. 56 | Gesamtwert 128 übernehmen, Geschlechterwerte mit Abweichungskennzeichen. |
| Gesundheitstabelle verwendet für 2023 nur 810’304 Personen | S22 S. 65 | Sektoralen Nenner nicht als Ersatz des Zensuswertes 820’404/820’405 verwenden. |
| Gesundheitsgesamtwert 2010 = 509’532 | S10 S. 21, Tab. 9 | Widerspricht den Bevölkerungstabellen S. 16 und 78; 558’041 bevorzugen. |
| 2012: 589’417 im Gesundheitskapitel vs. 589’418 in Demografie | S12 S. 22 vs. S. 15 | 589’418 aus dem Demografiekapitel bevorzugen; Variante dokumentieren. |
| Fehlerhafte Jahresüberschrift in Bevölkerungstabelle | S20 S. 20: doppelte Überschrift 2020 | 2020/2021 durch Tab. II-3 auf S. 22 abgesichert; älteren Wert 1988 aus S17/S22 übernehmen. |

Nicht jede Zahl in einem amtlichen Bericht ist automatisch intern konsistent. Die aufgeführten Fehler rechtfertigen keine pauschale Verwerfung der Quellen, wohl aber die Auswahl klar belegter Tabellen und die Dokumentation von Varianten.

## 5. Zusätzliche Daten für das natürliche Bevölkerungswachstum

| Erhebung | Rohe Geburtenrate je 1’000 Personen | Rohe Sterberate je 1’000 Personen | Eigene Differenz | Quelle |
|---|---:|---:|---:|---|
| 2013 | 46,4 | 8,5 | 37,9 ‰ = 3,79 % pro Jahr | S13, PDF-S. 20 und 22 / Druck-S. 25 und 27 |
| 2023 | 38,6 | 5,0 | 33,6 ‰ = 3,36 % pro Jahr | S22, S. 21–22, Tab. II-4 |

Die Differenzen sind selbst berechnete Näherungen für den natürlichen Zuwachs im jeweiligen Bezugsjahr, keine durchgehende gemessene Wachstumsreihe. Sie können die bisherige pauschale Annahme von 2,9 % im Modell besser begründen. Eine konstante Übernahme über 2013–2050 wäre wiederum eine Modellannahme. Gesamtbevölkerungswachstum enthält zusätzlich Migration und ist nicht gleich natürlichem Wachstum.

## 6. Konsequenzen für eure Dateien und LE2

### Bevölkerungsdatei

Die bisherigen Spalten `jahr,bevoelkerung,quelle` reichen für eine gemischte Datenbasis nicht aus. Ergänzen würde ich mindestens `datentyp`, `gebietsbezug`, `pdf_seite`, `tabelle` und `hinweis`. Die beiden 2023-Varianten dürfen nicht unmarkiert unter demselben Jahresschlüssel stehen. Das Modell braucht eine ausdrücklich gewählte Referenzreihe; Projektionen müssen beim Backtest ausgeschlossen werden.

### Migrationsdatei

Das jetzige Schema passt zu einer einzigen Erhebung. Für 2013 und 2023 sollte jede Zeile mindestens `erhebungsjahr`, `raumbezug`, `zeitfenster`, `richtung`, `personen`, `quelle`, `pdf_seite`, `tabelle` und `hinweis` enthalten. Zeitfenster und Richtung dürfen nicht allein in unklaren Freitexten verborgen sein. Fehlende Werte bleiben fehlend.

### Modell und Notebook

1. Die Aussage «internationale Auswanderung für Kaffrine nicht ausgewiesen» korrigieren: Für 2023 sind 2’447 mit Fünfjahres- und 742 mit Einjahresbezug vorhanden; für 2013 sind 1’936 mit Fünfjahresbezug vorhanden.
2. Zuzug als zusätzlichen Zufluss prüfen. Er ist in den Quellen beziffert und kann für die Bevölkerungsbilanz nicht ohne Weiteres ignoriert werden. Neue Werte allein beheben aber nicht automatisch die bisherige Modellabweichung.
3. Die Umrechnung `27588 / 5` ausdrücklich als Annualisierungsannahme behandeln. Sie ergibt 5’517,6 Personen pro Jahr, ist aber keine beobachtete Jahresreihe. Kalibrierung an dieser Zahl und anschliessender Vergleich mit derselben Zahl bleibt eine Konsistenzprüfung.
4. Die 2013er Lebenszeitabwanderung von 74’671 ist zeitlich näher am Modellstart als die bisher zum Vergleich genutzten 80’171 aus 2023. Sie entspricht dennoch nicht automatisch dem modellierten Netzwerkbestand.
5. Die natürliche Wachstumsrate mit regionalen Geburten- und Sterberaten begründen. Die weiterhin mögliche Diskrepanz zur Zensusentwicklung sorgfältig diskutieren; aus den vorliegenden Zahlen folgt kein gesicherter Nachweis einer Untererfassung 2013.
6. Projektionen 2024–2050 als Referenzszenario verwenden, nicht als historische Validierung. Historische Projektionen 2017–2021 sind ebenfalls keine unabhängig beobachteten Zwischenjahre.
7. Auch die Notebook-Aussage «keine regionalen Ertragsdaten» muss korrigiert werden. Beispielsweise enthält S22 auf S. 108, Tab. XVIII-3/4, Anbauflächen, Erträge und Produktion; S20 auf S. 125, S17 auf S. 133–134, S12 auf S. 107 und S13 auf PDF-S. 106–107 / Druck-S. 111–112 bieten weitere landwirtschaftliche Tabellen. Das ist eine zusätzliche Datenquelle für die nächste Modellverbesserung; die Ertragsreihen wurden hier nicht vollständig extrahiert.

## 7. Grenzen der Prüfung

Alle bereitgestellten Dateien wurden nach ihrer Relevanz für die beiden Datensätze geprüft; die relevanten demografischen Tabellen, Definitionen und Widersprüche wurden im Detail ausgewertet. Unverwandte Fachkapitel wurden nicht vollständig in Daten umgewandelt. Die kritischen Tabellen für 2009, den Migrationswert 25’956 und die Projektionsbasis 820’404 wurden zusätzlich visuell am PDF kontrolliert.

Die Quellen erlauben keine durchgehende beobachtete jährliche Migrationsreihe für Kaffrine und keine direkte Schätzung des kausalen Dürreeffekts auf Migration. Die weiterführenden Methodenlinks in den Textdateien wurden nicht als zusätzliche externe Datenquellen untersucht. Alle aufgeführten Zahlen stammen aus den bereitgestellten Dateien; abgeleitete Zahlen sind entsprechend gekennzeichnet.

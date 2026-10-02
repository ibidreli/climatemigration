# **LE1 – Systemkarte: Klimabedingte Abwanderung aus Kaffrine**

## **1. Leitfrage**

Wie beeinflussen Dürre, Wasserknappheit und Ernteausfälle die Abwanderung aus der Region Kaffrine (Senegal), und welche Rückwirkungen hat die Abwanderung auf die lokale Bevölkerung und Landwirtschaft?

Dürre wird über den Niederschlag erfasst: Eine Dürre ist ein Jahr oder Szenario mit deutlich unterdurchschnittlichem Niederschlag.

## **2. Systemgrenzen**

### **Räumlich**

Region Kaffrine (Senegal), im Kontext der Sahel-Zone. Betrachtet wird die Abwanderung aus Kaffrine. Die Zielorte liegen ausserhalb des Systems.

### **Zeitlich**

| Zeitraum | Zweck |
|---|---|
| 2002–2023 | Vergleich mit echten Daten (Backtest) |
| 2024–2050 | Szenarien für die Zukunft |

Begründung anhand der Datenlage:

| Grösse | Datenquelle | Verfügbar |
|---|---|---|
| Niederschlag | CHIRPS v2.0 (Satellit und Stationen, 0.05°) | 1981 bis heute, jährlich |
| Bevölkerung | ANSD, Volkszählungen (RGPH) | 1976, 1988, 2002, 2013, 2023 |
| Abwanderung | ANSD, RGPH-5 2023, Kapitel Migration | Momentaufnahme (letztes Jahr, letzte 5 Jahre, Lebenszeit) |
| Landwirtschaft | ANSD, Situation économique et sociale (SES) Kaffrine; FAOSTAT national | regional ab Gründung der Region 2008 (zu prüfen), national ab 1961 |

Ab 2002 liegen drei Volkszählungen (2002, 2013, 2023) und lückenlose Niederschlagsdaten vor. Die Region Kaffrine besteht erst seit 2008 (vorher Teil von Kaolack). Daten vor 2008 müssen daher über die Departemente rekonstruiert werden. Die Abwanderung ist am schlechtesten belegt: Es gibt nur Momentaufnahmen aus den Volkszählungen, keine jährliche Zeitreihe.

### **Variablen im und ausserhalb des Systems**

| Variable | Rolle | Begründung |
|---|---|---|
| Niederschlag | exogen | Klima wird vom System nicht beeinflusst |
| Wasserverfügbarkeit, Landwirtschaftlicher Ertrag, Landwirtschaftliche Produktion | endogen (Kernmodell) | Kette von Klima zu Landwirtschaft |
| Landwirtschaftliches Einkommen, Haushaltseinkommen | endogen (Kernmodell) | wirtschaftliche Lage der Haushalte |
| Bevölkerung, Verfügbare Arbeitskräfte | endogen (Kernmodell) | Bestand der Region |
| Abwanderung, Abgewanderte Personen, Rücküberweisungen | endogen (Kernmodell) | Abwanderung und ihre Rückwirkungen |
| Nahrungsmittelverfügbarkeit pro Person | endogen (Kernmodell) | Versorgungsdruck in der Region |
| Temperatur, Bodenqualität, Anbaufläche, Wasserbedarf, Lebensmittelpreise, Kaufkraft, wirtschaftliche Alternativen, soziale Netzwerke, familiäre Abhängigkeiten, institutionelle Faktoren | Kontext (Detailmodule) | im Gedankenprozess berücksichtigt, im Kernmodell nicht aufgenommen (siehe Abschnitt 3) |
| Zielorte, Zuwanderung, Rückkehrmigration | weggelassen | ausserhalb des Fokus der Leitfrage |
| Konflikte, Politik, Wirtschaftskrisen | weggelassen | Kontext, nicht modelliert |

## **3. Cluster System Map**

![Cluster System Map](cluster_system_map.png)

Die Cluster System Map sammelt alle Faktoren, die zu Beginn als relevant betrachtet wurden, und ordnet sie in Themenbereiche.

### **Von der Cluster Map zur Causal Loop Map**

Alle Faktoren der Cluster Map sind in Teil 02 der Causal Loop Map (Detailmodule) enthalten. In das Kernmodell (Teil 01), das später in LE2 simuliert wird, wurden nur die folgenden aufgenommen:

| Faktor aus der Cluster Map | Im Kernmodell | Begründung |
|---|---|---|
| Niederschlag | übernommen (exogen) | Klimatreiber, direkt messbar |
| Dürre | nicht übernommen | Dürre ist zu wenig Niederschlag; beide Variablen würden denselben Effekt doppelt zählen |
| Temperatur, Bodenqualität | nicht übernommen | wirken über Wasserhaushalt bzw. sehr langsam; keine regionalen Daten |
| Anbaufläche, Wasserbedarf | nicht übernommen | Anbaufläche wird als konstant angenommen |
| Wasserverfügbarkeit, Ertrag, Produktion | übernommen | Kernkette der Leitfrage |
| Nahrungsmittelverfügbarkeit pro Person | übernommen | zeigt den Versorgungsdruck (Schleife B1) |
| Landwirtschaftliches Einkommen, Haushaltseinkommen | übernommen | |
| Lebensmittelpreise, Kaufkraft, wirtschaftliche Alternativen | nicht übernommen | hängen von externen Märkten ab; werden als konstant angenommen |
| Bevölkerung, verfügbare Arbeitskräfte, Abwanderung | übernommen | |
| Soziale Netzwerke | als «Abgewanderte Personen» übernommen | Netzwerke entstehen durch bereits Abgewanderte und sind so messbar (Schleife R2) |
| Rücküberweisungen | übernommen | Schleife B2 |
| Familiäre Abhängigkeiten | nicht übernommen | Wirkung uneindeutig (±), auf Ebene einzelner Haushalte |
| Institutionelle Faktoren (Unterstützung, Infrastruktur, Bewässerung usw.) | nicht übernommen | Hebel für Szenarien in LE4 |
| Konflikte, politische Veränderungen, wirtschaftliche Krisen | nicht übernommen | ausserhalb der Systemgrenze |

## **4. Stakeholder Map**

![Stakeholder Map](stakeholder_map.png)

Die erste Version liegt unter `archiv/stakeholder_map_v1.png`. Alle Inhalte sind unverändert übernommen; neu ist unten der Abschnitt «Einfluss und Betroffenheit».

### **Einfluss und Betroffenheit**

Eigene Einschätzung:

| Akteur | Einfluss auf das System | Betroffenheit | Rolle |
|---|---|---|---|
| Lokale Haushalte | tief | hoch | entscheiden über Abwanderung |
| Landwirtschaftliche Betriebe und Bauern | tief | hoch | tragen Ernteausfälle |
| Abwandernde Personen | mittel | hoch | senden Rücküberweisungen, erleichtern weitere Abwanderung |
| Zurückbleibende Familien | tief | hoch | verlieren Arbeitskräfte, erhalten Rücküberweisungen |
| Lokale Gemeinschaften | mittel | hoch | gegenseitige Hilfe |
| Lokale und regionale Behörden | mittel | mittel | setzen Massnahmen um |
| Nationale Regierung | hoch | tief | Rahmenbedingungen und Mittel (staatliche Unterstützung, Bewässerung) |
| Hilfs- und Entwicklungsorganisationen | mittel | tief | Ernährungssicherheit, Anpassung |
| Landwirtschaftliche Beratungsstellen | mittel | tief | Wissen zu Anbau und Wasser |
| Forschung und internationale Organisationen | tief | tief | Daten und Analysen |

Hoher Einfluss bei tiefer Betroffenheit (nationale Regierung, Hilfsorganisationen) heisst: Diese Akteure können Massnahmen finanzieren und umsetzen, tragen die Folgen aber nicht selbst. Sie sind die Adressaten der Szenarien in LE4.

## **5. Causal Loop Map**

![Causal Loop Map](causal_loop_map.png)

Die Karte besteht aus zwei Teilen: Teil 01 ist das Kernmodell, das in LE2 simuliert wird. Teil 02 zeigt alle Faktoren der Cluster Map als Detailmodule und dokumentiert den Gedankenprozess.

### **Änderungen gegenüber der ersten Version**

Die erste Version liegt unter `archiv/causal_loop_map_v1.png`. Teil 02 ist unverändert. Im Kernmodell wurde Folgendes angepasst:

| Änderung | Grund |
|---|---|
| Dürre entfernt, Niederschlag grau (exogen) | Dürre und Niederschlag zählten denselben Effekt doppelt |
| Ertrag → Produktion statt Ertrag → Einkommen | Ertrag (pro Hektar) wirkt über die Gesamtproduktion auf das Einkommen |
| Bevölkerung → Arbeitskräfte statt Abwanderung → Arbeitskräfte | Abwanderung wirkt über den Bestand der Bevölkerung |
| Neu: Abgewanderte Personen, Schleife R2 | Netzwerkeffekt der Migration |
| Rücküberweisungen über die Abgewanderten Personen (B2) | Geld schicken alle bereits Abgewanderten, nicht nur die neu Abwandernden |
| Neu: Nahrungsmittelverfügbarkeit pro Person, Schleife B1 | Rückwirkung der Abwanderung auf die Region |
| Verzögerungen (\|\|), Schleifen nummeriert, R1 als Hypothese | Transparenz und Vorbereitung für LE2 |

### **Schleifen**

| Schleife | Typ | Ablauf | Bedeutung |
|---|---|---|---|
| R1 Arbeitskräfte–Einkommen | verstärkend (Hypothese) | Abwanderung → Bevölkerung (−) → Arbeitskräfte (+) → Produktion (+) → landw. Einkommen (+) → Abwanderung (−) | Wer abwandert, fehlt als Arbeitskraft; die Produktion sinkt, und noch mehr Menschen wandern ab. |
| R2 Netzwerk | verstärkend, verzögert | Abwanderung → Abgewanderte Personen (+) → Abwanderung (+) | Bereits Abgewanderte erleichtern Nachfolgenden die Abwanderung. |
| B1 Versorgung | ausgleichend | Abwanderung → Bevölkerung (−) → Nahrungsmittelverfügbarkeit pro Person (−) → Abwanderung (−) | Weniger Menschen heisst mehr Nahrung pro Person; der Druck zur Abwanderung sinkt. |
| B2 Rücküberweisungen | ausgleichend, verzögert | Abwanderung → Abgewanderte Personen (+) → Rücküberweisungen (+) → Haushaltseinkommen (+) → Abwanderung (−) | Geld der Abgewanderten stützt die Haushalte; weniger weitere Abwanderung. |

R1 und B1 starten beide bei der sinkenden Bevölkerung, wirken aber in entgegengesetzte Richtung. Welche der beiden Schleifen überwiegt, ist eine Kernfrage für LE2.

### **Begründung der Wirkungen (Kernmodell)**

| Von | Nach | Wirkung | Begründung | Beleg |
|---|---|---|---|---|
| Niederschlag | Wasserverfügbarkeit | + | Landwirtschaft in Kaffrine ist fast ausschliesslich Regenfeldbau | Annahme |
| Wasserverfügbarkeit | Ertrag | + | Ertrag im Erdnussbecken hängt stark vom Niederschlag ab | Atmosphere (2024), Climate-Related Risks … Senegalese Groundnut Basin |
| Ertrag | Produktion | + | Produktion = Ertrag × Anbaufläche | Definition |
| Verfügbare Arbeitskräfte | Produktion | + | Weniger Arbeitskräfte, weniger bewirtschaftete Fläche | Annahme, siehe Hinweis 2 |
| Produktion | Landw. Einkommen | + | Verkauf, v.a. Erdnuss | Annahme |
| Landw. Einkommen | Abwanderung | − | Wirtschaftliche Not ist ein Hauptgrund für Abwanderung | Annahme, siehe Hinweis 1 |
| Rücküberweisungen | Haushaltseinkommen | + | Teil des Haushaltseinkommens | Definition |
| Haushaltseinkommen | Abwanderung | − | wie oben | Annahme, siehe Hinweis 1 |
| Abwanderung | Bevölkerung | − | Abfluss aus dem Bestand | Definition |
| Bevölkerung | Verfügbare Arbeitskräfte | + | Anteil im erwerbsfähigen Alter | Annahme |
| Bevölkerung | Nahrungsmittelverfügbarkeit pro Person | − | Gleiche Menge auf mehr Menschen verteilt | Definition |
| Nahrungsmittelverfügbarkeit pro Person | Abwanderung | − | Ernährungsunsicherheit erhöht den Druck zur Abwanderung | Annahme |
| Abwanderung | Abgewanderte Personen | + | Zufluss in den Bestand der Abgewanderten | Definition |
| Abgewanderte Personen | Rücküberweisungen | + (verzögert) | Abgewanderte unterstützen ihre Familien, sobald sie Einkommen haben | Lucas & Stark (1985) |
| Abgewanderte Personen | Abwanderung | + (verzögert) | Netzwerke senken Kosten und Risiko der Abwanderung | Massey (1990) |

### **Hinweise zur Interpretation**

1. **Einkommen und Abwanderung (Migration Hump):** Der Zusammenhang ist nicht immer negativ. Sehr arme Haushalte können sich die Abwanderung oft nicht leisten; steigt ihr Einkommen etwas, wandern sie zuerst sogar mehr ab (Cattaneo & Peri, 2016). Die Karte zeigt mit «−» den Normalfall. In LE2 wird das als vereinfachende Annahme deklariert.
2. **R1 ist eine Hypothese:** Im ländlichen Sahel gibt es oft mehr Arbeitskräfte als Arbeit. Ob Abwanderung die Produktion wirklich senkt, ist unsicher und wird in LE2 mit einer Sensitivitätsanalyse geprüft.

## **6. Ausblick auf LE2**

| Typ | Variablen |
|---|---|
| Stock (Bestand) | Bevölkerung, Abgewanderte Personen |
| Flow (Fluss) | Abwanderung, natürliches Bevölkerungswachstum |
| Converter (Hilfsgrösse) | Wasserverfügbarkeit, Ertrag, Produktion, Arbeitskräfte, landw. Einkommen, Haushaltseinkommen, Rücküberweisungen, Nahrungsmittelverfügbarkeit pro Person |
| Exogene Eingabe | Niederschlag (Zeitreihe) |

## **Dateien**

- Karten als Bild: `cluster_system_map.png`, `stakeholder_map.png`, `causal_loop_map.png`
- Quellen: `drawio/`. Causal Loop Map und Stakeholder Map werden mit `drawio/generate_maps.py` aus den Originalkarten (`archiv/*_v1.drawio`) erzeugt.
- Erste Versionen (v1) der Causal Loop Map und der Stakeholder Map: `archiv/`

## **Quellen**

- ANSD (2024): RGPH-5 2023, Rapport définitif, Chapitre 6 – Migrations.
- ANSD (2025): Situation économique et sociale de la région de Kaffrine 2022–2023.
- Cattaneo, C. & Peri, G. (2016): The migration response to increasing temperatures. Journal of Development Economics, 122, 127–146.
- Funk, C. et al. (2015): The climate hazards infrared precipitation with stations (CHIRPS). Scientific Data, 2, 150066.
- Lucas, R. E. B. & Stark, O. (1985): Motivations to Remit: Evidence from Botswana. Journal of Political Economy, 93(5), 901–918.
- Massey, D. S. (1990): Social Structure, Household Strategies, and the Cumulative Causation of Migration. Population Index, 56(1), 3–26.
- Atmosphere (2024): Climate-Related Risks and Agricultural Yield Assessment in the Senegalese Groundnut Basin. Atmosphere, 15(10), 1246.

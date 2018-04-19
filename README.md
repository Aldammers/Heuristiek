# Heuristiek
Authors:

- Stan Rozing
- Jan Marten
- Alexander Dammers 10528415

Algoritmes voor Proteinfolding

Random algoritme
Bouwt een random eiwit op de grid voor een aantal iteraties. De hoeveelheid iteraties moet van te voren worden aangegeven. Berekent de waarde van de verbindingen van het totale eiwit.
De meest waardevolle van de eiwitten (meest negatieve) wordt gereturned.0

Greedy algoritme
Kijkt voor elke positie waar het eiwit begint wat de optimale positie van de Htjes en Ptjes zijn voor een zo laag mogelijke score.
Probleem: De eerste stappen mogen dan wel voor de hoogste negatieve waarde zorgen. Dit is geen garantie dat het voor de totale hoogste negatieve waarde zorgt. 
Probleem: Eerste stap is altijd rechtdoor, en daarmee ook de tweede, derde etc

Brute algoritme
Begin met een positie van het eerste aminozuur op de grid. En voegt een mogelijke aanpassing toe indien mogelijk, dus een Htje of een Ptje toevoegen. Doe dat totdat het doel is bereikt, de eiwitketen dus compleet is. Lijkt op het random algorithm. 


Hillclimber algoritme
Bekijk alle richtingen van het aminozuur en kies de richting met een waarde voor het eiwit. Dan kijkt het algoritme of er een richting is die beter is dan de huidige staat, zonder overlap. Hoogste waarde wordt hiermee dus de hoogste negatieve waarde die toegevoegd kan worden. 
Probleem: Eerste stap is altijd rechtdoor, tweede stap ook etc ect. Misschien random aspect toevoegen aan algoritme?

Expanding Universe algoritme?

Combineren van Hillclimber met een random aspect er in?

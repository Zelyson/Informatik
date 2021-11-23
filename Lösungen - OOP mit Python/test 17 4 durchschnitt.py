from kartenspiel import Kartenstapel, Kartenhaufen
# Testprogramm
kartenstapel = Kartenstapel()
kartenstapel.mischen()
kartenhaufenSpieler1 = Kartenhaufen()
gewonnen=0
groeser21=0
kleiner21=0
runde=0
while runde!= 1000:
    while kartenhaufenSpieler1.wert < 18:
        karte = kartenstapel.karteZiehen()
        kartenhaufenSpieler1.hinzufuegen(karte)
    if kartenhaufenSpieler1.wert == 21:
        gewonnen= gewonnen +1 
    elif kartenhaufenSpieler1.wert > 21:
        groeser21=groeser21 +1
    elif kartenhaufenSpieler1.wert < 21:
        kleiner21=kleiner21 +1
    runde= runde+1
    kartenstapel = Kartenstapel()
    kartenstapel.mischen()
    kartenhaufenSpieler1 = Kartenhaufen()        
print("gewonnen:",gewonnen,", größer21:",groeser21,", kleiner21:",kleiner21)
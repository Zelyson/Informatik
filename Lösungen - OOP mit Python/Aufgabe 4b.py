from kartenspiel import Kartenstapel, Kartenhaufen
kartenstapel = Kartenstapel()
kartenstapel.mischen()
kartenhaufenSpieler1 = Kartenhaufen()
kartenhaufenSpieler2 = Kartenhaufen()
zaehler = 0
print('Spieler 1:')
print()

kartenhaufenSpieler1.hinzufuegen(karte)
while kartenhaufenSpieler1.wert < 18:
    zaehler = zaehler + 1
    karte = kartenstapel.karteZiehen()
    print("Karte", zaehler,":")
    print(karte)
    print(kartenhaufenSpieler1.wert)
    print()
    kartenhaufenSpieler1.hinzufuegen(karte)
zaehler = zaehler + 1
print("Karte", zaehler,":")
print(karte)
print(kartenhaufenSpieler1.wert)
print()
zaehler = 0
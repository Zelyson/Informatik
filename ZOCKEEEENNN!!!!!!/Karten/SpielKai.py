from typing import Counter
from kartenspiel import *

stapel = Kartenstapel()
stapel.mischen()
spieler1 = Kartenhaufen()

while spieler1.wert <= 18:
    spieler1.hinzufuegen(stapel.karteZiehen())
    if spieler1.wert > 21:
        print("Verloren :(", spieler1.wert)
        exit()
print("Gewonnen!!", spieler1.wert)

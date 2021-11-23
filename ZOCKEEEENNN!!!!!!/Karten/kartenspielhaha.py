from typing import Counter
from kartenspiel import *

stapel = Kartenstapel()
stapel.mischen()
spieler1 = Kartenhaufen()
spieler2 = Kartenhaufen()

jesNo = ""
ctr = 0

while ctr < 2:
    # Player 1
    jesNo = input("Spieler1: Karte ziehen (J/N)? ")
    if jesNo == "j":
        spieler1.hinzufuegen(stapel.karteZiehen())
        print(spieler1.wert)
        if spieler1.wert > 21:
            print("Spieler 2 hat gewonnen!!!!!!", spieler2.wert)
            exit()
    else:
        ctr += 1
        if ctr > 1:
            break

    # Player 2
    jesNo = input("Spieler2: Karte ziehen (J/N)? ")
    if jesNo == "j":
        spieler2.hinzufuegen(stapel.karteZiehen())
        print(spieler2.wert)
        if spieler2.wert > 21:
            print("Spieler 1 hat gewonnen!!!!!!", spieler1.wert)
            exit()
    else:
        ctr += 1

if spieler1.wert > spieler2.wert:
    print("Spieler 1 hat gewonnen!!!!!!", spieler1.wert)
elif spieler2.wert > spieler1.wert:
    print("Spieler 2 hat gewonnen!!!!!!", spieler2.wert)
else:
    print("Gleichstand ihr langweiler :(", spieler1.wert)

from kartenspiel import Kartenstapel, Kartenhaufen
# 2 Spieler
kartenstapel = Kartenstapel()
kartenstapel.mischen()
kartenhaufenSpieler1 = Kartenhaufen()
kartenhaufenSpieler2 = Kartenhaufen()
print('Spieler 1:')
karte = kartenstapel.karteZiehen()
print(karte)
kartenhaufenSpieler1.hinzufuegen(karte)
print(kartenhaufenSpieler1.wert)
print()
print('Spieler 2:')
karte = kartenstapel.karteZiehen()
print(karte)
kartenhaufenSpieler2.hinzufuegen(karte)
print(kartenhaufenSpieler2.wert)
print()
Spieler1fertig=False
Spieler2fertig=False
while Spieler1fertig==False or Spieler2fertig==False:
    if Spieler1fertig==False:
        print('Will Spieler 1 noch eine? Dein Wert ist derzeitig:',kartenhaufenSpieler1.wert)
        x=input('ja/nein: ')
        if x == 'ja' and Spieler1fertig==False:
            karte = kartenstapel.karteZiehen()
            print(karte)
            kartenhaufenSpieler1.hinzufuegen(karte)
            print(kartenhaufenSpieler1.wert)
            print()
            if kartenhaufenSpieler1.wert > 21:
                Spieler1fertig=True
                print('BUST')
                print()
        else:
            Spieler1fertig=True
            print('ok')
            print()
    if Spieler2fertig==False:
        print('Will Spieler 2 noch eine? Dein Wert ist derzeitig:',kartenhaufenSpieler2.wert)
        x=input('ja/nein: ')
        if x == 'ja':
            karte = kartenstapel.karteZiehen()
            print(karte)
            kartenhaufenSpieler2.hinzufuegen(karte)
            print(kartenhaufenSpieler2.wert)
            print()
            if kartenhaufenSpieler2.wert > 21:
                Spieler2fertig=True
                print('BUST')
                print()
        else:
            Spieler2fertig=True
            print('ok')
            print()
if kartenhaufenSpieler1.wert > kartenhaufenSpieler2.wert and kartenhaufenSpieler1.wert < 22:
    print('Spieler 1 hat gwonne')
if kartenhaufenSpieler2.wert > kartenhaufenSpieler1.wert and kartenhaufenSpieler2.wert < 22:
    print('Spieler 2 hat gwonne')
if kartenhaufenSpieler2.wert == kartenhaufenSpieler1.wert and kartenhaufenSpieler2.wert < 22 and kartenhaufenSpieler1.wert < 22:
    print('unentschide')
if kartenhaufenSpieler2.wert > 21 and kartenhaufenSpieler1.wert < 22:
    print('Spieler 1 hat gwonne')
if kartenhaufenSpieler1.wert > 21 and kartenhaufenSpieler2.wert < 22:
    print('Spieler 2 hat gwonne')
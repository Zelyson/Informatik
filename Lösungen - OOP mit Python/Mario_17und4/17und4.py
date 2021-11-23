# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 08:16:19 2021

@author: Schweikert.Mar
"""


from kartenspiel import Kartenstapel, Kartenhaufen
# Testprogrammn

spielerAnzahl=5


kartenstapel = Kartenstapel()
kartenstapel.mischen()

kartenhaufen=[]
Name=[]
fertig=[]
for i in range(spielerAnzahl):
    kartenhaufen.append(Kartenhaufen())
    Name.append("Spieler-"+str(i))
    fertig.append(False)

spielFertig=False

while not spielFertig:
    for i in range(spielerAnzahl):
        if kartenstapel.istLeer():
            kartenstapel = Kartenstapel()
            kartenstapel.mischen()
            
        if not fertig[i]:
            kartenhaufenSpieler=kartenhaufen[i]
            NameSpieler=Name[i]
            print(NameSpieler+":")
            antwort=str(input("Willst du eine Karte? (y/n) Dein Zahlenwert ist: "+str(kartenhaufen[i].wert)+"\n"))
            if antwort=="y" or antwort=="j":        
                karte = kartenstapel.karteZiehen()
                kartenhaufenSpieler.hinzufuegen(karte)
                print("Deine Karte ist ", karte," und dein neuer Zahlenwert ist:", kartenhaufenSpieler.wert,"\n\n\n")
            else:
                fertig[i]=True
            if kartenhaufenSpieler.wert>21:
                fertig[i]=True
        
        if not (False in fertig):
            spielFertig=True
            break
        


print("\n\nSpiel Ende - Finale Aufstellung\n\n")


werte=[]
for i in range(spielerAnzahl):
    if kartenhaufen[i].wert>21:
        print(Name[i]+" ist bust!")
        werte.append(-1)
    else:
        print("Kartenwert ",Name[i],":", str(kartenhaufen[i].wert))
        werte.append(kartenhaufen[i].wert)

SpielerGewonnen=Name[werte.index(max(werte))]

print("\nSpieler ", SpielerGewonnen, "hat gewonnen.")


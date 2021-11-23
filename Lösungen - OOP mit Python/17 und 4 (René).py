from kartenspiel import Kartenstapel, Kartenhaufen

# Festlegung von Variablen
stapel = Kartenstapel()
stapel.mischen()
S1 = Kartenhaufen()
S2 = Kartenhaufen()
S3 = Kartenhaufen()
S4 = Kartenhaufen()
SL = [S1, S2, S3, S4]
K1 = ""
K2 = ""
K3 = ""
K4 = ""
KL = [K1, K2, K3, K4]
raus = []

# Funktion zu Ja|Nein Fragen
def eingabeWert():
    JN = ["ja","Ja","JA","nein","Nein","NEIN"]
    e = input("[Ja|Nein]  ")
    while not e in JN:
        print("FEHLER! Bitte auf die möglichen Eingaben achten")
        e = input("[Ja|Nein]  ")
    if e in JN[0:3]:
        e = True
    else:
        e = False
    return e

# Einstellungen
print("--------- 17 und 4 ---------")
print()
print("Anzahl der Spieler?")
S = int(input("[1|2|3|4]  "))
while not 1 <= S <= 4:
    print("FEHLER! Bitte auf die möglichen Eingaben achten")
    S = int(input("[1|2|3|4]  "))
print()
print("Mit Ass-Sonderregel spielen? (Zwei Asse als 1. und 2. gezogene Karte ergeben 21 statt 22)")
A = eingabeWert()
print()

# Hauptspiel
print("----------------------------")
print()
print("GAME START!")
print()
for i in range(0,S):
    print("Spieler", i+1)
    karte = stapel.karteZiehen()
    KL[i] = KL[i] + karte
    SL[i].hinzufuegen(karte)
    print(KL[i]," (",SL[i].wert,")")
    print()
while len(raus) != S and stapel.istLeer() == False:
    print()
    for i in range(0,S):
        if not i in raus and stapel.istLeer() == False:
            print("Spieler", i+1, "- Karte ziehen?")
            Z = eingabeWert()
            print("--------------------------")
            if Z == True:
                karte = stapel.karteZiehen()
                KL[i] = KL[i] + " | " + karte
                SL[i].hinzufuegen(karte)
                print(KL[i]," (",SL[i].wert,")")
                if SL[i].wert > 21:
                    raus = raus + [i]
                    if A == True and len(SL[i].kartenListe) == 2:
                        SL[i].wert = SL[i].wert - 1
                        print("Glück im Unglück! Dein Kartenwert beträgt somit 21 statt 22")
                    else:
                        print("Über 21 hinausgeschossen, Spieler", i+1, "ist raus!")
            else:
                raus = raus + [i]
                print("Spieler", i+1, "ist ausgestiegen")
            print()

# Ergebnisse
print("----------------------------")
print()
if S == 1:
    if S1.wert > 21:
        print("GAME OVER!")
    else:
        print("Ergebnis  - ", S1.wert,"  ",KL[0])
else:
    print("Ergebnisse!")
    for i in range(0,S):
        if SL[i].wert > 21:
            print("Spieler",i+1," -  DSQ. ",KL[i])
        else:
            print("Spieler",i+1," - ",SL[i].wert,"  ",KL[i])
            

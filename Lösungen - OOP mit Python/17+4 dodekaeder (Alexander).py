from wuerfel import Dodekaederwuerfel
d = Dodekaederwuerfel()
zaehler = 0
spielen = True
while d.wert<22 and spielen == True:
    eingabe = input("möchten Sie eine Karte ziehen?")
    if eingabe == "ja":
        d.werfen()
        d.hinzufuegen(d.augen)
        zaehler = zaehler + 1
        print("Sie haben",zaehler, "mal gewürfelt und die Augenzahl",d.wert)
    else:
        spielen = False
        print("Spiel beendet. Ihre Augenzahl beträgt",d.wert,".")
if d.wert > 21:
    print()
    print("21 überschritten. game over.")
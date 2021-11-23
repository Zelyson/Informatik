from ZählerMitObergrenze import Zaehler
import time

# Sekundenzähler

# Zähler definieren
zaehler = Zaehler()
zaehler.grenze = 60

# Zufällige Schleife zum testen
for i in range(0, 100):

    # Wenn der Zähler 60 zeigt, soll er zurückgesetzt werden
    if (zaehler.stand == 61):
        zaehler.nullSetzen()

    # Stand ausgeben
    print("Stand:", zaehler.stand)

    # Timer, damit nur einmal in der Sekunde erhöht wird
    time.sleep(1)

    # Zähler erhöhen
    zaehler.weiterZaehlen()
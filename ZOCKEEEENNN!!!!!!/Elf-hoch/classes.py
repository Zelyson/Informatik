from random import randint


class Spieler(object):
    def __init__(self) -> None:
        self.name = NameError
        self.marken = 0
        self.verloren = 0

    def getMarken(self):
        return self.marken

    def markenEinzahlen(self, rein):
        self.marken += rein

    def markenAuszahlen(self, raus):
        self.marken -= raus

        if self.marken == 0 or self.marken < 0:
            self.verloren = 1


# -----------------------------------------------------------
# Würfel
# -----------------------------------------------------------
class Wuerfel(object):

    nn = 6

    def __init__(self):
        """
        Die Methode __init__ erzeugt ein Wuerfel-Objekt.
        Die Augenzahl wird dabei auf eine Zufallszahl aus
        dem Bereich 1..6 gesetzt.
        """

        self.augen = randint(1, self.nn)

    def werfen(self):
        """
        Die Methode werfen erzeugt eine neue Augenzahl
        als Zufallszahl aus dem Bereich 1..6.
        """

        self.augen = randint(1, self.nn)

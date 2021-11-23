from random import randint

class Dodekaederwuerfel(object):

    def __init__(self):

        """
        Die Methode __init__ erzeugt ein Wuerfel-Objekt.
        Die Augenzahl wird dabei auf eine Zufallszahl aus
        dem Bereich 1..6 gesetzt.
        """

        self.augen = randint(1, 12)
        self.wert = 0

    def werfen(self):

        """
        Die Methode werfen erzeugt eine neue Augenzahl
        als Zufallszahl aus dem Bereich 1..6.
        """
        
        self.augen = randint(1, 12)
    
    def hinzufuegen(self, augen):
        self.wert = self.wert + self.augen
        

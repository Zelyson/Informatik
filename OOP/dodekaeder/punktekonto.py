class Kartenhand(object):
    def __init__(self):
        self.kartenListe = []
        self.anzahl = 0

    def hinzufuegen(self, karte):
        self.kartenListe = self.kartenListe + [karte]
        self.anzahl = self.anzahl + 1

    def wegnehmen(self, karte):
        if karte in self.kartenListe:
            i = self.kartenListe.index(karte)
            del self.kartenListe[i]
            self.anzahl = self.anzahl - 1


from pynput.keyboard import Key, Controller

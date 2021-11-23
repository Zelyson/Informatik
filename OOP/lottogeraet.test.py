from lottogeraet import Lottogeraet

der_gerät = Lottogeraet()
winCounter = 0
guesses = []
winningNun = []
sims = int(input("Durchgänge: "))


def prntList(list):
    for i in list:
        print(i)


def test():
    try:
        der_gerät.geraetVorbereiten()
        der_gerät.kugelZiehen()
        der_gerät.ziehungDurchfuehren()
        print("Vorhandene Kugeln: " + str(der_gerät.getVorhandeneKugeln()))
        print("Gezogene Kugeln: " + str(der_gerät.getGezogeneKugeln()))
        print("\n\nDer Test war erfolgreich!")
    except:
        print("Es ist ein Fehler aufgetreten. Bitte versuche es später erneut.")


for i in range(0, 6):
    guesse = int(input("Gib Zahlen ein: "))
    guesses.append(guesse)

for i in range(0, sims):

    der_gerät.geraetVorbereiten()
    der_gerät.ziehungDurchfuehren()
    winningNun = der_gerät.getGezogeneKugeln()

    for i in guesses:
        if i in winningNun:
            winCounter += 1
        if winCounter == 6:
            print(str(winCounter))
            break
    winCounter = 0


class mecka():
    def __init__(self) -> None:
        self.mekka = "das ist ein Kuchen hahahahaha"

    def out(self):
        print(self.mekka)

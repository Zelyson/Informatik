class konto(object):
    def __init__(self, name) -> None:
        self.__name = name
        self.__punkte = 0

    def punkte_add(self, numPlus):
        self.__punkte += numPlus

    def punkte_sub(self, numMinus):
        self.__punkte -= numMinus


spieler = {}

for i in range(0, 10):
    spieler[i] = konto(str(i))

for spieler, konto in spieler.items():
    konto.punkte_add(20)
    print(konto.punkte)

for spieler, konto in spieler.items():
    konto.punkte_sub(1)
    print(konto.punkte)

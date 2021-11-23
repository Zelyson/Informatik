modulo = int(input("modulo: "))
pubKeyBase = int(input("pubKeyBase: "))
pubKeyExp = int(input("pubKeyExp: "))
pot = 1
plainTepubKeyBaset = str(input("Wort: "))


while pubKeyExp > 0:
    if pubKeyExp % modulo != modulo:
        pot = (pot * pubKeyBase) % modulo
        pubKeyExp = pubKeyExp - 1
    else:
        pubKeyBase = (pubKeyBase * pubKeyBase) % modulo
        pubKeyExp = pubKeyExp // modulo

print(pot)

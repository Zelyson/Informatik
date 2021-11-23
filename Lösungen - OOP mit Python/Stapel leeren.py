from kartenstapel import Kartenstapel

# Stapel lehren
stapel = Kartenstapel()

print('Karten werden gemischt...')
print()
stapel.mischen()
print('Karten gemischt!')
print()

while stapel.istLeer() == False:
    gezogeneKarte = stapel.karteZiehen()
    print(gezogeneKarte)

print()
print('Stapel leer =', stapel.istLeer())


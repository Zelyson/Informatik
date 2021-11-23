from wuerfel import Wuerfel
w1 = Wuerfel()
w2 = Wuerfel()
w3 = Wuerfel()
while w1.augen != 6:
    w1.werfen()
while w2.augen != 6:
    w2.werfen()
while w3.augen != 6:
    w3.werfen()
print(w1.augen)
print(w2.augen)
print(w3.augen)
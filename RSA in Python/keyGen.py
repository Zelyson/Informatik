import random

def pubKey(p,q):
    n = p * q
    phi = (p - 1) + (q - 1)
    e = random.randrange(1,phi)

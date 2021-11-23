import time


class zahler:
    def __init__(self) -> None:
        self.stand = 0
        self.obergrenze = 60

    def eins_hoch(self):
        self.stand += 1

    def set_zero(self):
        self.stand = 0

    def eins_hoch_print(self):
        self.stand += 1
        print(self.stand)


zapzap = zahler()

while True:
    zapzap.eins_hoch_print()
    time.sleep(0)
    if zapzap.stand == zapzap.obergrenze:
        break

print("Du sohn :D")

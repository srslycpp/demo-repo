class Calculator():

    def __init__(self):
        self.ostatni_wynik = 0

    def dodaj(self, a, b):
        wynik = a+b


    def odejmij(self, a, b):
        wynik = a-b
        print(wynik)


calc = Calculator()
print(calc.dodaj(4,11))


calc.odejmij(13,6)
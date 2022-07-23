class Człowiek:
    imie = "sebastian"

    def przedstawsie(self):
        return "czesc, mam na imie " + self.imie

   
obiekt = Człowiek()
print(obiekt.przedstawsie())

obiekt2 = Człowiek()
obiekt2.imie = "zenek"
print(obiekt2.przedstawsie())
    
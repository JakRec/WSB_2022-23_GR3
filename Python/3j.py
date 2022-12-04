class Zwierze():
    def glos(self):
        return "ja mowie!"

class Malpa(Zwierze):
    def glos(self):
        return "uauaua!"
        

class Kon(Zwierze):
    def glos(self):
        return "ihaahaa"

class Pies(Malpa, Kon):
    pass

class Kot(Kon, Malpa):
    pass


# print(Pies.mro())

pi = Pies()
ko = Kot()
on = Kon()
ma = Malpa()

print(pi.glos())
print(ko.glos())
print(on.glos())
print(ma.glos())
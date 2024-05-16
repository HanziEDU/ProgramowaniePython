class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Elektryczny(Samochod):
    def __init__(self, marka, model, zasieg_na_ladowaniu):
        super().__init__(marka, model)
        self.zasieg_na_ladowaniu = zasieg_na_ladowaniu

class Sportowy(Samochod):
    def __init__(self, marka, model, maksymalna_predkosc):
        super().__init__(marka, model)
        self.maksymalna_predkosc = maksymalna_predkosc

class ElektrycznySportowy(Elektryczny, Sportowy):
    def __init__(self, marka, model, zasieg_na_ladowaniu, maksymalna_predkosc):
        Elektryczny.__init__(self, marka, model, zasieg_na_ladowaniu)
        Sportowy.__init__(self, marka, model, maksymalna_predkosc)

elektro_sportowy = ElektrycznySportowy("Tesla", "Model S", 500, 250)
print("Marka:", elektro_sportowy.marka)
print("Model:", elektro_sportowy.model)
print("Zasięg na jednym ładowaniu:", elektro_sportowy.zasieg_na_ladowaniu)
print("Maksymalna prędkość:", elektro_sportowy.maksymalna_predkosc)
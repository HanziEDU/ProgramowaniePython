# %% Zadanie 3: Projektowanie klas DamainWilk3
#a
class Pracownik:
    def __init__(self, imie, stanowisko, pensja):
        self.imie = imie
        self.stanowisko = stanowisko
        self.pensja = pensja

    def awansuj(self, nowe_stanowisko, nowa_pensja):
        self.stanowisko = nowe_stanowisko
        self.pensja = nowa_pensja

    def wyswietl_informacje(self):
        print(f"\nImię: {self.imie}, Stanowisko: {self.stanowisko}, Pensja: {self.pensja}")

#b
class Potwor:
    def __init__(self, nazwa, zdrowie, obrazenia):
        self.nazwa = nazwa
        self.zdrowie = zdrowie
        self.obrazenia = obrazenia

    def atak(self, cel):
        print(f"{self.nazwa} atakuje {cel.nazwa} z obrażeniami {self.obrazenia}")
        cel.otrzymaj_obrazenia(self.obrazenia)

    def otrzymaj_obrazenia(self, ilosc):
        self.zdrowie -= ilosc
        if self.zdrowie <= 0:
            print(f"{self.nazwa} został pokonany!")
        else:
            print(f"{self.nazwa} ma jeszcze {self.zdrowie} punktów życia")

#c
class Lodowka:
    def __init__(self, marka, pojemnosc):
        self.marka = marka
        self.pojemnosc = pojemnosc
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def usun_przedmiot(self, przedmiot):
        if przedmiot in self.przedmioty:
            self.przedmioty.remove(przedmiot)
            print(f"\n{przedmiot} został usunięty z lodówki")
        else:
            print(f"\n{przedmiot} nie znaleziono w lodówce")

    def wyswietl_zawartosc(self):
        print(f"\nMarka lodówki: {self.marka}, Pojemność: {self.pojemnosc}")
        print("Przedmioty w lodówce:")
        for przedmiot in self.przedmioty:
            print(przedmiot)
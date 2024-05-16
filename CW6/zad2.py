class BankAccount:
    def __init__(self, numer, waluta, saldo, wlasciciel):
        self.numer = numer
        self.waluta = waluta
        self.__saldo = saldo
        self.__wlasciciel = wlasciciel

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, value):
        self.__saldo = value

    def get_wlasciciel(self):
        return self.__wlasciciel

    def set_wlasciciel(self, value):
        self.__wlasciciel = value

    def __str__(self):
        return f"Konto {self.numer} należy do {self.__wlasciciel} i ma saldo {self.__saldo} {self.waluta}"

    def __len__(self):
        return self.__saldo

    def __add__(self, other):
        if (self.numer == other.numer) and (self.waluta == other.waluta) and (self.__wlasciciel == other.__wlasciciel):
            new_balance = self.__saldo + other.get_saldo()
            return new_balance
        else:
            raise ValueError("Nie można dodać konta - różne numery, waluty lub właściciele")

konto1 = BankAccount(123456, "PLN", 1000, "Jan Kowalski")
konto2 = BankAccount(654321, "PLN", 2000, "Anna Nowak")

print(konto1)
print(konto2)
print("Długość konta 1:", len(konto1))
print("Długość konta 2:", len(konto2))

try:
    konto3 = konto1 + konto2
    print("Nowe saldo po dodaniu:", konto3)
except ValueError as e:
    print(e)
class BankAccount:
    def __init__(self, numer, waluta, saldo, wlasciciel):
        self.numer = numer
        self.waluta = waluta
        self.__saldo = saldo
        self.__wlasciciel = wlasciciel

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    @property
    def wlasciciel(self):
        return self.__wlasciciel

    @wlasciciel.setter
    def wlasciciel(self, value):
        self.__wlasciciel = value

    @staticmethod
    def convert_currency(amount, exchange_rate):
        return amount * exchange_rate
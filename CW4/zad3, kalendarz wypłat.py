import datetime
import calendar
import holidays
def czy_dzien_roboczy(data):
    return data.weekday() < 5
def ostatni_dzien_roboczy(miesiac, rok):
    ostatni_dzien = calendar.monthrange(rok, miesiac)[1]
    ostatni_dzien_data = datetime.date(rok, miesiac, ostatni_dzien)
    while not czy_dzien_roboczy(ostatni_dzien_data) or czy_swieto(ostatni_dzien_data):
        ostatni_dzien -= 1
        ostatni_dzien_data = datetime.date(rok, miesiac, ostatni_dzien)
    return ostatni_dzien_data

def nazwa_miesiaca(miesiac):
    return calendar.month_name[miesiac]

def czy_swieto(data):
    polskie_swieta = holidays.Poland()
    return data in polskie_swieta

rok = int(input("Podaj rok: "))

for miesiac in range(1, 13):
    ostatni_dzien = ostatni_dzien_roboczy(miesiac, rok)
    print(f"{nazwa_miesiaca(miesiac)}: {ostatni_dzien.strftime('%d-%m-%Y')}")


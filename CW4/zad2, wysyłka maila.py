import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def odczytaj_plik(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        return plik.read()

adres_serwera = input("Podaj adres serwera SMTP: ")
port = input("Podaj port serwera SMTP: ")
nazwa_uzytkownika = input("Podaj nazwę użytkownika: ")
haslo = input("Podaj hasło: ")
nadawca = input("Podaj adres e-mail nadawcy: ")
odbiorca = input("Podaj adres e-mail odbiorcy: ")
tytul = input("Podaj tytuł wiadomości: ")
nazwa_pliku = input("Podaj nazwę pliku do odczytu: ")

tresc = odczytaj_plik(nazwa_pliku)

wiadomosc = MIMEMultipart()
wiadomosc["From"] = nadawca
wiadomosc["To"] = odbiorca
wiadomosc["Subject"] = tytul

wiadomosc.attach(MIMEText(tresc, "plain"))

try:
    serwer_smtp = smtplib.SMTP(adres_serwera, port)
    serwer_smtp.starttls()
    serwer_smtp.login(nazwa_uzytkownika, haslo)
    serwer_smtp.sendmail(nadawca, odbiorca, wiadomosc.as_string())
    serwer_smtp.quit()
    print("Wiadomość została wysłana pomyślnie.")
except Exception as e:
    print(f"Wystąpił błąd podczas wysyłania wiadomości: {e}")

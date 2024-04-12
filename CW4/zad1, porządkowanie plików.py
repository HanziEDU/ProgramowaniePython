import os
import shutil

katalog_bazowy = "ścieżka/do/katalogu/bazowego"

sciezka_kopii = os.path.join(katalog_bazowy, "kopie")
if not os.path.exists(sciezka_kopii):
    os.makedirs(sciezka_kopii)

def skopiuj_zdjecia(sciezka_folderu, nazwa_folderu):
    pliki_zdjec = [plik for plik in os.listdir(sciezka_folderu)
                   if plik.lower().endswith(('.jpg', '.png'))]
    for indeks, plik in enumerate(pliki_zdjec):
        nowa_nazwa = f"{nazwa_folderu}_{indeks}.{plik.split('.')[-1].lower()}"
        shutil.copy2(os.path.join(sciezka_folderu, plik),
                     os.path.join(sciezka_kopii, nowa_nazwa))

raport = ""

for folder, _, pliki in os.walk(katalog_bazowy):
    if folder != sciezka_kopii:
        raport += f"\n\n{folder}:\n"
        skopiuj_zdjecia(folder, os.path.basename(folder))
        for plik in pliki:
            raport += f"{plik}\n"

with open(os.path.join(katalog_bazowy, "raport.txt"), "w") as file:
    file.write(raport)

print("Operacja zakończona. Sprawdź plik raportu.")

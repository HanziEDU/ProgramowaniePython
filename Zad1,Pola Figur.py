figury = ["prostokąt", "trapez", "koło", "trójkąt", "deltoid"]
print(figury)
wybrana_figura = input("Wybierz pole figury spośród dostępnych {}: ")

if wybrana_figura not in figury:
    print("Podana figura nie znajduje się na liście.")
else:
    parametry_input = input("Podaj parametry figury (oddzielone spacją): ")
    parametry = parametry_input.split()

    if len(parametry) != 2 and wybrana_figura != "koło":
        print("Nieprawidłowa liczba parametrów.")
    elif len(parametry) != 1 and wybrana_figura == "koło":
        print("Nieprawidłowa liczba parametrów.")
    else:
        if any(float(param) <= 0 for param in parametry):
            print("Wartości parametrów muszą być dodatnie.")
        else:
            if wybrana_figura == "prostokąt":
                pole = float(parametry[0]) * float(parametry[1])
            elif wybrana_figura == "trapez":
                pole = 0.5 * (float(parametry[0]) + float(parametry[1])) * float(parametry[2])
            elif wybrana_figura == "koło":
                pole = 3.14 * (float(parametry[0]) ** 2)
            elif wybrana_figura == "trójkąt":
                pole = 0.5 * float(parametry[0]) * float(parametry[1])
            elif wybrana_figura == "deltoid":
                pole = 0.5 * float(parametry[0]) * float(parametry[1])

            print("Pole figury", wybrana_figura, "to:", pole)

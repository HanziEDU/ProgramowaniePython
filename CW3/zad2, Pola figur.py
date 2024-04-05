import math
def square_area(side):
    return side * side

def rectangle_area(side_a, side_b):
    return side_a * side_b

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def calculate_area_of_figure():
    while True:
        figure = input("Wybierz figurę (square, rectangle, circle, triangle): ").lower()

        if figure == "stop":
            print("Koniec programu.")
            break

        if figure not in ["square", "rectangle", "circle", "triangle"]:
            print("Nieznana figura. Spróbuj ponownie.")
            continue

        if figure == "square":
            side = float(input("Podaj długość boku: "))
            print(f"Pole kwadratu wynosi: {square_area(side)}")
        elif figure == "rectangle":
            side_a = float(input("Podaj długość boku a: "))
            side_b = float(input("Podaj długość boku b: "))
            print(f"Pole prostokąta wynosi: {rectangle_area(side_a, side_b)}")
        elif figure == "circle":
            radius = float(input("Podaj promień koła: "))
            print(f"Pole koła wynosi: {circle_area(radius)}")
        elif figure == "triangle":
            base = float(input("Podaj długość podstawy: "))
            height = float(input("Podaj wysokość: "))
            print(f"Pole trójkąta wynosi:{triangle_area(base, height)}")

calculate_area_of_figure()
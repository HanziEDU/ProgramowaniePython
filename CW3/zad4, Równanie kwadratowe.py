import math
def quadratic_equation(a, b, c):
    if a == 0:
        print("Rownanie nie ma rozwiązań")
    else:
        delta = b**2 - 4 * a * c
        if delta > 0:
             x1 = (-b - math.sqrt(delta)) / (2 * a)
             x2 = (-b + math.sqrt(delta)) / (2 * a)
             return x1, x2
        elif delta == 0:
              x0 = -(b / 2 * a)
              return x0
        elif delta < 0:
               print("Nie posiada rozwiązań")

a = int(input('podaj a: '))
b = int(input('podaj b: '))
c = int(input('podaj c: '))

print(quadratic_equation(a, b, c))
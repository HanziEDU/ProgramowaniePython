import math
def Heron(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        print("Podany trójkąt nie istnieje")
        return None

a = float(input('podaj a: '))
b = float(input('podaj b: '))
c = float(input('podaj c: '))


print(Heron(a, b, c))
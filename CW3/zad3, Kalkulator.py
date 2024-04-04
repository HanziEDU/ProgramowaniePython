def addition(a, b):
    print(a + b)
def subtraction(a, b):
    return a - b
def division(a, b):
    if b < 0.0000001:
        return 'Nie dziel przez 0!'
    else:
        return a / b
def multiplication(a, b):
    return a * b


user = input('Napisz jakie działanie chcesz wykonać z list (+,-,/,*)')
a = float(input('podaj a: '))
b = float(input('podaj b: '))

if user == '+':
    print(addition(a, b))
elif user == '-':
    print(subtraction(a, b))
elif user == '/':
    print(division(a, b))
elif user == '*':
    print(multiplication(a, b))


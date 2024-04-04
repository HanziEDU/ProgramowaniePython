def simple_cash():
    products_input = input("Wprowadź produkty oddzielone przecinkami: ")
    products = set(products_input.split(','))
    prices = {}

    for product in products:
        price = input(f"Podaj cenę dla {product}: ")
        prices[product] = price

    print("Rachunek:")
    for product, price in prices.items():
        print(f"{product}: {price}")

simple_cash()

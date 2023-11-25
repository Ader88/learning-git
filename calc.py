import logging

logging.basicConfig(level=logging.INFO)

def dodawanie(*args):
    result = sum(args)
    return result

def odejmowanie(a, b):
    result = a - b
    return result

def mnozenie(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def dzielenie(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero")
    result = a / b
    return result

def main():
    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

    operacja = int(input())
    logging.info(f"Wybrano operację numer {operacja}")

    if operacja in [1, 2, 3, 4]:
        if operacja in [1, 3]:
            args = [float(x) for x in input("Podaj składniki oddzielone spacją: ").split()]
        else:
            a = float(input("Podaj składnik 1: "))
            b = float(input("Podaj składnik 2: "))

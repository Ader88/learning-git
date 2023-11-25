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
        if operacja == 1:
            logging.info(f"Dodaję {', '.join(map(str, args))}")
            result = dodawanie(*args)
        elif operacja == 2:
            logging.info(f"Odejmuję {a} i {b}")
            result = odejmowanie(a, b)
        elif operacja == 3:
            logging.info(f"Mnóżę {', '.join(map(str, args))}")
            result = mnozenie(*args)
        elif operacja == 4:
            logging.info(f"Dzielę {a} przez {b}")
            result = dzielenie(a, b)

        print(f"Wynik to {result:.2f}")

    else:
        print("Błędny numer operacji. Wybierz 1, 2, 3 lub 4.")
if __name__ == "__main__":
    main()

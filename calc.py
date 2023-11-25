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
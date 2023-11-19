print("......................................")
lista_zakupow = {
    'Piekarnia': ['Chleb', 'Pączek', 'Bułki'],
    'Warzywniak': ['Marchew', 'Seler', 'Rukola']
    }
print("L I S T A  Z A K U P Ó W :")
suma_produktow = 0
for sklep, produkty in lista_zakupow.items():
    sklep_wielkimi = sklep.upper()
    produkty_wielkimi = [produkt.upper() for produkt in produkty]
    print(f"Idę do {sklep_wielkimi}, kupuję tu następujące rzeczy: {produkty_wielkimi}.")
    suma_produktow += len(produkty)
print(f"W sumie kupuję {suma_produktow} produktów.")
print("......................................")
print("......................................")
lista_zakupow = {
    'Piekarnia': ['Chleb', 'Pączek', 'Bułki'],
    'Warzywniak': ['Marchew', 'Seler', 'Rukola']
    }
print("L I S T A  Z A K U P Ó W :")
suma_produktow = 0
for sklep, produkty in lista_zakupow.items():
    sklep_wielkimi = sklep.upper()
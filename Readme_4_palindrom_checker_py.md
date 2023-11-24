# Trochę o tym czym jest palindrom_checker:

PALINDROM to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo, zastem program sprawdza czy dane słowo (tekst) jest palindromem czy nie. 

# WYJAŚNIENIE KODU:

def czy_palindrom(tekst): # Sprawdza, czy dany tekst jest palindromem.

#Parametry:
 -> tekst (string): # Tekst do sprawdzenia.

    Zwraca: 
        True # jeśli tekst jest palindromem, 
        False # jeśli nim nie jest.

    tekst = tekst.replace(" ", "")  # Usuwa spacje z tekstu, aby uniknąć błędów w przypadku fraz z odstępami
    
#Sprawdzenie, czy tekst czytany od lewej do prawej i od prawej do lewej jest taki sam :

for i in range(len(tekst)//2):
        if tekst[i] != tekst[len(tekst)-1-i]:
            return False

#Jeśli wszystkie pary znaków są zgodne, to tekst jest palindromem

return True
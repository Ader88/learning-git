Trochę o tym czym jest palindrom_checker:

PALINDRM to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo, zastem program sprawdza czy dane słowo (tekst) jest palindromem czy nie. 

Wyjaśnienie kodu:

def czy_palindrom(tekst): # Sprawdza, czy dany tekst jest palindromem.

    Parametry:
    - tekst (string): # Tekst do sprawdzenia.

    Zwraca: 
        True # jeśli tekst jest palindromem, 
        False # jeśli nim nie jest.

    tekst = tekst.replace(" ", "")  # Usuwa spacje z tekstu, aby uniknąć błędów w przypadku fraz z odstępami
    
# Sprawdza, czy tekst czytany od lewej do prawej i od prawej do lewej jest taki sam :
for i in range(len(tekst)//2):
        if tekst[i] != tekst[len(tekst)-1-i]:
            return False
    
# Jeśli wszystkie pary znaków są zgodne, to tekst jest palindromem
        return True


print(czy_palindrom("kajak")) # Powinien zwrócić True
print(czy_palindrom("potop")) # Powinien zwrócić True
print(czy_palindrom("hello")) # Powinien zwrócić False
print(czy_palindrom("kamil")) # Powinien zwrócić False
print(czy_palindrom("ślimak")) # Powinien zwrócić False
print(czy_palindrom("anna")) # Powinien zwrócić True
print(czy_palindrom("kamil ślimak")) # Powinien zwrócić True
print(czy_palindrom("atak kata")) # Powinien zwrócić True
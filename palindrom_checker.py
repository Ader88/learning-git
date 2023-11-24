def czy_palindrom(tekst):
    tekst = tekst.replace(" ", "")
    for i in range(len(tekst)//2):
        if tekst[i] != tekst[len(tekst)-1-i]:
            return False
        return True
print(czy_palindrom("kajak"))
print(czy_palindrom("potop"))
print(czy_palindrom("hello"))
print(czy_palindrom("kamil"))
print(czy_palindrom("ślimak"))
print(czy_palindrom("anna"))
print(czy_palindrom("kamil ślimak"))
print(czy_palindrom("atak kata"))
def czy_palindrom(tekst):
    tekst = tekst.replace(" ", "")
    for i in range(len(tekst)//2):
        if tekst[i] != tekst[len(tekst)-1-i]:
            return False
        return True
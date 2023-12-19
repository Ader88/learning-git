import random

class Wizytowka:
    def __init__(self, imie, nazwisko, firma, stanowisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firma = firma
        self.stanowisko = stanowisko
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.email}"

# Generowanie losowych danych dla wizytówek
def generuj_losowe_dane():
    imiona = ["Anna", "Jan", "Maria", "Piotr", "Katarzyna"]
    nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Dąbrowski", "Lewandowski"]
    firmy = ["ABC Company", "XYZ Corporation", "123 Industries", "Smart Solutions", "Innovate Tech"]
    stanowiska = ["Manager", "Programmer", "Marketing Specialist", "CEO", "Analyst"]
    domeny_email = ["example.com", "company.com", "test.org", "email.net", "domain.biz"]

    imie = random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    firma = random.choice(firmy)
    stanowisko = random.choice(stanowiska)
    email = f"{imie.lower()}.{nazwisko.lower()}@{random.choice(domeny_email)}"

    return Wizytowka(imie, nazwisko, firma, stanowisko, email)

# Tworzenie listy wizytówek
lista_wizytowek = [generuj_losowe_dane() for _ in range(5)]

# Wyświetlanie informacji o wizytówkach
for wizytowka in lista_wizytowek:
    print(wizytowka)
from faker import Faker
import random
print("-----------------------------------------------------------------------")
fake = Faker()

class BaseContact:
    label_length = 0

    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
        BaseContact.label_length = len(f"{self.imie} {self.nazwisko}")

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko} z firmy {self.firma}")

def create_contacts(rodzaj, ilosc):
    contacts = []
    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        if rodzaj == "BaseContact":
            contacts.append(BaseContact(imie, nazwisko, telefon, email))
        elif rodzaj == "BusinessContact":
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            contacts.append(BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy))
    
    return contacts

# Tworzenie listy wizytówek
lista_wizytowek = create_contacts("BaseContact", 3) + create_contacts("BusinessContact", 2)

# Wyświetlanie informacji o wizytówkach
for wizytowka in lista_wizytowek:
    wizytowka.contact()
    print(f"Label length: {wizytowka.label_length}")
    print()
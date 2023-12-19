import random

class Media:
    def __init__(self, tytul, rok, gatunek, liczba_odt):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.liczba_odt = liczba_odt

    def play(self):
        self.liczba_odt += 1

    def __str__(self):
        return f"{self.tytul} ({self.rok})"

class Film(Media):
    def __str__(self):
        return f"{super().__str__()}"

class Serial(Media):
    def __init__(self, tytul, rok, gatunek, numer_sezonu, numer_odcinka, liczba_odt):
        super().__init__(tytul, rok, gatunek, liczba_odt)
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka

    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02} ({self.rok})"

class Biblioteka:
    def __init__(self):
        self.kolekcja = []

    def dodaj_media(self, media):
        self.kolekcja.append(media)

    def get_movies(self):
        return sorted([media for media in self.kolekcja if isinstance(media, Film)], key=lambda x: x.tytul)

    def get_series(self):
        return sorted([media for media in self.kolekcja if isinstance(media, Serial)], key=lambda x: x.tytul)

    def search(self, tytul):
        return [media for media in self.kolekcja if tytul.lower() in media.tytul.lower()]

    def generate_views(self):
        media = random.choice(self.kolekcja)
        views = random.randint(1, 100)
        media.liczba_odt += views
        print(f"Dodano {views} odtworzeń dla: {media}")

    def generate_views_multiple(self, n):
        for _ in range(n):
            self.generate_views()

    def top_titles(self, n):
        return sorted(self.kolekcja, key=lambda x: x.liczba_odt, reverse=True)[:n]

# Przykładowe użycie
biblioteka = Biblioteka()

# Dodanie filmów i seriali do biblioteki
film1 = Film("Pulp Fiction", 1994, "Crime", 0)
film2 = Film("The Shawshank Redemption", 1994, "Drama", 0)

serial1 = Serial("Breaking Bad", 2008, "Crime", 1, 1, 0)
serial2 = Serial("Game of Thrones", 2011, "Drama", 2, 3, 0)

biblioteka.dodaj_media(film1)
biblioteka.dodaj_media(film2)
biblioteka.dodaj_media(serial1)
biblioteka.dodaj_media(serial2)

# Odtwarzanie i wyświetlanie informacji o mediach
film1.play()
serial1.play()
biblioteka.generate_views_multiple(10)

# Wyświetlenie listy filmów i seriali
print("\nFilmy:")
for film in biblioteka.get_movies():
    print(film)

print("\nSeriale:")
for serial in biblioteka.get_series():
    print(serial)

# Wyszukiwanie
print("\nWyszukiwanie:")
results = biblioteka.search("Pulp")
for result in results:
    print(result)

# Top tytuły
print("\nTop tytuły:")
top_titles = biblioteka.top_titles(2)
for title in top_titles:
    print(f"{title} - Odtworzenia: {title.liczba_odt}")
import requests
import csv
import os

# Pobierz dane z API NBP
url = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"
response = requests.get(url)

# Sprawdź, czy żądanie było udane
if response.status_code == 200:
    data = response.json()

    # Pobierz listę rates
    rates_list = data[0]["rates"]

    # Ścieżka do pliku CSV w tym samym miejscu co plik aplikacji .py
    csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kursy_walut.csv")

    # Otwórz plik CSV do zapisu
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        # Utwórz obiekt writer z separatorem ; i formatem tekstowym dla wszystkich komórek
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

        # Zapisz nagłówki
        writer.writerow(['currency', 'code', 'bid', 'ask'])

        # Zapisz dane z listy rates
        for rate in rates_list:
            writer.writerow([rate['currency'], rate['code'], '="' + str(rate['bid']) + '"', '="' + str(rate['ask']) + '"'])

    print(f"Plik CSV został utworzony: {csv_file_path}")
else:
    print(f"Błąd podczas pobierania danych. Kod statusu: {response.status_code}")
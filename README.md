1. Plik skryptu oraz pliki csv muszą znajdować się w tej samej lokalizacji.
2. Skrypt database.py tworzy bazę danych weather_data.db na podstawie plików csv (clean_measure.csv oraz clean_stations.csv) w tym samym katalogu, w którym znajduje się skrypt.
3. Następnie skrypt odwołuje się do tej bazy danych poprzez wywołanie:

conn.execute("SELECT * FROM stations LIMIT 5").fetchall()

4. Wyniki są widoczne w terminalu po tekście "Wyniki po wczytaniu danych".

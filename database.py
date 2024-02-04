# database.py

from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
import os

# Zmiana aktualnej ścieżki roboczej na folder, w którym znajduje się skrypt
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# Sprawdzenie aktualnej ścieżki roboczej
print("Aktualna ścieżka robocza:", os.getcwd())

# Tworzenie bazy danych i tabeli
engine = create_engine('sqlite:///weather_data.db', echo=True)
Base = declarative_base()

# Tworzenie tabeli stacji
class Station(Base):
    __tablename__ = 'stations'
    station = Column(String, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    name = Column(String)
    country = Column(String)
    state = Column(String)

# Tworzenie tabeli pomiarów
class Measurement(Base):
    __tablename__ = 'measurements'
    station = Column(String, primary_key=True)
    date = Column(String, primary_key=True)
    precip = Column(Float)
    tobs = Column(Integer)

# Tworzenie tabel w bazie danych
Base.metadata.create_all(engine)

# Wczytywanie danych z clean_stations.csv do tabeli stacji
csv_path_stations = os.path.join(script_directory, 'clean_stations.csv')
with open(csv_path_stations, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    conn = engine.connect()
    conn.execute(Station.__table__.insert(), list(csv_reader))

# Wczytywanie danych z clean_measure.csv do tabeli pomiarów
csv_path_measure = os.path.join(script_directory, 'clean_measure.csv')
with open(csv_path_measure, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    conn.execute(Measurement.__table__.insert(), list(csv_reader))

# Przykład zapytania SELECT
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print("Wyniki po wczytaniu danych:")
print(result)

# Zamykanie połączenia
conn.close()

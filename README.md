# team-6-energy-costs

### Repo for energy costs project

# This is my Code right now:

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

#Daten importieren
energy_data = pd.read_csv("energy_2020.csv")
energy_data.head(3)

#Zeilenname verändern zur Vereinfachung
energy_data.rename(columns={'Datum (UTC);"Import Saldo";"Kernenergie";"Nicht Erneuerbar";"Erneuerbar";"Day Ahead Auktion (DE-LU)"': 'GesamteDaten'}, inplace=True)
energy_data.head(3)

#Große Spalte in sechs Spalten splitten mit ; als Schlüssel
energy_data[['UTC', 'ImportSaldo', 'Kernenergie', 'Nicht Erneuerbar', 'Erneuerbar', 'DayAheadAuktion']]=energy_data.GesamteDaten.str.split(';',expand=True)
energy_data.head(3)

#Gibt es eine Automatisierung wie viele Spalten es geben muss? Dass es sechs Spalten sind habe ich zufällig erraten..

#UTC Spalte in zwei Spalten splitten mit Leerzeichen als Schlüssel
energy_data[['Datum', 'Uhrzeit']]=energy_data.UTC.str.split(' ', expand=True)
energy_data.head(3)

#Spalten "GesamteDaten", "UTC" und "ImportSaldo" löschen
del energy_data['GesamteDaten']
del energy_data['UTC']
del energy_data['ImportSaldo']
energy_data.head(3)

energy_data = energy_data[['Datum', 'Uhrzeit', 'DayAheadAuktion', 'Kernenergie', 'Nicht Erneuerbar', 'Erneuerbar']]
energy_data.head(3)

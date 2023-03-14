import pandas as pd

energy_data = pd.read_csv("energy_data2020.csv", sep=";")

energy_data.rename(columns={"Datum (UTC)": "DatumUhrzeit", "Import Saldo": "ImportSaldo",
                            "Nicht Erneuerbar": "NichtErneuerbar",
                            "Day Ahead Auktion (DE-LU)": "DayAheadAuktion"}, inplace=True)


'''Hier sind erstmal generell Informationen über die Kernenergie'''
kernenergie_durchschnitt = energy_data.Kernenergie.mean()
kernenergie_median = energy_data.Kernenergie.median()
kernenergie_max = energy_data.Kernenergie.max()
kernenergie_min = energy_data.Kernenergie.min()

n_kernernergie = {"kern_durchschnitt": kernenergie_durchschnitt,
                  "median": kernenergie_median,
                  "max": kernenergie_max,
                  "min": kernenergie_min,
                  "spanne": kernenergie_max - kernenergie_min}

print(n_kernernergie)


'''Hier sind erstmal generell Informationen über Nicht Erneuerbar'''
nicht_ee_durchschnitt = energy_data.NichtErneuerbar.mean()
nicht_ee_median = energy_data.NichtErneuerbar.median()
nicht_ee_max = energy_data.NichtErneuerbar.max()
nicht_ee_min = energy_data.NichtErneuerbar.min()

n_nicht_ee = {"nicht_ee_durchschnitt": nicht_ee_durchschnitt,
              "median": nicht_ee_median,
              "max": nicht_ee_max,
              "min": nicht_ee_min,
              "spanne": nicht_ee_max - nicht_ee_min}

print(n_nicht_ee)


'''Hier sind erstmal generell Informationen über Erneuerbar'''
ee_durchschnitt = energy_data.Erneuerbar.mean()
ee_median = energy_data.Erneuerbar.median()
ee_max = energy_data.Erneuerbar.max()
ee_min = energy_data.Erneuerbar.min()

n_ee = {"ee_durchschnitt": ee_durchschnitt,
        "median": ee_median,
        "max": ee_max,
        "min": ee_min,
        "spanne": ee_max - ee_min}

print(n_ee)


'''Hier sind die Informationen in eine Liste zusammengefasst'''
energy_info = []

energy_info.append(n_kernernergie)
energy_info.append(n_nicht_ee)
energy_info.append(n_ee)

print(energy_info)


'''Hier sind die Rows an dem der Strom am meisten gekostet hat. Das war am 21.9.2020 zwischen 17h-18h'''
max_paid = energy_data.loc[(energy_data["DayAheadAuktion"] == energy_data.DayAheadAuktion.max())]


'''Hier sind die Rows an dem der Strom am wenigsten gekostet hat. Das war am 21.4.2020 zwischen 12h-13h'''
min_paid = energy_data.loc[(energy_data["DayAheadAuktion"] == energy_data.DayAheadAuktion.min())]

print(max_paid)
print(min_paid)


'''Hier wollte ich ein dict. erstellen in dem Datum und Uhrzeit als key und der Preis <0 (günstig) 
als value gespeichert ist. 
Das habe ich nicht herausgefunden, daher habe ich erstmal eine Liste erstellt mit den Kosten <0. 
Die sagt aber nicht viel aus.'''
cheap_cost = {}
cheap_cost = []

for cost in energy_data.DayAheadAuktion:
    if cost <0:
        #cheap_cost = {energy_data.DatumUhrzeit: num}
        cheap_cost.append(cost)




'''Hier wollte ich ein dict. erstellen in dem Datum und Uhrzeit als key und der Preis >180 (teuer) 
als value gespeichert ist. 
Das habe ich nicht herausgefunden, daher habe ich erstmal eine Liste erstellt mit den Kosten >180. 
Die sagt aber nicht viel aus.'''
expensive_cost = {}
expensive_cost = []

for cost in energy_data.DayAheadAuktion:
    if cost >180:
        #expensive_cost = {energy_data.DatumUhrzeit: num}
        expensive_cost.append(cost)

print(cheap_cost)
print(expensive_cost)
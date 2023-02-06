import data_preparator 
import pandas as pd

###  energy data  ###
# energy data 2020 cleaning and preparation 
df_energy_2020 = data_preparator.clean_df_energy('../data/raw/energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2020_Excel.csv')

# add date, day of week and time columns
df_energy_2020 = data_preparator.add_date_week_time(df_energy_2020)

# add total energy feeding
df_energy_2020['total_energy_feeding'] = df_energy_2020['nuclear_power'] + df_energy_2020['not_renewable'] + df_energy_2020['renewable']


# save as csv in data folder
df_energy_2020.to_csv(
    '../data/prepared/df_energy_price_and_feeding_2020', 
    index=False
)

# energy data 2021 cleaning and preparation 
df_energy_2021 = data_preparator.clean_df_energy('../data/raw/energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2021_Excel.csv')

# add date, day of week and time columns
df_energy_2020 = data_preparator.add_date_week_time(df_energy_2020)

# add date, day of week and time columns
df_energy_2021 = data_preparator.add_date_week_time(df_energy_2021)

# add total energy feeding
df_energy_2021['total_energy_feeding'] = df_energy_2021['nuclear_power'] + df_energy_2021['not_renewable'] + df_energy_2021['renewable']

# save as csv in data folder
df_energy_2021.to_csv(
    '../data/prepared/df_energy_price_and_feeding_2021',
    index=False
)
import data_preparator 
import pandas as pd

def save_prep_energy_data(data_url, save_url):

    # energy data 2020 cleaning and preparation 
    df_energy = data_preparator.clean_df_energy(data_url)

    # add date, day of week and time columns
    df_energy = data_preparator.add_date_week_time(df_energy)

    # add total energy feeding
    df_energy['total_energy_feeding'] = df_energy['nuclear_power'] +     df_energy['not_renewable'] + df_energy['renewable']

    # datetime
    df_energy['datetime'] = pd.to_datetime(df_energy['datetime'])

    # save as csv in data folder
    df_energy.to_csv(
        save_url,
        index=False
    )

# 2019
save_prep_energy_data(
    '../data/raw/energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2019_Excel.csv',
    '../data/prepared/df_energy_2019.csv'
)

# 2020
save_prep_energy_data(
    '../data/raw/energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2020_Excel.csv',
    '../data/prepared/df_energy_2020.csv'
)

# 2021
save_prep_energy_data(
    '../data/raw/energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2021_Excel.csv',
    '../data/prepared/df_energy_2021.csv'
)

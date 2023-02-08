import pandas as pd

df_energy_2020 = pd.read_csv('../data/prepared/df_energy_price_and_feeding_2020.csv')
df_energy_2021 = pd.read_csv('../data/prepared/df_energy_price_and_feeding_2021.csv')
df_climate_2020 = pd.read_csv('../data/prepared/df_climate_2020.csv')
df_climate_2021 = pd.read_csv('../data/prepared/df_climate_2021.csv')

def combine_energy_climate(energy_data, climate_data, save_url):
    # convert to datetime
   energy_data['datetime'] = pd.to_datetime(energy_data['datetime'])
   climate_data['datetime'] = pd.to_datetime(climate_data['datetime'])

   # resample df_energy_2020 by hour, as climate data is per hour
   energy_data_per_hour = df_energy_2020.resample('60min', on='datetime').agg({
        'nuclear_power': 'mean', 
        'not_renewable': 'mean',
        'renewable': 'mean',
        'energy_price': 'mean'
    })
   energy_data_per_hour.reset_index(inplace=True)
   df_energy_climate = pd.merge(climate_data, energy_data_per_hour)

   df_energy_climate.to_csv(save_url)

combine_energy_climate(
   df_energy_2020, 
   df_climate_2020, 
   '../data/prepared/df_energy_climate_2020'
)

combine_energy_climate(
   df_energy_2021, 
   df_climate_2021, 
   '../data/prepared/df_energy_climate_2021'
)
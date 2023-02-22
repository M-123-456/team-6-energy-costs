import pandas as pd

df_energy_2019 = pd.read_csv('../data/prepared/df_energy_2019.csv')
df_energy_2020 = pd.read_csv('../data/prepared/df_energy_2020.csv')
df_energy_2021 = pd.read_csv('../data/prepared/df_energy_2021.csv')
df_climate_2019 = pd.read_csv('../data/prepared/df_climate_2019.csv')
df_climate_2020 = pd.read_csv('../data/prepared/df_climate_2020.csv')
df_climate_2021 = pd.read_csv('../data/prepared/df_climate_2021.csv')

def combine_energy_climate(energy_data, climate_data, save_url):
   # datetime
   energy_data['datetime'] = pd.to_datetime(energy_data['datetime'])
   climate_data['datetime'] = pd.to_datetime(climate_data['datetime'])

   # resample energy_data by hour, as climate data is per hour
   energy_data_per_hour = energy_data.resample('60min', on='datetime').mean()
  
   energy_data_per_hour.reset_index(inplace=True)
   df_energy_climate = pd.merge(climate_data, energy_data_per_hour)

   df_energy_climate.to_csv(save_url, index=False)

combine_energy_climate(
   df_energy_2019, 
   df_climate_2019, 
   '../data/prepared/df_energy_climate_2019.csv'
)

combine_energy_climate(
   df_energy_2020, 
   df_climate_2020, 
   '../data/prepared/df_energy_climate_2020.csv'
)

combine_energy_climate(
   df_energy_2021, 
   df_climate_2021, 
   '../data/prepared/df_energy_climate_2021.csv'
)
import pandas as pd
from helpers import data_preparator 

###  energy data  ###
# energy data 2020 cleaning and preparation 
df_energy_2020 = data_preparator.clean_df_energy('./data/raw/energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2020_Excel.csv')

# add date, day of week and time columns
df_energy_2020 = data_preparator.add_date_week_time(df_energy_2020)

# save as csv in data folder
df_energy_2020.to_csv('./data/prepared/df_energy_price_and_feeding_2020')

# energy data 2021 cleaning and preparation 
df_energy_2021 = data_preparator.clean_df_energy('./data/raw/energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2021_Excel.csv')

# add date, day of week and time columns
df_energy_2021 = data_preparator.add_date_week_time(df_energy_2021)

# save as csv in data folder
df_energy_2021.to_csv('./data/prepared/df_energy_price_and_feeding_2021')


###  climate data  ###

# climate data 2020
df_wind_2020 = data_preparator.clean_df_climate('./data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2020_Excel.csv')

df_solar_2020 = data_preparator.clean_df_climate('./data/energy-charts_Globale_Solarstrahlung_in_Deutschland_im_Jahr_2020_Excel.csv')

# merge wind and sun data
df_climate_2020 = pd.merge(df_wind_2020, df_solar_2020)

# save as csv in data folder
df_climate_2020.to_csv('./data/prepared/df_climate_2020')

# climate data 2021
df_wind_2021 = data_preparator.clean_df_climate('./data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2021_Excel.csv')

df_solar_2021 = data_preparator.clean_df_climate('./data/')

print(df_wind_2021)

# merge wind and sun data
df_climate_2021 = pd.merge(df_wind_2021, df_solar_2021)

# save as csv in data folder
df_climate_2021.to_csv('./data/prepared/df_climate_2021')
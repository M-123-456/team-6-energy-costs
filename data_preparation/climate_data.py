import pandas as pd
import data_preparator 

# climate data 2020
df_wind_2020 = data_preparator.clean_df_climate('../data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2020_Excel.csv')

df_solar_2020 = data_preparator.clean_df_climate('../data/raw/energy-charts_Globale_Solarstrahlung_in_Deutschland_im_Jahr_2020_Excel.csv')

# merge wind and sun data
df_climate_2020 = pd.merge(df_wind_2020, df_solar_2020)

# save as csv in data folder
df_climate_2020.to_csv(
    '../data/prepared/df_climate_2020',
    index=False
)

# climate data 2021
df_wind_2021 = data_preparator.clean_df_climate('../data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2021_Excel.csv')

df_solar_2021 = data_preparator.clean_df_climate('../data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2021_Excel.csv')

# merge wind and sun data
df_climate_2021 = pd.merge(df_wind_2021, df_solar_2021)

# save as csv in data folder
df_climate_2021.to_csv(
    '../data/prepared/df_climate_2021',
    index=False
)
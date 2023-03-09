import pandas as pd
import data_preparator 

def save_prep_climate_data(wind_url, solar_url, temperature_url,  save_url):
    # climate data 2020
    df_wind = data_preparator.clean_df_climate(wind_url)
    df_solar = data_preparator.clean_df_climate(solar_url)
    df_tempreture = data_preparator.clean_df_climate(temperature_url)

    # merge wind, sun and tempreture data
    df_climate = df_wind.merge(df_solar, on='datetime')
    df_climate = df_climate.merge(df_tempreture, on='datetime')

    # datetime
    df_climate['datetime'] = pd.to_datetime(df_climate['datetime'])

    # save as csv in data folder
    df_climate.to_csv(
        save_url,
        index=False
    )

# 2019
save_prep_climate_data(
    '../data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2019_Excel.csv',
    '../data/raw/energy-charts_Globale_Solarstrahlung_in_Deutschland_im_Jahr_2019_Excel.csv',
    '../data/raw/energy-charts_Lufttemperatur_in_Deutschland_im_Jahr_2019_Excel.csv',
    '../data/prepared/df_climate_2019.csv'
)

# 2020
save_prep_climate_data(
    '../data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2020_Excel.csv',
    '../data/raw/energy-charts_Globale_Solarstrahlung_in_Deutschland_im_Jahr_2020_Excel.csv',
    '../data/raw/energy-charts_Lufttemperatur_in_Deutschland_im_Jahr_2020_Excel.csv',
    '../data/prepared/df_climate_2020.csv'
)

# 2021
save_prep_climate_data(
    '../data/raw/energy-charts_Windgeschwindigkeit_in_Deutschland_im_Jahr_2021_Excel.csv',
    '../data/raw/energy-charts_Globale_Solarstrahlung_in_Deutschland_im_Jahr_2021_Excel.csv',
     '../data/raw/energy-charts_Lufttemperatur_in_Deutschland_im_Jahr_2021_Excel.csv',
    '../data/prepared/df_climate_2021.csv'
)
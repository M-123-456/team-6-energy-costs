# imports
import numpy as np 
import pandas as pd
from datetime import datetime

def clean_df_energy(url):
    # define date parser
    d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

    # read csv file (set date column as index)
    df = pd.read_csv(
        url,
        sep=";", 
        parse_dates=['Datum (MT+1)'], 
        date_parser=d_parser
    )

    # copy df to edit df
    df_energy = df.copy()

    # remove import saldo column, as all values are NaN
    df_energy = df_energy.dropna(axis=1, how="all")

    # rename date column
    df_energy.rename(columns={'Datum (MT+1)': 'datetime', 'Day Ahead Auktion (DE-LU)': 'energy_price', 'Nicht Erneuerbar': 'not_renewable','Kernenergie': 'nuclear_power', 'Erneuerbar': 'renewable' }, inplace=True)

    # Check if there is any na value in df
    df_energy.replace('na', np.nan, inplace=True)
    df_energy.replace('NA', np.nan, inplace=True)
    df_energy.replace('Missing', np.nan, inplace=True)

    # drop duplicates
    df_energy.drop_duplicates(inplace=True)

    return df_energy

def add_date_week_time(df):
    # add Date column
    df['date'] = df['datetime'].dt.date
    # add weekday column
    df['day_of_week'] = df['datetime'].dt.day_name()
    # add time
    df['time'] = df['datetime'].dt.time

    return df


def clean_df_climate(url):
    d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    df_climate = pd.read_csv(
       url,
       sep=';',
       parse_dates=['Date (UTC)'], 
       date_parser=d_parser,
    )
    
    # Check if there is any na value in df
    df_climate.replace('na', np.nan, inplace=True)
    df_climate.replace('NA', np.nan, inplace=True)
    df_climate.replace('Missing', np.nan, inplace=True)

    # remove duplicates
    df_climate.drop_duplicates()

    if 'Windgeschwindigkeit' in url:
       df_climate.rename(columns={'Date (UTC)': 'datetime', 'Value': 'wind_speed'}, inplace=True)
    elif 'Solarstrahlung' in url:
        df_climate.rename(columns={'Date (UTC)': 'datetime', 'Value': 'solar_radiation'}, inplace=True)
    else:
        df_climate.rename(columns={'Date (UTC)': 'datetime', 'Value': 'tempreture'}, inplace=True)

    
    return df_climate

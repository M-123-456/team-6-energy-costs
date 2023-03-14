import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import pendulum
from pendulum.constants import SATURDAY

st.title('Energy cost estimation')

today = date.today()

# Calculation is done for one week, starting always on the next Saturday 
start_day = pendulum.now().next(SATURDAY)
end_day = start_day + timedelta(days=7)
formatted_start = start_day.strftime('%Y-%m-%d')
formatted_end = end_day.strftime('%Y-%m-%d')

st.markdown(f'Today is {today}')
st.markdown(f'The estimation period: {formatted_start} - {formatted_end}')


# On_click to be added to start estimation
button = st.button(
    'SHOW ESTIMATION OF NEXT WEEK',
)


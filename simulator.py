import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import pendulum

st.title('Energy cost estimation')

today = date.today()
start_day = pendulum.now().next(pendulum.SATURDAY)
end_day = start_day + timedelta(days=7)
formatted_start = start_day.strftime('%Y-%m-%d')
formatted_end = end_day.strftime('%Y-%m-%d')

st.markdown(f'Today is {today}')
st.markdown(f'The estimation period: {formatted_start} - {formatted_end}')

# on_click to be added
button = st.button(
    'SHOW ESTIMATION OF NEXT WEEK'
)

import pandas as pd
import streamlit as st
from db.connection import connect_to_db

@st.cache_data
def load_station_locations():
    conn = connect_to_db()
    query = "SELECT station_code, station_name, latitude, longitude, province, basin FROM flowcast.station_info;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
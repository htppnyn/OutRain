import psycopg2
import pandas as pd
from config import DB_CONFIG
import streamlit as st

def connect_to_db():
    return psycopg2.connect(**DB_CONFIG)

@st.cache_data
def load_station_locations():
    conn = connect_to_db()
    query = "SELECT station_code, station_name, latitude, longitude, province, basin FROM flowcast.station_info;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

@st.cache_data(show_spinner="กำลังโหลดข้อมูล...")
def get_rainfall_data(station_code):
    try:
        conn = connect_to_db()
        query = """
            SELECT station_code, time, rainfall
            FROM flowcast.rainfalltimeseries
            WHERE station_code = %s
            ORDER BY time DESC;
        """
        df = pd.read_sql(query, conn, params=(station_code,))
        conn.close()
        return df
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")
        return pd.DataFrame()

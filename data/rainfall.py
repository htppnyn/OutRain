import pandas as pd
import streamlit as st
from db.connection import connect_to_db

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

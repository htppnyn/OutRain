import streamlit as st
import pandas as pd
from datetime import timedelta
from utils.db import load_station_locations, get_rainfall_data
from utils.map_layer import create_map_layer
import pydeck as pdk

def app():
    st.title("Rainfall Time Series Viewer")
    st.subheader("แผนที่สถานีตรวจวัดฝน")

    station_df = load_station_locations()

    st.sidebar.title("ตัวกรอง")

    province_options = ["ทั้งหมด"] + sorted(station_df["province"].unique().tolist())
    selected_province = st.sidebar.selectbox("เลือกจังหวัด", province_options)

    filtered_df = station_df.copy()
    if selected_province != "ทั้งหมด":
        filtered_df = filtered_df[filtered_df["province"] == selected_province]

    basin_options = ["ทั้งหมด"] + sorted(filtered_df["basin"].unique().tolist())
    selected_basin = st.sidebar.selectbox("เลือกลุ่มน้ำ", basin_options)

    if selected_basin != "ทั้งหมด":
        filtered_df = filtered_df[filtered_df["basin"] == selected_basin]

    station_options = ["ทั้งหมด"] + sorted(
        filtered_df.apply(lambda row: f"{row['station_code']} - {row['station_name']}", axis=1).tolist()
    )
    selected_station_label = st.sidebar.selectbox("เลือกสถานี", station_options)
    selected_station_code = selected_station_label.split(" - ")[0] if selected_station_label != "ทั้งหมด" else None

    if selected_station_code:
        filtered_df = filtered_df[filtered_df["station_code"] == selected_station_code]

    lat_center = filtered_df["latitude"].mean()
    lon_center = filtered_df["longitude"].mean()

    layer = create_map_layer(station_df.copy(), selected_station_code)

    view_state = pdk.ViewState(
        latitude=lat_center,
        longitude=lon_center,
        zoom=7.5,
        pitch=0,
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/streets-v11",
        tooltip={"text": "{station_name}"}
    ))

    if selected_station_code and not filtered_df.empty:
        station_name = filtered_df.iloc[0]["station_name"]
        st.write(f"สถานีที่เลือก: **{selected_station_code} - {station_name}**")

        df = get_rainfall_data(selected_station_code)

        if not df.empty:
            df["time"] = pd.to_datetime(df["time"])
            min_date = df["time"].min().date()
            max_date = df["time"].max().date()
            default_start = max_date - timedelta(days=7)

            start_date, end_date = st.sidebar.date_input(
                "เลือกช่วงวันที่", 
                value=(default_start, max_date),
                min_value=min_date,
                max_value=max_date
            )

            filtered_rain = df[(df["time"].dt.date >= start_date) & (df["time"].dt.date <= end_date)]

            st.markdown(f"ข้อมูลฝนระหว่าง **{start_date} - {end_date}**")
            st.dataframe(filtered_rain.drop(columns=["station_code"]), use_container_width=True)

            if not filtered_rain.empty:
                st.line_chart(filtered_rain.set_index("time")["rainfall"])
            else:
                st.warning("ไม่มีข้อมูลในช่วงวันที่ที่เลือก")
        else:
            st.warning("ไม่พบข้อมูลฝนสำหรับสถานีนี้")

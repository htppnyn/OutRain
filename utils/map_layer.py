import pydeck as pdk

def create_map_layer(station_df, selected_station_code):
    station_df["color"] = station_df["station_code"].apply(
        lambda x: [255, 0, 0] if x == selected_station_code else [0, 0, 255, 50]
    )

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=station_df.rename(columns={"latitude": "lat", "longitude": "lon"}),
        get_position='[lon, lat]',
        get_fill_color="color",
        get_radius=5000,
        pickable=True
    )
    return layer

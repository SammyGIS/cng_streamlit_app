import streamlit as st
import pandas as pd
import geopandas as gpd
import leafmap.foliumap as leafmap


APP_TITLE = 'CNG STATION ACROSS NIGERIA'
file_path = "cng_locations_ng.geojson"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon='⛽',
    layout='wide',
    initial_sidebar_state='collapsed'
)

st.caption(APP_TITLE)

data = gpd.read_file(file_path)

def filter(data:gpd.GeoDataFrame, col_name:str):

    # create a sorted unique name
    col_unique_list = [None] + sorted(data[col_name].dropna().unique().tolist())

    # select options
    selection = st.sidebar.selectbox(col_name, col_unique_list, key=col_name)

    # filter based on selection
    if selection:
        selected_option = data[data[col_name] == selection]
    else:
        selected_option = data
    
    return selected_option


def create_basemap(center=[9.0820, 8.6753], zoom=6):
    """create a basemap"""
    m=leafmap.Map(center=center,zoom=zoom)
    m.add_tile_layer(
            url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            name="Google Satellite",
            attribution="Google",
        )
    m.add_basemap("TERRAIN")
    st.write("Map Visualization")
    m.to_streamlit()
    m.add_geojson(file_path, layer_name="CNG Stations")







filter(data,"State")
filter(data,"LGA")
filter(data,"Name")
create_basemap()
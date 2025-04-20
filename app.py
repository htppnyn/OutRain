import streamlit as st
from ui.map_view import show_map_view

def app():
    st.set_page_config(layout="wide")
    show_map_view()

if __name__ == "__main__":
    app()
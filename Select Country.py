import streamlit as st
import folium as fl
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import time
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

st.header('Select a country for data')
def get_country(lat,lng):
    URL = f'http://api.geonames.org/countryCodeJSON?lat={lat}&lng={lng}&username=lalva224'
    response = requests.get(URL)
    data = response.json()
    #this means no country selected
    if 'status' in data or data['countryName']=='Antarctica':
        st.error('No country selected!')   
    else:    
        country = data["countryName"]
        st.session_state['country'] = country




    
    
   
# global clicked_location
m = fl.Map()
m.add_child(fl.ClickForMarker(popup='Clicked Location'))


map = st_folium(m, height=350, width=700)

if st.button('Select Country'):
    lat = map['last_clicked']['lat']
    lng = map['last_clicked']['lng']
    get_country(lat,lng)

    


import streamlit as st
import folium as fl
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import time
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import folium


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
        country_code = data["countryCode"]
        st.session_state['countryCode'] = country_code
        st.session_state['country'] = country
        st.success(f'{country} selected')

# def get_country(lat,lng):
#     API_KEY = os.getenv('OPEN_CAGE_KEY')
#     URL = f'https://api.opencagedata.com/geocode/v1/json?q={lat}%2C{lng}&key={API_KEY}'
#     response = requests.get(URL)
#     data = response.json()

#     country = data['results'][0]['components']['country']
#     countryCode = data['results'][0]['components']['ISO_3166-1_alpha-2']
#     st.session_state['country'] = country
#     st.session_state['countryCode'] = countryCode
#     st.success(f'{country} selected')
  
    



    
    
   
# global clicked_location
m = fl.Map()
m.add_child(fl.ClickForMarker(popup='Clicked Location'))
# m = folium.Map()
# popup1 = folium.LatLngPopup()

# m.add_child(popup1)

map = st_folium(m, height=350, width=700)

if st.button('Select Country'):
    lat = map['last_clicked']['lat']
    lng = map['last_clicked']['lng']
    get_country(lat,lng)

    


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


def get_country(lat,lng):
    global SELECTED_COUNTRY
    URL = f'http://api.geonames.org/countryCodeJSON?lat={lat}&lng={lng}&username=lalva224'
    response = requests.get(URL)
    data = response.json()
    country = data["countryName"]
    SELECTED_COUNTRY = country
    

    #get some of their data

def get_fertility_rate():
    url = "https://geography4.p.rapidapi.com/apis/geography/v1/fertility/"

    querystring = {"name":SELECTED_COUNTRY}

    headers = {
        "X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
        "X-RapidAPI-Host": "geography4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    #fertility data in graph
    for area in data:
        country_name = area["name"]
        href_fertility = area["historicalData"]['href']
        url_fertility = f'https://geography4.p.rapidapi.com{href_fertility}'

        response_fertility = requests.get(url_fertility, headers=headers, params=querystring)
 
        df = pd.DataFrame(response_fertility.json())
        df = df.set_index('year')
        st.header(country_name)
        st.line_chart(df)
        # st.write(response.json())
    
    
   
INDEX = 0
# global clicked_location
m = fl.Map()
m.add_child(fl.ClickForMarker(popup='Clicked Location'))


map = st_folium(m, height=350, width=700)

if st.button('Select Country'):
    lat = map['last_clicked']['lat']
    lng = map['last_clicked']['lng']
    get_country(lat,lng)

    


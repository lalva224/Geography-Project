import requests
from dotenv import load_dotenv
import os
import streamlit as st
import folium
from streamlit_folium import folium_static

load_dotenv()
city_data = []
st.header('Major Cities')
def add_marker(m,name,lat,lng):

    # Add a marker for the provided latitude and longitude
    folium.Marker([lat, lng], popup=name).add_to(m) 

def display_cities(og_lat,og_lng):
     m = folium.Map(location=[og_lat, og_lng], zoom_start=4)
     for city in city_data:
        add_marker(m,city['name'],city['lat'],city['lng'])
     folium_static(m)

def get_major_cities():
    api_url = f"https://api.api-ninjas.com/v1/city?country={st.session_state['countryCode']}&limit=10"
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv('API_NINJAS_KEY')})
    if response.status_code == requests.codes.ok:
        # st.write(response.json())

        for city in response.json():
            name = city['name']
            lat = city['latitude']
            lng = city['longitude']

            city_dict = {
                'name':name,
                'lat': lat,
                'lng':lng
            }
            city_data.append(city_dict)
        
        #give a random location in this city bc it will be zoomed out
        display_cities(city_data[0]['lat'],city_data[0]['lng'])
    else:
        st.error(response.text)
        print("Error:", response.status_code, response.text)


if 'country' in st.session_state and st.session_state['country']!=None:   
    get_major_cities()
else:
    st.warning('Please select a country')

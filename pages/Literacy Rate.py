import requests
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()

st.header('Literacy Rate')
def get_literacy_rate():
    url = "https://geography4.p.rapidapi.com/apis/geography/v1/literacy/"

    querystring = {"limit":"5","name":st.session_state['country']}

    headers = {
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": "geography4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    for i,area in enumerate(data):
        country_name = area["name"]
        literacy_href =  area["historicalData"]['href']
        url = f'https://geography4.p.rapidapi.com{literacy_href}'
        response = requests.get(url=url,headers=headers,params=querystring)

                # Extract the value of "adult"
        adult_value = data[i]["total"]["adult"]

        # Create labels and sizes for the pie chart
        labels = ['Literate', 'Illiterate']
        sizes = [adult_value, 100 - adult_value]

        # Create a pie chart
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


        st.header(f'{country_name} Literacy Rate')
        st.pyplot(fig)
        

    

if 'country' in st.session_state and st.session_state['country']!=None:   
    get_literacy_rate()
else:
    st.warning('Please select a country')
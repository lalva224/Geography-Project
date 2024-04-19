import streamlit as st
import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()

st.header('Fertility Rate  starting 2017')
def get_fertility_rate():
    url = "https://geography4.p.rapidapi.com/apis/geography/v1/fertility/"

    querystring = {"name":st.session_state['country']}

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

if 'country' in st.session_state and st.session_state['country']!=None:   
    get_fertility_rate()
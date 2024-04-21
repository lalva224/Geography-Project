import streamlit as st
import os
from dotenv import load_dotenv
import requests
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()

st.header('Fertility Rate')
def get_fertility_rate():
    url = "https://geography4.p.rapidapi.com/apis/geography/v1/fertility/"

    querystring = {"limit":"5","name":st.session_state['country']}

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


# def get_fertility_rate():
#     df = pd.read_csv('data/children_per_woman_total_fertility.csv')
#     # st.write(df['country']==st.session_state['country'])
#     country_row = df.loc[df['country']== st.session_state['country']]
#     # st.write(df)
#     # st.write(country_row[0])
#     years = country_row.columns
#     data = country_row.iloc[:,1:]
#     st.bar_chart(country_row)
   
 
    # indexes_to_select = [1] + list(range(51, country_row.shape[1], 50))

    # # Select the specific rows using iloc
    # specific_rows = country_row.iloc[:,indexes_to_select]
    # specific_rows.set_index(years)
    # st.line_chart(specific_rows)


if 'country' in st.session_state and st.session_state['country']!=None:   
    get_fertility_rate()
else:
    st.warning('Please select a country')
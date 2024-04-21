import requests
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

load_dotenv()
countries = []
def display_countries():
    df = pd.DataFrame(countries)
    st.write(df)
    
def search_by_language(language):
    url = f"https://geography4.p.rapidapi.com/apis/geography/v1/country/language/{language}"

    querystring = {"sortOrder":"desc","limit":"10","sortBy":"population","fields":"name,currencies,capital,region,subregion,languages,landlocked"}

    headers = {
        "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
        "X-RapidAPI-Host": "geography4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    # st.write(data)
    for country in data:
        try:
            name = country['name']['common']
            
            capital = country["capital"][0]["name"]
            print('-----------------------')
            print(capital)
            print('-----------------------')
            region = country['region']
            subregion = country['subregion']
            landlocked = country['landlocked']

            language_list = country['languages']
            language_builder = [language['name'] for language in language_list]
            languages = ','.join(language_builder)

            currency_list = country["currencies"]
            currency_builder = [currency['name'] for currency in currency_list]
            currencies = ','.join(currency_builder)
        except KeyError:
            pass
        country_dict = {
            'name':name,
            'currency':currencies,
            'capital':capital,
            'region':region,
            'subregion':subregion,
            'landlocked':landlocked,
            'languages' : languages

        }
        countries.append(country_dict)
    
    display_countries()

st.header('Countries by Language')

language_selection = st.radio(
    'Select a language',
    ['English','Spanish','Portuguese','Arabic','Russian']
)

language = st.text_input('Language: ')

if st.button('Confirm Selection'):
    
    search_by_language(language_selection)

if language!='':
    search_by_language(language)






   
import streamlit as st
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY') 

st.set_page_config(page_title='Weather App',page_icon="🌤️")

css_file = Path(__file__).parent / "app.css"

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title('Wheather App 🌤️')

st.write('Enter the city name and click on button to fetch weather data')

city = st.text_input("Enter city" )

if(st.button('Fetch Weather data')):
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(API_URL)
    if(response.status_code == 200):
        st.success('weather data fetch successfully')
        data = (response.json())
        # exract data in variables
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        condition = data['weather'][0]['main']
        country = data['sys']['country']
        name = data['name']
        # Display the Data
        st.header(f'{name},{country}')
        col1,col2 = st.columns(2)
        col3,col4 = st.columns(2)
        col1.metric('Temperature',f'{temperature}°C🌡️')
        col2.metric('Humidity',f'{humidity}%💦')
        col3.metric('Wind_speed',f'{wind_speed}m/s🍃')
        col4.metric('Condition',f'{condition}🌧️')
    else :
        st.error('Invalid city name')
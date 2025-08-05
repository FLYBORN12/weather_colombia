from bs4 import BeautifulSoup
import requests
from etl import handler_error

def extract_scrapping(url_base):
    try:
        requests_page = requests.get(url_base)
        result = requests_page.text


        soup_page = BeautifulSoup(result,"html.parser")
        table_weather = soup_page.find_all(class_  = 'zebra')[0]

        citys = table_weather.find_all('a')
        weathers = table_weather.find_all('img',alt=True)
        temps = table_weather.find_all(class_ = 'rbi')

        data = {
            'ciudad':[],
            'weather':[],
            'temp':[]
            }


        for city in citys:
            data['ciudad'].append(city.get_text(strip=True))

        for weather in weathers:
            data['weather'].append(weather['alt'].strip())

        for temp in temps:
            data['temp'].append(temp.get_text(strip=True))

        return data
    except Exception as e:
        handler_error.logging.error(f'Error trying extract info from the source {e}')
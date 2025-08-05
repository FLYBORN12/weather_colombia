import pandas as pd
from etl import transform,extract_clima_scrapper,load_to_db,extract_from_db,handler_error,create_tables

#url_base = 'http://dragonball-api.com/api'
#result = requests.get(f'{url_base}/characters/{2}')
#resultHtml = result.text

def run():
    url_base = 'https://www.timeanddate.com/weather/colombia'

    data = extract_clima_scrapper.extract_scrapping(url_base)

    df = pd.DataFrame(data)

    #Add datetime to Dataframe
    df['datetime'] = pd.to_datetime('today')
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M')

    #Transform temperature
    df['temp'] = df['temp'].str.replace('°C','')

    #Trasformation
    df_original = df

    df_clean_to_insert_childs_tbl = transform.handler_data_to_insert(df_original)

    #crear tablas 
    create_tables.create_tables()

    load_to_db.load_tbl_city(list(df_clean_to_insert_childs_tbl['ciudad']))
    load_to_db.load_tbl_weather(list(df_clean_to_insert_childs_tbl['weather']))
    load_to_db.load_tbl_temp(list(df_clean_to_insert_childs_tbl['temp']))


    data_city_from_db = extract_from_db.get_data_from_DB('city',['id_city','name_city'])
    data_weather_from_db = extract_from_db.get_data_from_DB('weather',['id_weather','type_weather'])
    data_temp_from_db = extract_from_db.get_data_from_DB('temperature',['id_temp','temperature'])

    
    union_data = {
        'city':data_city_from_db,
        'weather':data_weather_from_db,
        'temperature':data_temp_from_db
    }

    data_to_insert_fact = transform.clean_to_insert_fact_db(union_data,df_original)

    load_to_db.load_tbl_fact_weather_city(data_to_insert_fact)



if __name__ == '__main__':
    run()
else:
    handler_error.logging.critical('Ups, this module have something wrong! check code')
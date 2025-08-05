import pandas as pd
from etl import handler_error


def handler_data_to_insert(dataFrame):
    try:
        df_test = dataFrame.copy()

        #Transformation
        df_test['temp'] = df_test['temp'].str.replace('°C','')

        df_test['weather'] = [(str(w),) for w in df_test['weather']]
        df_test['ciudad'] = [(str(c),) for c in df_test['ciudad']]
        df_test['temp'] = [(int(t),) for t in df_test['temp']]
        
        return df_test
    except Exception as e:
        handler_error.logging.critical(f'error cleaning data {e}')


"""def drop_duplicates_by_column(data,column):
    try:
        result = data.drop_duplicates(subset=[column],keep='first')
        return result
    except Exception as e:
        handler_error.logging.critical(f'Error intentando borrar duplicados {e}')"""


def clean_to_insert_fact_db(dataDB,dataScrapping):
    df_final = dataScrapping.copy()


    if 'city' in dataDB:
        df_city = pd.DataFrame(dataDB['city'],columns=['id_city','name_city'])
        df_final = pd.merge(df_city,df_final,left_on='name_city',right_on='ciudad',how='inner')
    if 'weather' in dataDB:
        df_weather = pd.DataFrame(dataDB['weather'],columns=['id_weather','type_weather'])
        df_final = pd.merge(df_weather,df_final,left_on='type_weather',right_on='weather',how='inner')
    if 'temperature' in dataDB:
        df_temp = pd.DataFrame(dataDB['temperature'],columns=['id_temp','temperature'])
        #Parseando los datos de temp a int, ya que desde el df viene en type object!
        df_final['temp'] = [(int(t)) for t in df_final['temp']]
        df_final = pd.merge(df_temp,df_final,left_on='temperature',right_on='temp',how='inner')


    df_to_save = df_final[['id_city','id_weather','id_temp','datetime']]

    df_to_save = [(row.id_city,row.id_weather,row.id_temp,row.datetime) for row in df_to_save.itertuples(index=False)]

    return df_to_save

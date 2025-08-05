from etl import handler_error
from etl.config import get_connection


def load_tbl_city(data):
    conn = get_connection()
    if conn is None:
        return []
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany("""INSERT INTO city (name_city) values (%s) ON CONFLICT (name_city) DO NOTHING""",data)
                conn.commit()
        if cur.rowcount > 0:
            handler_error.logging.info(f'Insert realizado con exito, fueron {cur.rowcount} registros insetados en la tbl city')
        else:
            handler_error.logging.info(f'los registros ya existían en la base de datos. Nada nuevo insertado')
    except Exception as e:
        handler_error.logging.error(f'Error insertando en la tbl city {e}')
    finally:
        conn.close()


def load_tbl_weather(data):
    conn = get_connection()
    if conn is None:
        return []
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany("INSERT INTO weather (type_weather) values (%s) ON CONFLICT (type_weather) DO NOTHING",data)
                conn.commit()
        if cur.rowcount > 0:
            handler_error.logging.info(f'Insert realizado con exito, fueron {cur.rowcount} registros insetados en la tbl weather')
        else:
            handler_error.logging.info(f'los registros ya existían en la base de datos. Nada nuevo insertado')
    except Exception as e:
        handler_error.logging.error(f'Error insertando en la tbl weather {e}')
    finally:
        conn.close()


def load_tbl_temp(data):
    conn = get_connection()
    if conn is None:
        return []
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany("INSERT INTO temperature (temperature) values (%s) ON CONFLICT (temperature) DO NOTHING",data)
                conn.commit()
        if cur.rowcount > 0:
            handler_error.logging.info(f'Insert realizado con exito, fueron {cur.rowcount} registros insetados en la tbl temperature')
        else:
            handler_error.logging.info(f'los registros ya existían en la base de datos. Nada nuevo insertado')
    except Exception as e:
        handler_error.logging.error(f'Error insertando en la tbl temperature {e}')
    finally:
        conn.close()



def load_tbl_fact_weather_city(data):
    conn = get_connection()
    if conn is None:
        return []
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany("INSERT INTO weather_city_by_colombia (id_city,id_weather,id_temp,date_weather) values (%s,%s,%s,%s)",data)
                conn.commit()
        if cur.rowcount > 0:
            handler_error.logging.info(f'Insert realizado con exito, fueron {cur.rowcount} registros insetados en la tbl fact')
        else:
            handler_error.logging.info(f'los registros ya existían en la base de datos. Nada nuevo insertado')
    except Exception as e:
        handler_error.logging.error(f'Error insertando en la tbl fact {e}')
    finally:
        conn.close()        

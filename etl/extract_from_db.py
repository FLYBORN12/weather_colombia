from etl import handler_error
from etl.config import get_connection


def get_data_from_DB(tbl,columns):
    allowed_tables = [
        'weather',
        'city',
        'temperature',
        'weather_city_by_colombia'
    ]

    allowed_columns = {
        'weather':['id_weather','type_weather'],
        'city':['id_city','name_city'],
        'temperature':['id_temp','temperature']
    }

    if tbl not in allowed_tables:
        handler_error.logging.error(f'Tabla no permitada!')

    for col in columns:
        if col not in allowed_columns[tbl]:
            handler_error.logging.error(f'Columna {col} no permitida en la tabla {tbl}')

    columns_sql = ', '.join(columns)
    query = f'Select {columns_sql} from {tbl}'

    conn = get_connection()
    if conn is None:
        return []

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                resultQuery = cur.fetchall()
                conn.commit()
            if cur.rowcount > 0:
                handler_error.logging.info(f'Consulta realizada con exito a tbl {tbl}')
                return resultQuery
            else:
                return handler_error.logging.info(f'No hay data en la tabla {tbl}!')
    except Exception as e:
        return handler_error.logging.error(f'Error consultando la tabla {tbl}, {e}')
    finally:
        conn.close()

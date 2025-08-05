import psycopg2
import os
from dotenv import load_dotenv
from etl import handler_error

load_dotenv()

user = os.getenv('USER_DB')
db = os.getenv('NAME_DB')
password = os.getenv('PASS_DB')
host = os.getenv('HOST_DB')
port = os.getenv('PORT_DB')


def get_connection():
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user=user,
            password=password
        )
        return conn
    except psycopg2.Error as e:
        handler_error.logging.critical(f'Error trying connect to DB {db} \n more info {e}')
        exit()
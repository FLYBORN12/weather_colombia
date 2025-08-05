from etl import handler_error
from etl.config import get_connection


commands = (
"""
create table if not exists city(
id_city serial not null,
name_city varchar(50) not null,
CONSTRAINT pk_city PRIMARY KEY (id_city),
CONSTRAINT unique_name_city UNIQUE (name_city)
)""",

"""
create table if not exists weather(
id_weather serial not null,
type_weather varchar(100) not null,
	CONSTRAINT pk_weather PRIMARY KEY (id_weather),
	CONSTRAINT unique_type_weather UNIQUE (type_weather)
)
""",
"""
create table if not exists temperature(
id_temp serial not null,
temperature int not null,
	CONSTRAINT pk_id_temp PRIMARY KEY (id_temp),
	CONSTRAINT unique_temperature UNIQUE (temperature)
)""",
"""
CREATE TABLE if not exists weather_city_by_colombia (
	id_weather_city serial NOT NULL,
	id_weather int NOT NULL,
	id_city int NOT NULL,
	id_temp int NOT NULL,
	date_weather timestamp NOT NULL,
	CONSTRAINT pk_weather_city_by_colombia PRIMARY KEY (id_weather_city),
	CONSTRAINT wcbyc_id_weather_fk FOREIGN KEY (id_weather) REFERENCES weather(id_weather),
	CONSTRAINT wcbyc_id_city_fk FOREIGN KEY (id_city) REFERENCES city(id_city),
	CONSTRAINT wcbyc_id_temp_fk FOREIGN KEY (id_temp) REFERENCES temperature(id_temp)
)""",


)

def create_tables():
    conn = get_connection()
    if conn is None:
        handler_error.logging.error("Connection is None, cannot create tables.")
        return
    try:
        with conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
            handler_error.logging.info("Tables created successfully.")
    except Exception as e:
        handler_error.logging.error(f'Failed to create tables: {e}')
    finally:
        conn.close()
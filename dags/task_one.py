from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.main import run


from common_args import default_args


dag = DAG(
    dag_id='run_proyect_weather',
    default_args=default_args,
    description='DAG para ejecutar main del proyect',
    schedule='@hourly',  # Corre cada hora
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['main_etl_dag'],
) 



task_main = PythonOperator(
    task_id='task_main',
    python_callable=run,
    dag = dag
)

task_main
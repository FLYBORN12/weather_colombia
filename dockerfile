FROM apache/airflow:3.0.3

USER root

# Copia solo el requirements.txt
COPY requirements.txt /

# Instala dependencias del sistema y pip requirements
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar código al contenedor
COPY etl /opt/airflow/etl
COPY dags /opt/airflow/dags

USER airflow

RUN pip install --no-cache-dir -r /requirements.txt
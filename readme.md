## 🌤️ Weather Data Pipeline

### ⚙️Tecnologías

![Airflow](https://img.shields.io/badge/Airflow-2.0+-blue?logo=apache-airflow)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue?logo=postgresql)  
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?logo=power-bi)  
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)  
![GCP](https://img.shields.io/badge/GCP-Deployed-brightgreen?logo=google-cloud)  

### 📌 Descripción

Este proyecto implementa un **pipeline de datos del clima en Colombia** que:

- **Scrapea datos meteorológicos** de fuentes públicas.  
- **Orquesta el flujo** usando **Apache Airflow**.  
- **Almacena la información** en una base de datos **PostgreSQL** desplegada en **Google Cloud Platform (GCP)**.  
- **Visualiza los resultados** en un dashboard interactivo de **Power BI**.  

El objetivo es mostrar un flujo de trabajo completo de **Data Engineering + BI**, desde la extracción hasta la visualización.  

### ⚙️ Arquitectura

```
flowchart LR
    A[🌍 Scraping Clima] --> B[🌀 Airflow DAG]
    B --> C[(🐘 PostgreSQL en GCP)]
    C --> D[📊 Power BI Dashboard]
🚀 Tecnologías utilizadas
Python 🐍 → Web Scraping y procesamiento de datos (Pandas)

Apache Airflow 🌀 → Orquestación de tareas ETL

PostgreSQL 🐘 → Base de datos en la nube

Docker 🐳 → Contenerización del entorno

Google Cloud Platform (GCP) ☁️ → Infraestructura en la nube

Power BI 📊 → Visualización de datos
```

### 🛠️ Instalación local
```

- Clona el repositorio
git clone https://github.com/FLYBORN12/weather_colombia.git
cd weather_colombia

Configura las variables de entorno en .env

- USER_DB=
- NAME_DB=
- PASS_DB=
- HOST_DB=
- PORT_DB=

#DOCKER
- AIRFLOW_IMAGE_NAME=apache/airflow:3.0.3
- AIRFLOW_UID=50000


- Construye los contenedores con Docker
docker-compose up --build

- Accede a Airflow en tu navegador
http://localhost:8080
```

### 📊 Dashboard
```
El dashboard en Power BI permite:

📅 Filtrar por fecha/hora

🌡️ Analizar temperatura

📍 Ver información segmentada por región

```

👨‍💻 Autor 
<br></br>
<a href="https://www.linkedin.com/in/juanfehoyos/"><img alt="Linkedin" src="https://img.shields.io/badge/Linkedin-Felipe%20Hoyos-blue?style=flat-square&logo=linkedin"></a>

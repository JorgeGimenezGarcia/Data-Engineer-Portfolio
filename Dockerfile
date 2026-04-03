# Base Airflow image
FROM apache/airflow:2.8.1-python3.11

# Install required Python packages for the project
USER airflow
RUN pip install --no-cache-dir \
    "dbt-snowflake" \
    "snowflake-connector-python[pandas]" \
    "pandas" \
    "apache-airflow-providers-dbt-cloud" \
    "apache-airflow[cncf.kubernetes]" # Useful for future Kubernetes-based tasks

# Copy your dags, dbt project, and pipelines into the container
COPY dags/ /opt/airflow/dags
COPY pipelines/ /opt/airflow/pipelines
COPY dbt_project/ /opt/airflow/dbt_project
COPY requirements.txt /opt/airflow/requirements.txt
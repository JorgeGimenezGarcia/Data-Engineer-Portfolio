from __future__ import annotations
import pendulum

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# The Python callable needs to be imported relative to the DAGs folder
from pipelines.ingestion import run_ingestion

with DAG(
    dag_id="data_engineer_portfolio_elt",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,  # Run manually for the portfolio demo
    catchup=False,
    tags=["data_engineering", "dbt", "snowflake", "elt"],
) as dag:

    # 1. Ingestion Task (Python script to load data into Snowflake STAGING)
    ingest_to_snowflake = PythonOperator(
        task_id="ingest_raw_data_to_snowflake",
        python_callable=run_ingestion,
    )

    # 2. Data Quality Test (CRITICAL: Shows TDD and Data Governance)
    dbt_test = BashOperator(
        task_id="run_dbt_tests",
        # Use the profile defined in dbt_project/profiles.yml
        bash_command="cd /opt/airflow/dbt_project && dbt test --profiles-dir . --profile de_portfolio_dbt",
    )

    # 3. Transformation Task (dbt run to build the Marts)
    dbt_run = BashOperator(
        task_id="run_dbt_models",
        bash_command="cd /opt/airflow/dbt_project && dbt run --profiles-dir . --profile de_portfolio_dbt",
    )

    # Define the ELT pipeline dependency order:
    ingest_to_snowflake >> dbt_test >> dbt_run

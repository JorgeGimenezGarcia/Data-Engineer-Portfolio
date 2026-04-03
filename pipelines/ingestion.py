import pandas as pd
from snowflake.connector import connect

# Using write_pandas for efficient staging load
from snowflake.connector.pandas_tools import write_pandas
import os

# Use environment variables for connection (best practice)
SNOWFLAKE_USER = os.environ.get("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.environ.get("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.environ.get("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.environ.get("SNOWFLAKE_WAREHOUSE")

# Fixed target details
SNOWFLAKE_DATABASE = "DE_PORTFOLIO_DB"
SNOWFLAKE_SCHEMA = "STAGING"
SNOWFLAKE_TABLE = "RAW_SALES_DATA"


def run_ingestion():
    # 1. SIMULATION OF EXTRACTION (e.g., from a Salesforce/SAP API or Cloud Storage)
    print("Simulating data extraction...")
    data = {
        "id": [1, 2, 3, 4, 5],
        "product_name": ["A", "B", "C", "D", "E"],
        "price": [10.50, 20.00, 5.25, 15.00, 30.00],
        "sale_date": [
            "2023-10-01",
            "2023-10-02",
            "2023-10-03",
            "2023-10-04",
            "2023-10-05",
        ],
    }
    df = pd.DataFrame(data)

    # 2. LOAD TO SNOWFLAKE
    try:
        conn = connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
        )
        print(
            f"Connected to Snowflake. Loading data into {SNOWFLAKE_SCHEMA}.{SNOWFLAKE_TABLE}..."
        )

        success, nchunks, nrows = write_pandas(
            conn=conn,
            df=df,
            table_name=SNOWFLAKE_TABLE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA,
            auto_create_table=True,
            overwrite=True,
        )
        print(f"Data loaded successfully: {nrows} rows.")
        conn.close()

    except Exception as e:
        print(f"Error during Snowflake operation: {e}")
        raise


if __name__ == "__main__":
    run_ingestion()

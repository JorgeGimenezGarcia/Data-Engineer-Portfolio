# 🚀 Senior Data Engineer Portfolio: Scalable ELT Pipeline (Airflow, dbt, Snowflake)

## 🎯 Project Overview

This repository showcases a professional, end-to-end **ELT (Extract, Load, Transform)** data pipeline built with cloud-native technologies, reflecting my experience as a **Senior Data Engineer**.

The pipeline is orchestrated with **Apache Airflow**, leverages **dbt (Data Build Tool)** for robust data transformations, and uses **Snowflake** as the **Cloud Data Warehouse (CDW)**.  
The entire environment is containerized using **Docker Compose** for local, reproducible deployment, demonstrating strong **DataOps** and **Infrastructure as Code (IaC)** proficiency.

---

## 🌟 Key Features

- **Advanced Orchestration:** Manages task dependencies, retries, and monitoring via Apache Airflow.  
- **Data Quality & Governance:** Integration of **dbt tests** as a required gate before data transformation (`dbt run`).  
- **Infrastructure as Code (IaC):** Full environment setup using `docker-compose.yml`.  
- **Cloud-Native Stack:** Focused on high-performance tools — **Snowflake**, **dbt**, and **Python/Pandas**.

---

## 💡 Data Ecosystem Vision & Architecture

> **Note on Scope:**  
> The following diagram represents a full technical vision of a mature, end-to-end Data Engineering ecosystem (including components for Streaming, MLOps, and CI/CD).  
> The core repository implementation focuses on the **Airflow → dbt → Snowflake** segment, demonstrating robust ELT orchestration and data quality practices.

```mermaid
graph TD
  %% Data Sources
  A1[APIs / Streaming] -->|Ingestion| B1[Ingestion: Kafka / Airflow / Prefect]
  A2[SQL / NoSQL Databases] -->|Connections| B1
  A3[CSV Files / SFTP] -->|Batch| B1

  %% Orchestration & CI/CD
  subgraph Orchestration
    B1
    B2[Scheduler: Airflow / Prefect]
  end
  B2 --> B1

  %% Staging / Landing
  B1 --> C1[Data Lake Staging S3 / GCS]
  C1 -->|Raw| D1[Staging Tables / Bronze]

  %% Processing
  subgraph Processing
    D1 --> E1[Processing: Spark / Databricks / EMR]
    E1 --> E2[Transformations: dbt / SQL]
  end
  E2 --> F1[Data Warehouse / Lakehouse - Snowflake / BigQuery / Redshift / Delta Lake]

  %% Consumption Layer
  F1 --> G1[Data Marts / Cubes]
  G1 --> H1[BI Tools: Looker / Tableau / Power BI]
  G1 --> H2[ML Models / Feature Store]

  %% Infra & Ops
  subgraph Infra
    I1[CI/CD: GitHub Actions / GitLab CI]
    I2[Docker / Kubernetes]
    I3[Secrets: HashiCorp Vault / KMS]
    I4[Monitoring: Prometheus / Grafana / ELK]
  end
  I1 --> B2
  I2 --> E1
  I3 --> B1
  I4 -->|Logs / Metrics| B1
  I4 -->|Metrics| E1

  %% Metadata, Test & Quality
  E2 --> J1[Catalog / Metadata: Amundsen / Data Catalog]
  E2 --> J2[Tests: Great Expectations / dbt Tests]
  J2 --> I1

  %% Additional Flows
  C1 -.->|Temp Files / Logs| I4
  F1 -->|Backups| K1[Object Storage Archive]
  ```

## 💻 Technology Stack & Technical Justification

| Component | Technology | Justification (The "Why") |
| :--- | :--- | :--- |
| **Data Warehouse** | **Snowflake** | Utilized for its **elastic scalability** and **compute/storage separation**, ensuring cost-effectiveness and high performance for business intelligence (BI) and analytics. |
| **Orchestration** | **Apache Airflow** | Chosen for robust dependency management, scheduling, and error handling, critical for managing complex, mission-critical data flows. |
| **Transformation (ELT)** | **dbt (Data Build Tool)** | Implemented to apply Software Engineering best practices (Testing, Modularization, Versioning) to the SQL transformation layer, maximizing code maintainability. |
| **Ingestion Layer** | **Python (Pandas/Snowflake)** | Used for flexible data extraction (simulating API/ERP sources like SAP/Salesforce) and efficient bulk loading using the Snowflake Connector. |
| **Infrastructure** | **Docker / Docker Compose** | Deploys a reproducible, self-contained development environment, showcasing proficiency in modern **DataOps** and IaC principles. |

---

## ⚙️ Deployment and Execution

### Prerequisites

* Docker and Docker Compose installed.
* A Snowflake Account and valid credentials.

### Setup Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/Data-Engineer-Portfolio.git](https://github.com/YourUsername/Data-Engineer-Portfolio.git)
    cd Data-Engineer-Portfolio
    ```

2.  **Configure Credentials:**
    Update the environment variables in `docker-compose.yml` with your actual Snowflake credentials (USER, PASSWORD, ACCOUNT, WAREHOUSE, ROLE).

3.  **Build and Run the Stack:**
    This command builds the custom Airflow/dbt image and starts the Postgres metadata database and the Airflow Webserver/Scheduler.
    ```bash
    docker compose build
    docker compose up -d
    ```

4.  **Access Airflow UI:**
    Open `http://localhost:8080` in your browser. (Credentials: `admin`/`admin`)

5.  **Run the Pipeline:**
    * Find the `data_engineer_portfolio_elt` DAG.
    * Unpause the DAG and manually trigger a run.
    * Observe the sequence: **Ingestion** (Python) → **dbt Tests** (Data Quality) → **dbt Run** (Transformation).

---

## 📂 Repository Structure

This structure reflects a standard DataOps project layout, separating orchestration (dags), transformation (dbt_project), and custom code (pipelines).

```text
.
├── .github/                  # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       └── ci.yml            # Code quality check (Black) and dbt validation
├── dags/                     # Airflow DAGs
│   └── snowflake_dbt_dag.py  # Orchestrates Ingestion -> dbt Tests -> dbt Run
├── dbt_project/              # dbt core files (Transformation and Testing)
│   ├── models/
│   │   ├── marts/
│   │   │   ├── dim_daily_sales.sql
│   │   │   └── schema.yml      <-- Defines tests for Marts (Business Quality)
│   │   └── staging/
│   │       ├── stg_sales.sql
│   │       └── schema.yml      <-- Defines sources and tests for Staging (Data Integrity)
│   ├── profiles.yml
│   └── dbt_project.yml
├── pipelines/                # Custom Python ETL/Ingestion scripts
│   └── ingestion.py          # Script to load data into Snowflake RAW/STAGING
├── .gitignore
├── Dockerfile                # Custom Airflow + dbt image definition
└── docker-compose.yml        # Local environment orchestration
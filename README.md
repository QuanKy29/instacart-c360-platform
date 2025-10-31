# 🛒 Instacart C360 Platform
**Phase 1: Data Warehouse & Analytics Pipeline (Jan – Apr 2025)**  

---

## 📘 Project Overview  
This repository contains an end-to-end data platform built for the **Instacart e-commerce dataset**.  
The goal is to design a **modern data warehouse** supporting analytics, data modeling, and machine learning use cases.

The project applies the **Medallion Architecture** (Raw → Staging → Silver → Gold → ML/BI), and each layer is implemented with clear transformation logic using **dbt + PostgreSQL + Docker**.

---

## 🧱 Architecture Overview  
RAW (CSV)
↓
PostgreSQL (Docker)
↓
dbt staging (clean tables)
↓
dbt silver (fact tables)
↓
dbt gold (aggregated marts)
↓
Python export → CSV
↓
Power BI / ML models
---
---

## 📊 Data Flow Diagram  

```mermaid
flowchart TD
    A[CSV Raw Data] --> B[(PostgreSQL - Raw Layer)]
    B --> C[dbt Staging (Cleaned Models)]
    C --> D[dbt Silver (Fact Tables)]
    D --> E[dbt Gold (Analytics Marts)]
    E --> F[Python Export to CSV]
    F --> G[Power BI Dashboard / ML Models]

## 🗂️ Repository Structure  
instacart-c360-platform/
├── warehouse/             # DDL scripts, schema initialization
│   └── ddl/
│       └── init_schemas.sql
│
├── dbt/                   # dbt project (models, macros, tests, etc.)
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/       # staging models (cleaned base tables)
│   │   ├── silver/        # intermediate fact/dimension tables
│   │   └── gold/          # analytics-ready marts
│   └── target/            # compiled dbt outputs
│
├── ml/                    # Machine Learning preparation scripts
│   ├── export_gold_to_csv.py
│   └── exported_data/
│       ├── mart_user_summary.csv
│       ├── mart_product_summary.csv
│       └── mart_user_product_features.csv
│
├── bi/                    # (placeholder) dashboards & Power BI reports
│
├── docker-compose.yml     # Services: PostgreSQL, pgAdmin
├── README.md              # Main project documentation
└── README_top.md          # Executive summary for HR/portfolio
---

## ⚙️ Tech Stack  
| Layer | Tool / Technology |
|:------|:-------------------|
| **Data Storage** | PostgreSQL 15 (Docker container) |
| **Transformation** | dbt Core v1.10 |
| **Orchestration (upcoming)** | Apache Airflow (Phase 2) |
| **Data Export** | Python 3.12 (pandas + SQLAlchemy) |
| **Analytics & BI (upcoming)** | Power BI / Tableau |
| **Version Control** | Git + GitHub |
| **Environment** | macOS + VS Code |

---

## 📊 Current Status  

✅ **Phase 1 (Jan – Apr 2025)** – *Data Warehouse completed, Gold layer exported to CSV successfully*  
🟡 **Phase 2 (May – Aug 2025)** – *Implement Airflow DAGs, feature store, Power BI dashboard*  
🔵 **Phase 3 (Sep – Dec 2025)** – *Machine Learning models, MLflow tracking, API serving, CI/CD pipeline*

---

## 📈 Key Outputs (Gold Layer)
| Table Name | Description |
|-------------|--------------|
| `mart_user_summary` | Aggregated order metrics by user (total orders, reorder ratio, etc.) |
| `mart_product_summary` | Aggregated sales metrics by product (popularity, reorder rate, etc.) |
| `mart_user_product_features` | ML-ready features describing user × product interactions |

All three Gold tables are exported as CSV for downstream **Power BI** dashboards or **ML pipelines**.

---

## 🧠 Key Learnings  
- Data modeling with dbt (staging → silver → gold).  
- SQL optimization and transformation in PostgreSQL.  
- ELT/ETL design and testing with dbt.  
- Python data export automation.  
- Version control for data engineering projects.  
- Building reproducible pipelines with Docker + VS Code.  

---

## 🧩 Next Steps  
- [ ] Automate pipeline with **Airflow DAGs**.  
- [ ] Create Power BI dashboards from Gold CSV exports.  
- [ ] Implement **MLflow** to track models & experiments.  
- [ ] Deploy trained recommender system via FastAPI.  

---

## 👤 Author  
**Trương Quân Kỳ**  
Data Science Student @ IUH  
🎯 Aspiring Data Engineer / Data Analyst in E-Commerce Analytics  
📂 GitHub: [QuanKy29](https://github.com/QuanKy29)  

---

## 🏁 License  
This project is for educational purposes only and part of a long-term learning roadmap (2025 – 2026).  
Feel free to fork or reference for non-commercial use.



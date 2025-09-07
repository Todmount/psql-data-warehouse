<!-- GitHub adds lines after h1 and h2. To get rid of them, I use <details open> construction -->
<!-- Project name image -->
<p align="center">
    <img
        style="width: 800px"
        src="docs/assets/dbt_postges_project_name.webp"
        alt="dbt + PostgreSQL Data Warehouse"
    />
</p>

<!-- Some neat badges -->
<p align="center">
    <a href="https://github.com/Todmount" target="_blank">
        <img src="https://img.shields.io/badge/Portfolio_Project-215B55?style=flat-square" alt="Badge" title="My GitHub"></a>&#8287;
    <a href="LICENSE" target="_blank">
        <img src="https://img.shields.io/github/license/todmount/psql-data-warehouse?style=flat-square&label=License&color=%23A6C3A8" alt="Licence - MIT" title="License"></a>&#8287;
    <a href="https://www.databricks.com/glossary/medallion-architecture" target="_blank">
        <img src="https://img.shields.io/badge/Architecture-Medallion-215B80?style=flat-square" alt="Architecture - Medallion" title="Architecture"></a>&#8287;
    <a href="https://python.org" title="Supported python versions" target="_blank">
        <img src="https://img.shields.io/badge/Python-3.12+-blue.svg?&style=flat-square&logo=python&logoColor=white" alt="Python 3.12+"></a>&#8287;
    <a href="">
        <img src="https://img.shields.io/badge/Postgres-1.9.1-%23316192.svg?&style=flat-square&logo=postgresql&logoColor=white" alt="PostqreSQL 1.9.1"></a>&#8287;
    <a href="">
        <img src="https://img.shields.io/badge/dbt-1.10.11-%23316192.svg?&style=flat-square&logo=dbt&logoColor=white&color=FF694B" alt="dbt 1.10.11"></a>&#8287;
</p>

<!-- Overview -->
<details open>
    <summary><h2>Overview ✨</h2></summary>
    This repository contains a <b>dbt + PostgreSQL based data warehouse</b> built and adapted from a 
    <a href="https://ua.udemy.com/course/building-a-modern-data-warehouse-data-engineering-bootcamp" target="_blank">Data Engineering Bootcamp</a> curriculum.<br>  
    The original course examples use SQL Server — here, I re-implement them using dbt and PostgreSQL to deepen my understanding of SQL and warehouse design.
</details>

<!-- Objectives -->
<details open>
    <summary><h2>Objectives 🎯</h2></summary>

- Practice **SQL (DDL, DML, DCL, TCL)** in a warehouse environment
- Gain experience with **schema design and data modeling**
- Explore **ETL workflows** for loading and transforming data
- Learn **dimensional modeling** concepts
- Apply basic **analytics & reporting** queries
- Document progress as a learning and portfolio project
</details>

<!-- Data Architecture -->
<details>
    <summary><h2>Data Architecture 🏗</h2></summary>
    This project follows the suggested Medallion Architecture (Bronze, Silver, Gold layers), a common pattern for modern data warehouses.
    <img 
        src="docs/assets/data_architecture.webp" 
        alt="Medallion Data Architecture"
        title="High Level Architecture"
    />
</details>

<!-- Data Flow -->
<details><summary><h2>Data Flow 📽</h2></summary>

    <img
        src="docs/assets/data_flow.webp"
        alt="Project Data Flow"
        title="High Level Architecture"
    />

</details>

<!-- Repository Structure -->
<details open><summary><h2>Repository Structure 📂</h2></summary>

- `datasets` - Raw ERP and CRM datasets used for the project
- `docs` - Documentation and architecture diagrams
- `scripts` - SQL, Python, and Bash scripts for ETL and transformations
- `tests` - Validation scripts and data quality checks
</details>

<!-- Tech Stack -->
<details open><summary><h2>Tech Stack 🛠️</h2></summary>

- **PostgreSQL**
- Bash / Python (for ETL & automation)

</details>

<!-- Status -->
<details open><summary><h2>Status 📈</h2></summary>

Work in progress 🚧 — updated as I progress through the bootcamp.  
This is not a production-ready warehouse, but a **learning project** to practice data engineering fundamentals.

- [x] Add script for database initialization
- [x] Implement bronze level

</details>

<!-- Contributing -->
<details open><summary><h2>Contributing 🤝</h2></summary>

This is a learner’s portfolio project, so external contributions are not expected. However, feedback and suggestions are always welcome 😎

</details>

<!-- Contact -->
<details open markdown=1><summary><h2>Contact 🌐</h2></summary>

You could find relevant contact info on my [GitHub profile](https://github.com/Todmount)

</details>

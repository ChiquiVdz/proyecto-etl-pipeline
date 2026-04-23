# ETL Pipeline Project

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Python. The pipeline processes data from Excel files, performs cleaning and transformations, and loads the results into a SQLite database.

The design follows a modular approach to ensure maintainability and scalability.

---

## Architecture

The pipeline is composed of three stages:

* **Extract**: Reads raw data from Excel files
* **Transform**: Cleans and standardizes the data
* **Load**: Stores the processed data in a SQLite database

Pipeline flow:

```bash
Excel files → Extract → Transform → Load → SQLite database
```

---

## Project Structure

```bash
proyecto-etl-pipeline/
│
├── data/                # Source Excel files
├── extract.py           # Data extraction logic
├── transform.py         # Data transformation logic
├── load.py              # Data loading logic
├── main.py              # Pipeline orchestrator
├── proyecto.db          # Output database
└── README.md
```

---

## Technologies

* Python 3
* pandas
* SQLite
* pathlib

---

## How to Run

```bash
git clone <repository-url>
cd proyecto-etl-pipeline
pip install pandas openpyxl
python main.py
```

---

## ETL Process

### Extract

Reads multiple Excel files from the `data/` directory.

### Transform

Applies data cleaning operations such as:

* String normalization
* Duplicate removal
* Filtering invalid records

### Load

Loads the processed data into multiple tables in SQLite.

---

## Database Schema

The pipeline generates the following tables:

* `productos`
* `categorias`
* `proyectos`
* `transportes`
* `envios`
* `producto-proyecto`
* `costos`

Each table is created from its corresponding processed dataset.

---

## Output

The result is a SQLite database (`proyecto.db`) containing structured and cleaned data ready for analysis.

---

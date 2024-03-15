# Tax Invoice Project Documentation

## Overview
The Tax Invoice Project consists of a Django backend for data storage and processing and various Python scripts for data extraction, deduplication, SQL operations, reporting, and more. This project aims to extract transaction details from tax invoice PDF files, store them in a database, perform operations on the data, and generate reports based on the extracted information.

### Project Structure
- **tax_invoice_project/**: Root directory for the project.
  - **.vscode/**: Visual Studio Code configuration directory.
    - **launch.json**: Configuration file for running Python scripts.
  - **data/**: Directory containing sample PDF files.
    - **Test PDF.pdf**: Sample PDF file containing tax invoice data.
  - **src/**: Directory containing Python scripts for different project components.
    - **data_extraction.py**: Script to extract transaction details from PDF files.
    - **data_storage.py**: Script to store extracted transactions in the database.
    - **deduplication.py**: Script to remove duplicate transactions from the database.
    - **sql_operations.py**: Script to perform SQL operations on the database.
    - **reporting.py**: Script to generate reports based on the extracted data.
    - **models.py**: Django models for transactions.
  - **tax_invoice/**: Django project directory.
    - **tax_invoice/**: Django app directory.
      - **__init__.py**
      - **settings.py**: Django project settings file.
      - **urls.py**: URL configurations for the Django project.
      - **wsgi.py**: WSGI configuration for deployment.
    - **transactions/**: Django app directory for managing transactions.
      - **__init__.py**
      - **admin.py**: Django admin configurations.
      - **models.py**: Django models for transactions.
      - **tests.py**: Django tests for transactions.
      - **views.py**: Django views for transactions.
    - **db.sqlite3**: SQLite database file.
    - **manage.py**: Django management script.

### Functionality
- **Data Extraction (data_extraction.py)**: Extracts transaction details from tax invoice PDF files.
- **Data Storage (data_storage.py)**: Stores extracted transactions in the database.
- **Deduplication (deduplication.py)**: Removes duplicate transactions from the database.
- **SQL Operations (sql_operations.py)**: Performs SQL operations on the database, including calculating total loan amounts and highest loan amounts by broker.
- **Reporting (reporting.py)**: Generates various reports based on the extracted data, including data extraction report, data storage report, deduplication report, SQL operations report, and custom reporting logic.

## Running the Project
1. Ensure Python and Django are installed.
2. Set up the Django backend:
   - Navigate to the `tax_invoice` directory.
   - Run `python manage.py runserver`.
3. Run Python scripts for data extraction, data storage, deduplication, SQL operations, and reporting as needed.
4. Access Django admin interface to view and manage transactions: http://localhost:8000/admin/.
5. Explore generated reports and perform custom analysis based on project requirements.

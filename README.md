
---

# Credit Approval System

The **Credit Approval System** is a backend API built using Python/Django, designed to handle customer registration, credit limit calculation, and loan management based on past and current loan data. This project uses background tasks for data ingestion and integrates seamlessly with a PostgreSQL database, all containerized using Docker for easy setup and deployment.

---

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Background Tasks](#background-tasks)
- [Database Models](#database-models)
- [Example Requests](#example-requests)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Customer Registration**: Automatically calculates and assigns a credit limit based on the customer's monthly income.
- **Loan Eligibility Check**: Determines loan eligibility using historical data and provides loan interest rate recommendations.
- **Loan Creation**: Processes loan applications and manages loan details.
- **View Loan Information**: Retrieve detailed loan information for individual loans and all loans associated with a customer.
- **Data Ingestion**: Background workers to ingest customer and loan data from Excel files.

---

## Project Structure
```
Credit-Approval-System
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── customer_data.xlsx
├── loan_data.xlsx
│
├── credit_api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── tests.py
│
└── credit_approval_system
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── asgi.py
    └── views.py
```

---

## Tech Stack
- **Backend**: Python, Django, Django Rest Framework
- **Database**: PostgreSQL
- **Background Tasks**: `background_task` library
- **Containerization**: Docker, Docker Compose

---

## Setup and Installation
### Prerequisites
- Docker and Docker Compose installed on your system

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/Credit-Approval-System.git
   cd Credit-Approval-System
   ```

2. **Set Up Environment Variables**
   - Create a `.env` file (if required) to store environment-specific variables such as database credentials.

3. **Build and Run the Docker Containers**
   ```bash
   docker-compose up --build
   ```
   This command builds the Docker images and starts the containers for both the Django app and PostgreSQL database.

4. **Apply Migrations**
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

5. **Run Background Tasks for Data Ingestion**
   - The data ingestion tasks will run in the background, importing data from `customer_data.xlsx` and `loan_data.xlsx`.

---

## Running the Application
- Access the API at: `http://localhost:8000`
- **Admin Panel**: `http://localhost:8000/admin` (ensure you create a superuser using `python manage.py createsuperuser`)

---

## API Endpoints
### 1. **Register Customer** (`POST /register/`)
   - Registers a new customer and calculates the approved credit limit.
   - **Request Body**: `first_name`, `last_name`, `age`, `monthly_income`, `phone_number`
   - **Response**: Customer details with calculated credit limit.

### 2. **Check Loan Eligibility** (`POST /check-eligibility/`)
   - Checks the loan eligibility of a customer based on their credit score.
   - **Request Body**: `customer_id`, `loan_amount`, `interest_rate`, `tenure`
   - **Response**: Loan eligibility status and recommended interest rate.

### 3. **Create Loan** (`POST /create-loan/`)
   - Processes a new loan application for a customer.
   - **Request Body**: `customer_id`, `loan_amount`, `interest_rate`, `tenure`
   - **Response**: Loan approval status and monthly installment amount.

### 4. **View Loan** (`GET /view-loan/<loan_id>/`)
   - Retrieves detailed information about a specific loan.
   - **Response**: Loan details and associated customer information.

### 5. **View Loans by Customer** (`GET /view-loans/<customer_id>/`)
   - Lists all loans associated with a specific customer.
   - **Response**: A list of loan details.

---

## Background Tasks
- The project uses background tasks to ingest data from `customer_data.xlsx` and `loan_data.xlsx`.
- **Libraries Used**: `background_task`

---

## Database Models
### 1. **Customer Model**
   - `customer_id`: Auto-incremented primary key
   - `first_name`, `last_name`, `age`, `phone_number`
   - `monthly_salary`, `approved_limit`, `current_debt`

### 2. **Loan Model**
   - `loan_id`: Auto-incremented primary key
   - `customer`: Foreign key linking to `Customer`
   - `loan_amount`, `tenure`, `interest_rate`, `monthly_repayment`
   - `emis_paid_on_time`, `start_date`, `end_date`

---

## Example Requests
### Register Customer
```json
POST /register/
{
  "first_name": "John",
  "last_name": "Doe",
  "age": 30,
  "monthly_income": 50000,
  "phone_number": "1234567890"
}
```

### Check Loan Eligibility
```json
POST /check-eligibility/
{
  "customer_id": 1,
  "loan_amount": 100000,
  "interest_rate": 10,
  "tenure": 24
}
```

### Create Loan
```json
POST /create-loan/
{
  "customer_id": 1,
  "loan_amount": 100000,
  "interest_rate": 10,
  "tenure": 24
}
```

---

## Future Improvements
- Implement a frontend for better user experience.
- Enhance loan eligibility logic to consider more factors.
- Integrate automated testing for improved reliability.
- Add authentication and authorization for secure API access.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

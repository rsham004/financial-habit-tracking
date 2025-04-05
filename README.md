# Financial Habit Tracking Application

A web application for tracking expenses and analyzing spending habits.

## Features

- Add and update expenses with categories and notes
- View analytics by category to understand spending patterns
- View analytics by month to track spending over time

## Architecture

- **Backend**: FastAPI REST API
- **Frontend**: Streamlit web application
- **Database**: PostgreSQL

## Deployment Guide (Render.com)

This guide will help you deploy the application on Render.com, a simple cloud platform.

### 1. Database Setup

1. Sign up for a Render account at https://render.com
2. Create a new PostgreSQL database:
   - Go to Dashboard > New > PostgreSQL
   - Name: expense-manager-db
   - Database: expense_manager  expense_manager_xrnm
   - User: expense_user
   - Choose a plan (Free plan available for testing)
   - Click "Create Database"
3. Once created, note the following information:
   - Internal Database URL postgresql://expense_user:TGXJcqHlzbqMBqFtL4T3LDAVmI8KMWX5@dpg-cvof5gruibrs73bpqm5g-a/expense_manager_xrnm
   - External Database URL postgresql://expense_user:TGXJcqHlzbqMBqFtL4T3LDAVmI8KMWX5@dpg-cvof5gruibrs73bpqm5g-a.oregon-postgres.render.com/expense_manager_xrnm
   - Username expense_user
   - Password TGXJcqHlzbqMBqFtL4T3LDAVmI8KMWX5
   - Host dpg-cvof5gruibrs73bpqm5g-a
   - Port 5432
   - PSQL Command PGPASSWORD=TGXJcqHlzbqMBqFtL4T3LDAVmI8KMWX5 psql -h dpg-cvof5gruibrs73bpqm5g-a.oregon-postgres.render.com -U expense_user expense_manager_xrnm

4. Import the database schema and sample data:
   - Connect to your database using a PostgreSQL client (e.g., psql, pgAdmin)
   - Run the SQL commands from `expense_db_postgres.sql`

### 2. Backend Deployment

1. In Render dashboard, go to "New" > "Web Service"
2. Connect your GitHub repository or use the "Upload" option
3. Configure the service:
   - Name: expense-tracker-backend
   - Root Directory: backend
   - Runtime: Python 3
   - Build Command: `pip install -r ../requirements.txt`
   - Start Command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
4. Add environment variables:
   - DB_HOST: [Your Render PostgreSQL host]
   - DB_PORT: 5432
   - DB_USER: expense_user
   - DB_PASSWORD: [Your Render PostgreSQL password]
   - DB_NAME: expense_manager
5. Click "Create Web Service"

### 3. Frontend Deployment

1. In Render dashboard, go to "New" > "Web Service"
2. Connect your GitHub repository or use the "Upload" option
3. Configure the service:
   - Name: expense-tracker-frontend
   - Root Directory: frontend
   - Runtime: Python 3
   - Build Command: `pip install -r ../requirements.txt`
   - Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Add environment variables:
   - STREAMLIT_SERVER_PORT: $PORT
5. Add secret files:
   - Path: `.streamlit/secrets.toml`
   - Content:
     ```
     [db_credentials]
     url = "postgresql://expense_user:YOUR_PASSWORD@YOUR_HOST:5432/expense_manager"
     ```
6. Click "Create Web Service"

### 4. Connecting Frontend to Backend

If your frontend needs to communicate with the backend API:

1. Add an environment variable to the frontend service:
   - BACKEND_URL: [Your backend service URL]
2. Update your frontend code to use this URL for API requests

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up a local PostgreSQL database and import the schema
4. Configure environment variables in `.env` and `.streamlit/secrets.toml`
5. Run the backend: `cd backend && uvicorn server:app --reload`
6. Run the frontend: `cd frontend && streamlit run app.py`

## License

[MIT License](LICENSE)

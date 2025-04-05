#!/usr/bin/env python3
"""
Deployment helper script for the Financial Habit Tracking Application.
This script helps prepare the application for deployment to Render.com.
"""

import os
import argparse
import shutil
import subprocess
import sys

def check_requirements():
    """Check if all required tools are installed."""
    print("Checking requirements...")
    
    try:
        subprocess.run(["pip", "--version"], check=True, stdout=subprocess.PIPE)
        print("✅ pip is installed")
    except (subprocess.SubprocessError, FileNotFoundError):
        print("❌ pip is not installed")
        return False
    
    try:
        subprocess.run(["psql", "--version"], check=True, stdout=subprocess.PIPE)
        print("✅ PostgreSQL client is installed")
    except (subprocess.SubprocessError, FileNotFoundError):
        print("⚠️ PostgreSQL client is not installed (needed for database import)")
    
    return True

def prepare_backend(db_host, db_user, db_password):
    """Prepare the backend for deployment."""
    print("\nPreparing backend...")
    
    # Create .env file
    env_path = os.path.join("backend", ".env")
    with open(env_path, "w") as f:
        f.write(f"""# Database connection
DB_HOST={db_host}
DB_PORT=5432
DB_USER={db_user}
DB_PASSWORD={db_password}
DB_NAME=expense_manager

# API settings
PORT=8000
""")
    print(f"✅ Created {env_path}")
    
    return True

def prepare_frontend(db_url):
    """Prepare the frontend for deployment."""
    print("\nPreparing frontend...")
    
    # Create .streamlit/secrets.toml
    secrets_dir = ".streamlit"
    if not os.path.exists(secrets_dir):
        os.makedirs(secrets_dir)
    
    secrets_path = os.path.join(secrets_dir, "secrets.toml")
    with open(secrets_path, "w") as f:
        f.write(f"""# PostgreSQL connection details for Render.com
[db_credentials]
url = "{db_url}"
""")
    print(f"✅ Created {secrets_path}")
    
    return True

def import_database(db_host, db_port, db_user, db_password, db_name):
    """Import the database schema and sample data."""
    print("\nImporting database schema and sample data...")
    
    try:
        # Create a temporary file with the PGPASSWORD to avoid password prompt
        env = os.environ.copy()
        env["PGPASSWORD"] = db_password
        
        # Run the psql command to import the schema
        cmd = [
            "psql", 
            "-h", db_host,
            "-p", db_port,
            "-U", db_user,
            "-d", db_name,
            "-f", "expense_db_postgres.sql"
        ]
        
        result = subprocess.run(cmd, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ Database schema and sample data imported successfully")
        return True
    except subprocess.SubprocessError as e:
        print(f"❌ Failed to import database schema: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Deploy the Financial Habit Tracking Application")
    parser.add_argument("--db-host", required=True, help="PostgreSQL host")
    parser.add_argument("--db-port", default="5432", help="PostgreSQL port")
    parser.add_argument("--db-user", default="expense_user", help="PostgreSQL username")
    parser.add_argument("--db-password", required=True, help="PostgreSQL password")
    parser.add_argument("--db-name", default="expense_manager", help="PostgreSQL database name")
    parser.add_argument("--import-db", action="store_true", help="Import database schema and sample data")
    
    args = parser.parse_args()
    
    # Check requirements
    if not check_requirements():
        print("Please install the required tools and try again.")
        sys.exit(1)
    
    # Construct the database URL
    db_url = f"postgresql://{args.db_user}:{args.db_password}@{args.db_host}:{args.db_port}/{args.db_name}"
    
    # Prepare backend
    if not prepare_backend(args.db_host, args.db_user, args.db_password):
        print("Failed to prepare backend.")
        sys.exit(1)
    
    # Prepare frontend
    if not prepare_frontend(db_url):
        print("Failed to prepare frontend.")
        sys.exit(1)
    
    # Import database if requested
    if args.import_db:
        if not import_database(args.db_host, args.db_port, args.db_user, args.db_password, args.db_name):
            print("Failed to import database.")
            sys.exit(1)
    
    print("\n✅ Deployment preparation completed successfully!")
    print("\nNext steps:")
    print("1. Deploy the backend to Render.com")
    print("2. Deploy the frontend to Render.com")
    print("3. Update the frontend with the backend URL if needed")
    print("\nSee README.md for detailed deployment instructions.")

if __name__ == "__main__":
    main()
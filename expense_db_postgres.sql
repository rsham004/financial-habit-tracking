-- PostgreSQL version of the expense_manager database

-- Create database (this is typically done through the Render interface)
-- CREATE DATABASE expense_manager;

-- Connect to the database
-- \c expense_manager

-- Table structure for table expenses
DROP TABLE IF EXISTS expenses;

CREATE TABLE expenses (
  id SERIAL PRIMARY KEY,
  expense_date DATE NOT NULL,
  amount FLOAT NOT NULL,
  category VARCHAR(255) NOT NULL,
  notes TEXT
);

-- Sample data for the expenses table
INSERT INTO expenses (expense_date, amount, category, notes) VALUES
('2024-08-02', 50, 'Entertainment', 'Movie tickets'),
('2024-08-02', 150, 'Shopping', 'New shoes'),
('2024-08-03', 100, 'Food', 'Dinner at a restaurant'),
('2024-08-02', 400, 'Food', 'Groceries for the week'),
('2024-08-02', 80, 'Entertainment', 'Concert tickets'),
('2024-08-02', 100, 'Shopping', 'Clothes'),
('2024-08-02', 50, 'Other', 'Gasoline'),
('2024-08-03', 60, 'Food', 'Dinner at a restaurant'),
('2024-08-03', 20, 'Entertainment', 'Video rental'),
('2024-08-03', 120, 'Shopping', 'Gadgets'),
('2024-08-03', 15, 'Other', 'Coffee'),
('2024-08-04', 25, 'Food', 'Lunch'),
('2024-08-04', 200, 'Shopping', 'Home supplies'),
('2024-08-04', 10, 'Other', 'Parking'),
('2024-08-05', 350, 'Rent', 'Shared rent payment'),
('2024-08-05', 40, 'Food', 'Snacks'),
('2024-08-05', 75, 'Entertainment', 'Theater tickets'),
('2024-08-05', 100, 'Shopping', 'Books'),
('2024-08-05', 15, 'Other', 'Miscellaneous'),
('2024-08-06', 30, 'Food', 'Breakfast'),
('2024-08-06', 100, 'Shopping', 'Shoes'),
('2024-08-06', 80, 'Entertainment', 'Movies'),
('2024-08-06', 15, 'Other', 'Public transport'),
('2024-09-01', 1200, 'Rent', 'Monthly rent payment'),
('2024-09-01', 300, 'Food', 'Groceries for the week'),
('2024-09-01', 50, 'Entertainment', 'Movie tickets'),
('2024-09-01', 150, 'Shopping', 'New shoes'),
('2024-09-01', 20, 'Other', 'Bus fare'),
('2024-09-02', 400, 'Food', 'Groceries for the week'),
('2024-09-02', 80, 'Entertainment', 'Concert tickets'),
('2024-09-02', 100, 'Shopping', 'Clothes'),
('2024-09-02', 50, 'Other', 'Gasoline'),
('2024-09-03', 60, 'Food', 'Dinner at a restaurant'),
('2024-09-03', 20, 'Entertainment', 'Video rental'),
('2024-09-03', 120, 'Shopping', 'Gadgets'),
('2024-09-03', 15, 'Other', 'Coffee'),
('2024-09-04', 25, 'Food', 'Lunch'),
('2024-09-04', 200, 'Shopping', 'Home supplies'),
('2024-09-04', 10, 'Other', 'Parking'),
('2024-09-05', 350, 'Rent', 'Shared rent payment'),
('2024-09-05', 40, 'Food', 'Snacks'),
('2024-09-05', 75, 'Entertainment', 'Theater tickets'),
('2024-09-05', 100, 'Shopping', 'Books'),
('2024-09-05', 15, 'Other', 'Miscellaneous'),
('2024-09-30', 1000, 'Rent', 'Monthly rent payment'),
('2024-09-30', 250, 'Food', 'Groceries for the week'),
('2024-09-30', 40, 'Entertainment', 'Cinema tickets'),
('2024-09-30', 100, 'Shopping', 'Clothes'),
('2024-09-30', 20, 'Other', 'Public transport'),
('2024-08-15', 10, 'Shopping', 'Bought potatoes'),
('2024-08-01', 1227, 'Rent', 'Monthly rent payment'),
('2024-08-01', 300, 'Food', 'Groceries for the week'),
('2024-08-01', 1200, 'Rent', 'Monthly rent payment'),
('2024-08-01', 300, 'Food', 'Groceries for the week');
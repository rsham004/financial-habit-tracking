import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
	connection = mysql.connector.connect(
		host="codebasics-db.chsy4soomg0u.ap-southeast-2.rds.amazonaws.comcodebasics-db.chsy4soomg0u.ap-southeast-2.rds.amazonaws.com",
		user="root",
		password="iRGjzcZ5TcLhfnH5ssyc",
		database="codebasics-db"
	)

	cursor = connection.cursor(dictionary=True)
	yield cursor

	if commit:
		connection.commit()
	# print("Closing cursor")
	cursor.close()
	connection.close()


# def fetch_all_records():
#     query = "SELECT * from expenses"
#
#     with get_db_cursor() as cursor:
#         cursor.execute(query)
#         expenses = cursor.fetchall()
#         for expense in expenses:
#             print(expense)


def fetch_expenses_for_date(expense_date):
	logger.info(f"fetch_expenses_for_date called with {expense_date}")
	with get_db_cursor() as cursor:
		cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
		print(f"Executing query:  with parameter: {expense_date}")
		expenses = cursor.fetchall()
		print(f"Query returned {len(expenses)} results")
		for expense in expenses:
			print(expense)
	return expenses


def insert_expense(expense_date, amount, category, notes):
	logger.info(f"insert_expense called with {expense_date} and data amount :{amount}, category : {category}, notes : {notes}")
	with get_db_cursor(commit=True) as cursor:
		cursor.execute(
			"INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
			(expense_date, amount, category, notes)
		)


def delete_expenses_for_date(expense_date):
	logger.info(f"delete_expenses_for_date called with {expense_date}")
	with get_db_cursor(commit=True) as cursor:
		cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date, end_date):
	logger.info(f"fetch_expense_summary called with start:{start_date} end: {end_date}")
	with get_db_cursor() as cursor:
		cursor.execute(
			'''select category, SUM(amount) as Total
				from expense_manager.expenses
				WHERE expense_date
				BETWEEN %s AND %s 
				GROUP BY category''',
			(start_date, end_date)
		)
		data = cursor.fetchall()
	return data

def fetch_expense_summary_by_month():
	logger.info(f"fetch_expense_summary_by_month called ")

	with get_db_cursor() as cursor:
		cursor.execute(
			''' SELECT 
				MONTHNAME(expense_date) AS month,  
				SUM(amount) AS Total
				FROM expense_manager.expenses
				GROUP BY  month 
				ORDER BY STR_TO_DATE(month, '%b') 
				''',
			)
		data = cursor.fetchall()
	return data

if __name__ == "__main__":
	pass
	# expenses = fetch_expenses_for_date("2024-08-25")
	# print("***",expenses)
	# insert_expense("2024-08-25",40,"Alcohol","Jack Daniels")
	# insert_expense("2024-08-25",40,"Narcotics","Cocaine")
	# delete_expenses_for_date("2024-08-21")
	# summary = fetch_expense_summary("2024-08-24","2024-08-25")
	# for item in summary:
	# 	print (item)

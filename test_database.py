from database.db_connection import execute_query

rows = execute_query("SELECT GETDATE()")

print(rows[0][0])

print("Database Connected Successfully")
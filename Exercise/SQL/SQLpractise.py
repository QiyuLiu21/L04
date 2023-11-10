import sqlite3

def sql_connection():
  try:
    conn = sqlite3.connect('customers.db')
    return conn
  except:
    print("Error connecting to Database")

def sql_table(conn):
  cursor_obj = conn.cursor()
  cursor_obj.execute("INSERT INTO employees VALUES(1, 'Sarah','30000','Reserch','Analystist','2021')")
  conn.commit()

conn = sql_connection()
sql_table(conn)
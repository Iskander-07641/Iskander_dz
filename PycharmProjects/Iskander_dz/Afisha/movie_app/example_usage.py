from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table;")
results = cursor.fetchall()
cursor.close()
conn.close()
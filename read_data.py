import sqlite3

#Connect to the data base
def connect_to_db():
    conn = sqlite3.connect('db_api.db')
    return conn

#Read data from each table
def read_data(table_name):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table_name)
    rows = cur.fetchall()
    for row in rows:
        print(row)

#read_data("DEPARTMENTS")
#print("-----------")
#read_data("JOBS")
#print("-----------")
read_data("EMPLOYEES")
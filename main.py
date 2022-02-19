import os
import psycopg2

HOST = 'localhost'
DB_NAME = 'test'
DB_USER = 'postgres'
DB_PASS = 'Cnfhbr09!'
size = 1_048_576 * 210

file = open("1.txt", "w")
file.write((str(os.urandom(size))))
file.close()

# Подлючаемся к базе
conn = psycopg2.connect(host=HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
curs = conn.cursor()

# curs.execute("CREATE TABLE t_file (name text, oid_number oid);")
sql_file_add = """INSERT INTO t_file VALUES ('2.txt', lo_import('C:/PY/test/1.txt'))"""
curs.execute(sql_file_add)

curs.execute("SELECT lo_export(16494, 'C:/PY/test/2.txt');")
conn.commit()

curs.close()
conn.close()

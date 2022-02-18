import psycopg2

HOST = 'localhost'
DB_NAME = 'test'
DB_USER = 'user_db'
DB_PASS = 'password'

# Подлючаемся к базе
conn = psycopg2.connect(host=HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
curs = conn.cursor()

sql_size = curs.execute("SELECT pg_size_pretty( pg_database_size('test') );")
file = psycopg2.Binary(open('1.exe', 'rb').read())

# curs.execute("CREATE TABLE file (bin bytea);")
sql_file_add = """INSERT INTO file VALUES (%s);""" % file

curs.execute(sql_file_add)
conn.commit()
curs.close()
conn.close()

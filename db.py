import psycopg2 as pg
import csv

file = r'/upload/20191208-191546.csv'
sql_insert = """INSERT INTO prometheushistory(name,
timestamp,
value,
host,
instance,
job,
process_name,
systemd_unit,
user,
cpu,
alertname,
alertstate,
client,
queue_name,
severity,
pidfile,
name_1,
device,
fstype,
mode,
path,
quantile)
                VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"""
try:
    conn = pg.connect(user="",
        password="",
        host="",
        port="5432",
        database="")
    cursor = conn.cursor()
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader) # This skips the 1st row which is the header.
        for record in reader:
            cursor.execute(sql_insert, record)
            conn.commit()
except (Exception, pg.Error) as e:
    print(e)
finally:
    if (conn):
        cursor.close()
        conn.close()
        print("Connection closed.")

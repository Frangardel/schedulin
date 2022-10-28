import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json

user = 'FRANGARC'
passw = 'Noviembre2022'
host = 'FRANGARC.mysql.pythonanywhere-services.com'
database = "FRANGARC$schedulin"

db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
conn = db.connect()

tables = conn.execute(
 "SHOW TABLES;"
)

for table in tables.fetchall():
    print(table)

conn.close()
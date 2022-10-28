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

create_sql = """
    CREATE TABLE vecino (
            id int,
            name varchar(255),
            email varchar(255),
            status varchar(10)
);
"""

conn.execute(create_sql)

create_sql = """
    CREATE TABLE resource (
            id int,
            type varchar(255),
            max_pax int,
            price float,
            id_timetable int,
            in_advance int
);
"""

conn.execute(create_sql)

create_sql = """
    CREATE TABLE timetable (
            id int,
            start time,
            end time
);
"""

conn.execute(create_sql)

create_sql = """
    CREATE TABLE reservation (
            id int,
            id_resource int,
            id_vecino int,
            status varchar(10),
            start time,
            num_pax int
);
"""

conn.execute(create_sql)

tables = conn.execute(
 "SHOW TABLES;"
)

for table in tables.fetchall():
    print(table)

conn.close()
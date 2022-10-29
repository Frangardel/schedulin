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

timetable_creation = """
    CREATE TABLE IF NOT EXISTS timetable (
        id INT AUTO_INCREMENT PRIMARY KEY,
        start_time TIME,
        end_time TIME,
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP
    )  ENGINE=INNODB;
"""
resource_creation = """
    CREATE TABLE IF NOT EXISTS resource (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timetable_id INTEGER,
        type VARCHAR(255),
        description VARCHAR(2000),
        max_pax INTEGER,
        price DECIMAL(4, 2),
        hours_in_advance INTEGER,
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP,
        FOREIGN KEY(timetable_id) REFERENCES timetable(id)
    )  ENGINE=INNODB;
"""
user_creation = """
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        status VARCHAR(255),
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP
    )  ENGINE=INNODB;
"""

reservation_creation = """
    CREATE TABLE IF NOT EXISTS reservation (
        id INT AUTO_INCREMENT PRIMARY KEY,
        resource_id INTEGER,
        user_id INTEGER,
        start_time TIME,
        num_pax INTEGER,
        status VARCHAR(255),
        creation_date TIMESTAMP,
        modification_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deletion_date TIMESTAMP,
        FOREIGN KEY(resource_id) REFERENCES resource(id),
        FOREIGN KEY(user_id) REFERENCES user(id)
    )  ENGINE=INNODB;
"""

conn.execute(timetable_creation)
conn.execute(resource_creation)
conn.execute(user_creation)
conn.execute(reservation_creation)

tables = conn.execute(
 "SHOW TABLES;"
)

for table in tables.fetchall():
    print(table)

conn.close()

"""
SELECT 
    r.id AS reservation_id,
    r.status AS reservation_status,
    u.name AS user_name,
    u.email AS user_email,
    re.type AS resource_type,
FROM (
    SELECT id, status, user_id, resource_id
    FROM reservation) AS r
LEFT JOIN (
    SELECT id, name, email
    FROM user) AS u 
ON r.user_id = u.id
LEFT JOIN (
    SELECT resource.id, resource.type, timetable.start_time,timetable.end_time,
    FROM resource
    LEFT JOIN timetable
    ON resource.timetable_id = timetable.id) AS re 
ON r.resource_id = re.id;
"""

"""
SELECT
    r.id AS reservation_id,
    r.date AS reservation_id,
    r.status AS reservation_status,
    u.name AS user_name,
    u.email AS user_email,
    re.type AS resource_type,
    re.price AS price,
    t.start_time,
    t.end_time
FROM (
SELECT id, status, user_id, resource_id, date
    FROM reservation) AS r
LEFT JOIN (
    SELECT id, name, email
    FROM user) AS u
ON r.user_id = u.id
LEFT JOIN (
    SELECT id, type, price, timetable_id
    FROM resource) AS re
ON r.resource_id = re.id
LEFT JOIN (
    SELECT id, start_time, end_time
    FROM timetable) AS t
ON re.timetable_id = t.id;
"""
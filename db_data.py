import pymysql
from sqlalchemy import create_engine
from datetime import datetime

user = 'FRANGARC'
passw = 'Noviembre2022'
host = 'FRANGARC.mysql.pythonanywhere-services.com'
database = "FRANGARC$schedulin"

db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
conn = db.connect()

now = datetime.now()

timetables_lst = [
    """INSERT INTO timetable (start_time, end_time, creation_date)
           VALUES ('09:00:00', '10:30:00', '{0}')""".format(now),
    """INSERT INTO timetable (start_time, end_time, creation_date)
           VALUES ('10:30:00', '12:00:00', '{0}')""".format(now),
    ]

resources_lst = [
    """INSERT INTO resource (timetable_id, type, description, max_pax, price, hours_in_advance, creation_date)
           VALUES (1, 'PADEL', '', 4, 0.50, 24, '{0}')""".format(now),
    """INSERT INTO resource (timetable_id, type, description, max_pax, price, hours_in_advance, creation_date)
           VALUES (2, 'PADEL', '', 4, 0.75, 24, '{0}')""".format(now),
    ]

users_lst = [
    """INSERT INTO user (name, email, status, creation_date)
           VALUES ('John Doe', 'johndoe@mail.com', 'ACTIVE', '{0}')""".format(now),
    ]

reservations_lst = [
    """INSERT INTO reservation (resource_id, user_id, start_time, num_pax, status, creation_date)
           VALUES (1, 1, '09:00:00', 2, 'CONFIRMED', '{0}')""".format(now),
    ]

inserts_lst = [timetables_lst, resources_lst, users_lst, reservations_lst]


for lst in inserts_lst:
    for t in lst:
        print(t)
        conn.execute(t)


alter_sql = """
            ALTER TABLE reservation
            ADD date DATE;
            """

conn.execute(alter_sql)

update_sql = """
            UPDATE reservation
            SET date = '2022-10-31'
            WHERE id = 1;
            """

conn.execute(update_sql)

conn.close()
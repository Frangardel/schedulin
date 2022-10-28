
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, send_file, request
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json

user = 'FRANGARC'
passw = 'qazQAZ123'
host = 'FRANGARC.mysql.pythonanywhere-services.com'
database = "FRANGARC$foodb"

app = Flask(__name__)

def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

@app.route('/')
def home():
    # img_path = "/home/automato/website/img/home.gif"
    # return send_file(img_path, mimetype = 'image/gif')
    return "pythonreturnanywhere"
from os import path
from flask_login import UserMixin
from . import db
import sqlite3 as sql

ROOT = path.dirname(path.relpath((__file__)))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

def create_post(price, content, user_name):
    con = sql.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (price, content, user_name) values(?, ?, ?)', (price, content, user_name))
    con.commit()
    con.close()
    
def get_posts():
    con = sql.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts
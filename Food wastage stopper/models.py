from os import path
from flask_login import UserMixin
from . import User_details
import sqlite3 as sql

ROOT = path.dirname(path.relpath((__file__)))

class User(UserMixin, User_details.Model):
    id = User_details.Column(User_details.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = User_details.Column(User_details.String(100), unique=True)
    password = User_details.Column(User_details.String(100))
    name = User_details.Column(User_details.String(1000))

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
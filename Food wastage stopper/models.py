from os import path
from flask_login import UserMixin
from . import User_details
import sqlite3 as sql
from sqlite3 import Error

ROOT = path.dirname(path.relpath((__file__)))

class User(UserMixin, User_details.Model):
    id = User_details.Column(User_details.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = User_details.Column(User_details.String(100), unique=True)
    password = User_details.Column(User_details.String(100))
    name = User_details.Column(User_details.String(1000))
    
# def convert_back_into_image():
#     image = Image.open('Also_speed.png')
#     images = image.show()
#     print(image)
#     print(images)
#     return images
    
def get_contents():
    con = sql.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    database = cur.execute('select * from posts')
    price = ''
    content = ''
    user_name = ''
    title = ''
    file_name =''
    for x in database:
        price += (f' {x[1]}')
        content += (f' {x[2]}')
        user_name += (f' {x[3]}')
        title += (f' {x[4]}')
        file_name += (f' {x[5]}') 
    return price, content, user_name, title, file_name

def get_posts():
    con = sql.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

def convert_into_binary(file_path):
    with open(file_path, 'rb') as file:
        binary = file.read()
        return binary
    
def read_blob_data(entry_id):
    try:
        conn = sql.connect('food_database.db')
        cur = conn.cursor()
        sql_fetch_blob_query = 'SELECT * from posts where id = ?' 
        cur.execute(sql_fetch_blob_query, (entry_id,))
        record = cur.fetchall()
        for row in record:
            converted_file_name = row[1]
            photo_binarycode = row[2]
            last_slash_index = converted_file_name.rfind("/") + 1
            final_file_name = converted_file_name[last_slash_index:]
            write_to_file(photo_binarycode, final_file_name)
        cur.close()
    except sql.Error as error:
        print('[INFO] " Failed to read blob data from sqlite table', error)
    finally:
        if conn:
            conn.close()

def write_to_file(binary_data, file_name):
    with open(file_name, 'wb') as files:
        files.write(binary_data.encode('utf-8'))
    print('[DATA] : The following file has been writen to the project directory: ', file_name)

def insert_into_database(price, content, user_name, title, filename, file_blob):
    try:
        conn = sql.connect('food_database.db')
        cur = conn.cursor()
        sql_insert_file_query = 'INSERT INTO posts(price, content, user_name, title, file_name, file_blob) VALUES(?, ?, ?, ?, ?, ?)'
        cur = conn.cursor()
        cur.execute(sql_insert_file_query, (price, content, user_name, title, filename, file_blob, ))
        conn.commit()
        print('[INFO] : The blob for ', filename, 'is in the database.')
        last_updated_entry = cur.lastrowid
        return last_updated_entry
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        else:
            error = 'Oh shucks, something is wrong here.'

def create_post(price, content, user_name, title, filename):
    file_blob = convert_into_binary(fr'C:\Users\ethan\Documents\food_wastage_stopper\Food wastage stopper\static\Images\{filename}')
    # Assigning the file to a variable.
    last_updated_entry = insert_into_database(price, content, user_name, title, filename, file_blob)
    read_blob_data(last_updated_entry) 

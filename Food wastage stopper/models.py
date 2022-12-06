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
    # Assigning each variable to the column it is part of as part of the loging in mechanism.
    
def get_filenames():
    con = sql.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    database = cur.execute('select * from posts')
    file_name =''
    for x in database:
        file_name += (f' {x[5]}')
        # Adding the whole column for file_names to the filename variable.
    return file_name

def get_content():
    con = sql.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    content = cur.fetchall()
    return content
    # Returning the whole database as a variable with each element in the content variable as an entire row in the database.

def get_database():
    con = sql.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    database = cur.execute('select * from posts')
    return database
    # Returning the whole database as a variable with each element in the database variable as an entire column in the database.

def get_bids():
    con = sql.connect('Bidding.db')
    cur = con.cursor()
    content = cur.execute('select * from Bids')
    return content
    # Assigning the whole database column by column to the content variable.

def bid_comments(post_part_of):
    post_parts_of = []
    for x in post_part_of:
        post_parts_of.append(x[3])
        # Adding all the post_part_of or what post the bid is for to a list. 
    number_of_occurances = []
    # Assigning every post_parts_of to post_part_of.
    unique_post_values = list(dict.fromkeys(post_parts_of))
    # Adding all unique values of post_parts_of to unique_post_values.
    number_unique_elements = len(unique_post_values)
    # Adding the amount of unique numbers.
    for x in range(0, number_unique_elements):
        number_of_occurances.append(post_parts_of.count(unique_post_values[x]))
        # Adding the amount every value comes up to number_of_occurances.
    return unique_post_values, number_of_occurances

def create_bid(price, information, post_ID, user_name):
    con = sql.connect('Bidding.db')
    cur = con.cursor()
    cur.execute('insert into Bids (user_name, comment, post_part_of, price) values(?, ?, ?, ?)', (user_name, information, post_ID, price))
    con.commit()
    con.close()
    # Just to create a bid for content.

def convert_into_binary(file_path):
    with open(file_path, 'rb') as file:
        binary = file.read()
        return binary
    # Converting image to binary to be stored.
    
def read_blob_data(entry_id):
    try:
        conn = sql.connect('food_database.db')
        cur = conn.cursor()
        sql_fetch_blob_query = 'SELECT * from posts where id = ?' 
        cur.execute(sql_fetch_blob_query, (entry_id,))
        record = cur.fetchall()
        # Connecting to database and storing the database variable in record.
        for row in record:
            converted_file_name = row[1]
            photo_binarycode = row[2]
            # Assigning the binary code to photo_binarycode and filename to converted_file_name.
            last_slash_index = converted_file_name.rfind("/") + 1
            final_file_name = converted_file_name[last_slash_index:]
            # Getting the price of the post
            write_to_file(photo_binarycode, final_file_name)
        cur.close()
        #  Connecting to the database and copying newly created post and putting it into file system.
    except sql.Error as error:
        print('[INFO] " Failed to read blob data from sqlite table', error)
    finally:
        if conn:
            conn.close()
 
def write_to_file(binary_data, file_name):
    with open(file_name, 'wb') as files:
        files.write(binary_data.encode('utf-8'))
    print('[DATA] : The following file has been writen to the project directory: ', file_name)
    # Creating the file of the newly created post.

def insert_into_database(price, content, user_name, title, filename, file_blob):
    try:
        conn = sql.connect('food_database.db')
        cur = conn.cursor()
        sql_insert_file_query = 'INSERT INTO posts(price, content, user_name, title, file_name, file_blob) VALUES(?, ?, ?, ?, ?, ?)'
        cur = conn.cursor()
        cur.execute(sql_insert_file_query, (price, content, user_name, title, filename, file_blob, ))
        conn.commit()
        print('[INFO] : The blob for ', filename, 'is in the database.')
        # Inserting the post into the database
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

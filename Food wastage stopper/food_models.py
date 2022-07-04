import sqlite3
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values( ?, ?)',(name, content))
    con.commit()
    con.close()
    # To create a new post.

def get_posts():
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * FROM posts')
    posts = cur.fetchall()
    print(posts)
    return posts
    # To send all the database data to the front end.

def remove_post(id):
    db = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    c = db.cursor()
    c.execute('DELETE FROM posts WHERE id = ?;',id)
    db.commit()
    db.close()
    print('Post was removed')
    return ('Your post was removed') # To bring user back to frontpage. 
    # Removing the post.
    
def print_posts():
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    posts = cur.fetchall()
    print(posts) # Posting all the posts to the terminal within the database.
    # To print all the posts in the database.

def create_users(user_name, password):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values( ?, ?)',(user_name, password))
    con.commit()
    con.close()
    # Creating new user code.
    
    



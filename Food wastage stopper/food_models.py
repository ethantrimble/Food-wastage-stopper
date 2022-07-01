import sqlite3
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values( ?, ?)',(name, content))
    con.commit()
    con.close()
 
def get_posts():
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

def remove_post(id):
    db = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    c = db.cursor()
    c.execute('DELETE FROM posts WHERE id = ?;',id)
    db.commit()
    db.close()
    print('Post was removed')
    return ('Your post was removed') # To bring user back to frontpage. 
    
def print_posts():
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    posts = cur.fetchall()
    print(posts) # Posting all the posts to the terminal within the database.
    print("endofposts")

# def create_users():
    



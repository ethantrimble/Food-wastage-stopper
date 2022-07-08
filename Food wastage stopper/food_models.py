import sqlite3
from os import curdir, path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values( ?, ?)',(name, content))
    con.commit()
    con.close()
    # To create a new post.
    lastest_post_Id = splitListOfposts()[-1]
    print(lastest_post_Id)

def get_posts():
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * FROM posts')
    posts = cur.fetchall()
    return posts
    # To send all the database data to the front end.

def remove_post(id):
    db = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    c = db.cursor()
    c.execute('DELETE FROM posts WHERE id = ?;',id)
    db.commit()
    db.close()

def splitListOfTuples(lst):
  lst1 = []
  lst2 = []
  lst3 = []
  for x, y, z in lst:
    lst1.append(x)
    lst2.append(y)
    lst3.append(z)
  return (lst1, lst2, lst3)

def splitListOfposts():
    x, y, z = splitListOfTuples(get_posts())
    return(x)

def create_users(user_name, password):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('insert into users (user_name, password) values( ?, ?)',(user_name, password))
    con.commit()
    con.close()
    # Creating new user code.

def get_users():
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * FROM users')
    users = cur.fetchall()
    return users
    # To send all the database data to the front end.

def remove_post(id):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur= con.cursor()
    cur.execute('DELETE FROM posts WHERE id = ?', id)
    con.commit()
    con.close()
    
    



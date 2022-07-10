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
    lastest_post_Id = splitListOfposts_x()[-1]
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

def splitListOfposts_x():
    x, y, z = splitListOfTuples(get_posts())
    return(x)
def splitListOfposts_y():
    x, y, z = splitListOfTuples(get_posts())
    return(y)
def splitListOfposts_z():
    x, y, z = splitListOfTuples(get_posts())
    return(z)
def splitListOfusers_y():
    x, y, z = splitListOfTuples(get_users(None))
    return y
def splitListOfusers_z():
    x, y, z = splitListOfTuples(get_users(None))
    return z

def create_users(user_name, password):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('insert into users (user_name, password) values( ?, ?)',(user_name, password))
    con.commit()
    con.close()
    # Creating new user code.

def get_users(id):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur = con.cursor()
    cur.execute('select * FROM users')
    users = cur.fetchall()
    if(id != None):
        return users[id]
    if(id == None):
        return users
    # To send all the database data to the front end.

def remove_post(id):
    con = sqlite3.connect(path.join(ROOT, 'food_database.db'))
    cur= con.cursor()
    cur.execute('DELETE FROM posts WHERE id = ?', id)
    con.commit()
    con.close()
    
    



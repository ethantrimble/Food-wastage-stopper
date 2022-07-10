from contextlib import nullcontext
from pdb import post_mortem
from sqlite3 import dbapi2
from flask import Flask, render_template, request
from flask_cors import CORS
from food_models import create_post, get_posts, remove_post, create_users, get_users, splitListOfusers_y, splitListOfusers_z

app = Flask(__name__)

CORS(app)
    
@app.route('/', methods=['GET','POST','DELETE']) 
def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        if 'submit_post' in request.form:
            name = request.form.get('name')
            post = request.form.get('post')
            create_post(name, post)
        elif 'print_posts' in request.form:
            print(get_posts(),'printed get posts start page')
        else:
            print('malformed post start page')
            # unknown

    if request.method == 'DELETE':
        if 'delete_post' in request.form:
            print('delete post front page')
            remove_post(-1)
        # To delete a post.

    posts = get_posts()

    return render_template('food_index.html', posts=posts)

@app.route('/user_signup', methods=['GET','POST'])
def signup():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        if 'submit_user_details' in request.form:
            user_name = request.form.get('name')
            password = request.form.get('password')
            create_users(user_name, password)
        elif 'print_users' in request.form:
            print(get_users(None))
        else:
            print('malformed for page signup post')
    users = get_users(None)
    
    return render_template('user_signup.html', users=users)

@app.route('/user_sign_in', methods=['GET','POST'])
def login():
    	
    users = get_users(None)
    users_y = splitListOfusers_y()
    users_z = splitListOfusers_z()
    if request.method == 'GET':
        pass
    signedin = 'Either password or username is incorrect'
    if request.method == 'POST':
        if 'sig_in' in request.form:
            Name = request.form.get('name')
            Password = request.form.get('password')
            print(Name,' name and password ',Password)
            for i in range(len(users)):
                if(users_y[i] == Name and users_z[i] == Password):
                    signedin = 'You are signed in'
    

    return render_template('user_sign_in.html', signedin=signedin)

if __name__ == '__main__':
    app.run(debug=True)


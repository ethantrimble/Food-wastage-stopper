from contextlib import nullcontext
from pdb import post_mortem
from sqlite3 import dbapi2
from flask import Flask, render_template, request
from flask_cors import CORS
from food_models import create_post, create_users, get_posts, get_users, remove_post

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
        else:
            print('malformed post start page')
            # unknown

    if request.method == 'DELETE':
        if 'delete_post' in request.form:
            name = request.form.get('name')
            post = request.form.get('post')
            remove_post(name, post)
        # To delete a post.

    posts = get_posts()

    return render_template('food_index.html', posts=posts)

@app.route('/user_signup', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        print('pass get login page')
        pass

    if request.method == 'POST':
        if 'submit_user_details' in request.form:
            user_name = request.form.get('name')
            password = request.form.get('password')
            create_users(user_name, password)
        elif 'print_users' in request.form:
            print(get_users())
        else:
            print('malformed for page signup post')
    users = get_users()
    
    return render_template('user_signup.html', users=users)

# @app.route('/delete/<int:id>')
# def delete(id, food_database):
#     page_to_delete = post_mortem.query.get_or_404(name, content) # To assign the delete function to the intented post.
#     name = Noneform=UserForm()

#     try:
#         db.session.delete(page_to_delete)
#         db.session.commit()

#         our_users = Users.query.order_by(User.)
#         return render_template("add_user.html",

#     except:
#         print("Whoops error")
#         return render_template("add_user.html",)

#     # return render_template('food_index.html')
 
if __name__ == '__main__':
    app.run(debug=True)


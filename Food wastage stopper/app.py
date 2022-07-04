from contextlib import nullcontext
from pdb import post_mortem
from sqlite3 import dbapi2
from flask import Flask, render_template, request
from flask_cors import CORS
from food_models import create_post, get_posts, remove_post, print_posts

app = Flask(__name__)

CORS(app)
    
@app.route('/', methods=['GET','POST','DELETE']) 
def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        if 'print_posts' in request.form:
            print('Bye')
            print(get_posts)
        elif 'submit_post' in request.form:
            name = request.form.get('name')
            post = request.form.get('post')
            create_post(name, post)
            print('Hello')
        else:
            print("malformed")
            pass # unknown

    if request.method == 'DELETE':
        if 'delete_post' in request.form:
            name = request.form.get('name')
            post = request.form.get('post')
            remove_post(name, post)
            print('working')
        # To delete a post.

    posts = get_posts()

    return render_template('food_index.html', posts=posts)

@app.route('/user_signup', methods=['GET'])
def login():

    if request.method == 'GET':
        pass
    # if request.method == 'POST':
    
    return render_template('user_signup.html')

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


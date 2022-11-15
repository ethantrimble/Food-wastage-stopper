from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import get_posts, create_post

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# posts = get_posts()
# @main.route('/posts', methods=['GET','POST'])
# def post():

#     if request.method == 'GET':
#         pass

#     if request.method == 'POST':
#         price = request.form.get('price')
#         content = request.form.get('post')
#         user_name = current_user.name
#         create_post(price, content, user_name)

#     return render_template('posts.html', posts=posts)
# # To create posts and also redirect back to 'posts.html'.
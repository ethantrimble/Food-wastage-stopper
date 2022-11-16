from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from .models import create_post, get_posts

main = Blueprint('main', __name__)

@main.route('/')    
def home():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/posts', methods=['GET','POST'])
def posts():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        price = request.form.get('price')
        content = request.form.get('post')
        user_name = current_user.name
        create_post(price, content, user_name)

    return render_template('post.html', post=get_posts())
# To create posts and also redirect back to 'posts.html'.
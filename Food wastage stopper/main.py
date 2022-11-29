from flask import Blueprint, render_template, request, redirect, Flask, url_for
from flask_login import current_user, login_required

import os
from .models import create_post, get_posts
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = (r'C:\Users\ethan\Documents\food_wastage_stopper\Food wastage stopper\static\Images')
main = Blueprint('main', __name__)

@main.route('/')    
def home():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/post', methods=['POST','GET'])
def post():
    if request.method == 'POST':
        price = request.form.get('price')
        content = request.form.get('content')
        user_name = current_user.name
        title = request.form.get('title')
        image = request.files['file']
    
        if image.filename == '':
            print("File name is invalid")
            return redirect(request.url)
        
        filename = secure_filename(image.filename)
        # Assigning the name of the file to a variable.

        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))
        create_post(price, content, user_name, title, filename)

        return render_template('post.html',filename=filename,posts=get_posts())
    return render_template('post.html',posts=get_posts())
# To create posts and also redirect back to 'posts.html'.

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename = '/Images/' + filename, code=301))
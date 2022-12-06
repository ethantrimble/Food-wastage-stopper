from flask import Blueprint, render_template, request, redirect, Flask, url_for
from flask_login import current_user, login_required
import re

import os
from .models import create_post, get_content, get_filenames, create_bid, bid_comments, get_bids
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

@login_required
@main.route('/bidding',methods=['GET','POST'])
def bids():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        price = request.form.get('bidding price')
        information = request.form.get('information')
        post_ID = request.form.get('ID_value',"")
        print(post_ID)
        user_name = current_user.name
        create_bid(price, information, post_ID, user_name)

    bids = get_bids()
    bid = bid_comments(bids)
    # Importing all the data from the database.
    return render_template('bidding.html', name=current_user.name, post_part_of=bid[0], number_of_occurances=bid[1])

@main.route('/post', methods=['POST','GET'])
def post():
    content=get_content()[0]
    # Adding all the content in the database to the content variable.
    image_name = get_filenames()
    # Putting the image names into the variable image_names and the whole database into the content variable.

    pre_single_image_name = image_name.split(' ')
    # Splitting each image name into its own element.

    single_content = content[::-1]
    single_image_name = pre_single_image_name[::-1]
    # Moving the start element to the back and end to start and everything in between for each variable.

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
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"], filename))
        create_post(price, content, user_name, title, filename)

        return render_template('post.html',filename=filename, content=single_content, image_name=single_image_name)
    
    return render_template('post.html', content=single_content, image_name=single_image_name)
# To create posts and also redirect back to 'posts.html'.

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename = '/Images/' + filename, code=301))
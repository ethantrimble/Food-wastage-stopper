from flask import Blueprint, render_template, request, redirect, Flask, url_for
from flask_login import current_user, login_required
import re

import os
from .models import create_post, get_content, get_filenames, create_bid, bid_comments, get_bids, get_database
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
        print(post_ID + information + price)
        user_name = current_user.name
        create_bid(price, information, post_ID, user_name)
        # Creating post.

    bid = get_database()
    bids = []
    submission = get_bids()
    user_name = []
    comment = []
    price = []
    Post_ID = []
    # Creating lists and defining functions as variables
    for x in submission:
        user_name.append(x[1])
        comment.append(x[2])
        price.append(x[4])
        Post_ID.append(x[3])
    # Adding specific details of the submission variable to these variables.
    selected_content = []
    bid_database_len = len(user_name)
    for x in range(0, bid_database_len):
        pre_list = []
        pre_list.extend((user_name[x], comment[x], price[x], Post_ID[x]))
        selected_content.append(pre_list)
        # Adding all columns of the rows that are going to be put on the website to selected_content.
    for x in bid:
        bids.append(x[0])
        # Adding all the ID's of the food_database or the post ID's to bids.
    number_of_occurances = bid_comments(get_bids())[1]
    # Adding all the unique post values to bid.
    final_bid = bids[::-1]
    final_occurance = number_of_occurances[::-1]
    # Reversing all the unique post values and id's of the post to put the most recent posts on the top of the page on the bidding page.
    final_string_bid = []
    for x in final_bid:
        final_string_bid.append(str(x))
    return render_template('bidding.html', name=current_user.name, unique_post_values=final_string_bid, content=selected_content)

@main.route('/post', methods=['POST','GET'])
def post():
    content=get_content()
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
    # Displaying any posts created in the current season.
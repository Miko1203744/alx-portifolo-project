import secrets
import os
from flask import render_template, request,url_for,flash,redirect,Request
from flask_bolg import app,db,bcrypt
from flask_bolg.form import RegistrationForm,LoginForm,update_Form, wish_Form,SearchForm
from flask_bolg.model import User,Video,video_child,Book
from flask_login import login_user,current_user,logout_user
@app.route('/')
def about():
    return render_template("about.html")
@app.route('/home', methods=['GET','POST'])
def home():
    form=wish_Form()
    videos=Video.query.all()
    books=Book.query.all()
    return render_template("home.html",logout='logout', videos=videos,form=form, books=books)
@app.route('/entertainment')
def entertain():
    videos=Video.query.all()
    return render_template("entertainment.html",logout='logout',videos=videos)
@app.route('/audiobook_store')
def bookstore():
    books=Book.query.all()
    return render_template("audiobook.html",logout='logout',books=books)
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(user_name=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.user_password, form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect(url_for('home'))
        else:
            flash('login Unsuccesful. please check email and password')
    return render_template('login.html',form=form,logout='register')        

@app.route('/register',methods=['GET','POST'])
def register():
    '''if current_user.is_authenticated:
        return redirect(url_for('home'))'''
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user=User(user_name=form.username.data,user_fname=form.userfname.data,user_gfname=form.usergfname.data,user_age=form.userage.data, user_gender=form.usergender.data,user_password=hashed_password,user_phone_number=form.userphone_number.data,user_country=form.userCountry.data)
        #new_user=child(user_name=form.username.data,user_fname=form.userfname.data,user_gfname=form.usergfname.data,user_age=form.userage.data, user_gender=form.usergender.data,user_password=form.password.data,user_phone_number=form.userphone_number.data,user_country=form.userCountry.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',logout='login',form=form)

def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(app.root_path, 'static\images',picture_fn)
    form_picture.save(picture_path)
    return picture_fn

def save_picture1(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(app.root_path, 'static\images',picture_fn)
    form_picture.save(picture_path)
    return picture_fn


@app.context_processor
def base():
    form=SearchForm()
    return dict(form=form)
@app.route('/search', methods=["POST"])
def search():
    form=SearchForm()
    videos=Video.query
    book=Book.query
    if form.validate_on_submit():
        post=form.search.data
        videos=videos.filter(Video.video_title.like('%'+ post + '%'))
        videos=videos.order_by(Video.video_title).all()
        #book=book.filter(Book.audio_book_name.like('%'+ post + '%'))
        #book=book.order_by(Book.audio_book_name).all()
    
        return render_template("search.html",form=form,searched=post, videos=videos)

@app.route('/profile_page',methods=['GET','POST'])
def profile():
    form=update_Form()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            current_user.user_profile_pic=picture_file
        if form.cover_picture.data:
            picture_file=save_picture1(form.cover_picture.data)
            current_user.user_background_pic=picture_file
        current_user.user_name=form.username.data
        current_user.user_phone_number=form.userphone_number.data
        db.session.commit()
        flash('your account has been updated!')
        return redirect(url_for('profile'))
    elif request.method=='GET':
        form.username.data=current_user.user_name
        form.userphone_number.data=current_user.user_phone_number
    image_file1=url_for('static', filename='images/' + current_user.user_background_pic)
    image_file=url_for('static', filename='images/' + current_user.user_profile_pic)
    return render_template('profile.html', image_file=image_file,form=form,image_file1=image_file1)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

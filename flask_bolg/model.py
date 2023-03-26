from datetime import datetime

from sqlalchemy import Engine
from flask_bolg import db, login_manager,app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

video_child=db.Table("video_child",db.Column('video_id',db.Integer, db.ForeignKey('video.id')),
                                          db.Column('user_id',db.Integer, db.ForeignKey('user.id'))) 

book_child=db.Table("audiobook_child",db.Column('book_id',db.Integer, db.ForeignKey('book.id')),
                                          db.Column('user_id',db.Integer, db.ForeignKey('user.id')))



class User(db.Model, UserMixin):     
    id=db.Column(db.Integer,primary_key=True) 
    user_name=db.Column(db.String(50),unique=True, nullable=False)
    user_fname=db.Column(db.String(50), nullable=False)
    user_gfname=db.Column(db.String(50), nullable=False)
    user_age=db.Column(db.Integer, nullable=False)
    user_gender=db.Column(db.CHAR, nullable=False)
    user_profile_pic=db.Column(db.String(50), nullable=False, default='profile.jpg')
    user_background_pic=db.Column(db.String(50), nullable=False, default='sky.jpg')
    user_phone_number=db.Column(db.String(30), nullable=False)
    user_password=db.Column(db.String(50), nullable=False)
    user_country=db.Column(db.String(50), nullable=False)

'''with app.app_context():
    User.__table__.create(db.engine)'''

class Video(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    video_title=db.Column(db.String(50),unique=True, nullable=False)
    video_description=db.Column(db.String(200), nullable=False)
    video_size=db.Column(db.String(20), nullable=False)
    video_poster=db.Column(db.String(50), nullable=True)
    video_file_name=db.Column(db.String(50), nullable=False)
    users=db.relationship('User',secondary=video_child, backref='video')
'''with app.app_context():
    Video.__table__.create(db.engine)'''


class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    audio_book_name=db.Column(db.String(50), unique=True, nullable=False)
    audio_book_description=db.Column(db.String(200),nullable=False)
    book_size=db.Column(db.String(20), nullable=False)
    audiobook_poster=db.Column(db.String(50), nullable=True)
    audiobook_file_name=db.Column(db.String(50), nullable=False)
    users=db.relationship('User',secondary=book_child, backref='book')
    '''with app.app_context():
    Book.__table__.create(db.engine)'''
                              
    def __repr__(self):
        return f"User('{self.user_name}', '{self.user_age}','{self.user_country}')"
#with app.app_context():
 #   db.create_all()

'''with app.app_context():
    anthony=Book(audio_book_name='be_kind',audio_book_description='Be_Kind__A_Children_Story_about_things_that_matter',book_size='11mb',audiobook_file_name='123.mp4')
    anthony1=Book(audio_book_name='peter_pan',audio_book_description='Peter_Pan_–_Audiobook_in_English',book_size='220mb',audiobook_file_name='456.mp4')
    anthony2=Book(audio_book_name='the_detective_dog',audio_book_description='The_Detective_Dog_by_Julia_Donaldson._Childrens_audio_book',book_size='11mb',audiobook_file_name='abc.mp4')
    anthony3=Book(audio_book_name='the_lazy_boy',audio_book_description='The_Lazy_Boy_Story__Stories_for_Teenagers__@EnglishFairyTales',book_size='52mb',audiobook_file_name='def.mp4')
    anthony4=Book(audio_book_name='The_Selfish_Crocodile',audio_book_description='The_Selfish_Crocodile_By_Faustin_Charles_Illustrated_By_Michael_Terry(360p)',book_size='17mb',audiobook_file_name='ghi.mp4')
    db.session.add(anthony)
    db.session.add(anthony1)
    db.session.add(anthony2)
    db.session.add(anthony3)
    db.session.add(anthony4)
    db.session.commit()'''
  
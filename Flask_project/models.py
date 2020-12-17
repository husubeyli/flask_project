import datetime
from sqlalchemy import Column, Integer, DateTime, Integer, ForeignKey, String, Numeric, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class Book(db.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    author = Column(String(45), nullable=False)
    price = Column(Numeric(4,2))
    description = Column(Text)
    image_url = Column(String(120))
    stock = Column(Integer)
    genre = Column(String(45))
    language = Column(String(50))
    publisher = Column(String(100))
    comments = relationship('Comment', backref='book', lazy='dynamic')

    def __init__(self, title, author, price, description, image_url, stock, genre, language, publisher):
        self.title = title
        self.author = author
        self.price = price
        self.description = description
        self.image_url = image_url
        self.stock = stock
        self.genre = genre 
        self.language = language
        self.publisher = publisher

    def __repr__(self):
        return '<Book Name: %r>' % self.title

    def save(self):
        db.session.add(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(80), nullable=False)
    comment = Column(Text)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    book_id = Column(Integer, ForeignKey('book.id', ondelete="CASCADE"), nullable=False, index=True)



    def __repr__(self):
        return '<User Name: %r>' % self.user_name

    def __init__(self, user_name, comment, book_id):
        self.user_name = user_name
        self.comment = comment
        self.book_id = book_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(255), nullable=False) 
    is_active = Column(Boolean, nullable=False) 
    is_superuser = Column(Boolean, nullable=False)  

    def __init__(self, first_name, last_name, email, username, password, is_active=True, is_superuser=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.is_active = is_active
        self.is_superuser = is_superuser

    def __repr__(self):
        return '<Istifadəçi adı: %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()


    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    
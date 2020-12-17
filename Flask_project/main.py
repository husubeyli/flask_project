from flask import Flask
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/products'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = os.urandom(16)
from extensions import *
from models import *
from controllers import *


if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    app.run(debug=True, port=5000)


    
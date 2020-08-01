import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY']='secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from project.kitchen.views import kitchen_blueprint
from project.customers.views import customers_blueprint
app.register_blueprint (kitchen_blueprint,url_prefix='/kitchen')
app.register_blueprint (customers_blueprint,url_prefix='/customer')

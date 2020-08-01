# models.py file with both owners and puppies ...
# models is at same level as __init__.py
from project import db
#from project.kitchen.models import Dish
class Customer (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    num = db.Column(db.Integer)
    dish_id = db.relationship('Dish',backref='customer',uselist=True)
    #dish_amount = db.Column(db.Numeric)
    def __init__(self,num,name):
        self.num = num
        self.name = name

# models.py file with both owners and puppies ...
# models is at same level as __init__.py
from project import db
#from project.customers.models import Customer
class Dish (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    type = db.Column(db.String(30))
    description = db.Column(db.String(50))
    image = db.Column(db.String(80))
    price = db.Column(db.Numeric)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    def __init__(self,name,type,description,price,image):
        self.name = name
        self.type=type
        self.description=description
        self.price = price
        self.image = image
    def __repr__(self):
        return f" self.name "

class Dummy (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        print (name)

class Drink (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    type = db.Column(db.String(30))
    description = db.Column(db.String(50))
    image = db.Column(db.String(50))
    price = db.Column(db.Numeric)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    def __init__(self,name,type,description,price,image):
        self.name = name
        self.type=type
        self.description=description
        self.price = price
        self.image = image
    def __repr__(self):
        # if self.customer:
        #     return f"Customer with id {self.customer_id} has purchased item {self.name}"
        # else:
            # return f"No one has ordered the dish"
            return f" self.name "

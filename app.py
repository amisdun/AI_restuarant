from project import app
from flask import render_template
from flask import request, jsonify
import jsonpickle
from project.kitchen.models import Dish,Dummy,Drink

@app.route('/')
def index ():
    return render_template('home.html')

@app.route('/all/foods',methods = ['GET'])
def dishes():
    all_dishes = Dish.query.all()
    print (all_dishes)
    return jsonpickle.encode(all_dishes)

@app.route('/all/drinks',methods = ['GET'])
def drinks():
    all_dishes = Drink.query.all()
    print (all_dishes)
    return jsonpickle.encode(all_dishes)

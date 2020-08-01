from project import app
from flask import render_template
from flask import request, jsonify
import jsonpickle
from project.kitchen.models import Dish,Dummy,Drink
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/')
def index ():
    return render_template('home.html')

@app.route('/all/foods',methods = ['GET'])
def books():
    all_dishes = Dish.query.all()
    print (all_dishes)
    return jsonpickle.encode(all_dishes)


if __name__ == '__main__':
    app.run(debug=True)

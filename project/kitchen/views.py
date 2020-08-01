# project/owners/views.py
from flask import Blueprint, render_template, redirect,url_for,request,session
from project import db
from project.kitchen.models import Dish,Dummy,Drink
from project.kitchen.forms import ModifyIDForm,AddForm,ModifyForm,SubmitForm,ModifyOptionForm
from project.kitchen.forms import AddDrinkForm,ModifyDrinkIDForm,ModifyDrinkForm,SubmitDrinkForm,ModifyDrinkOptionForm

kitchen_blueprint = Blueprint('kitchen',__name__,template_folder='templates/kitchen')
@kitchen_blueprint.route('/add_dish',methods = ['GET','POST'])
def add ():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        dish_type = form.dish_type.data
        dish_description=form.dish_description.data
        price = form.price.data
        dish_image = form.dish_image.data
        db.create_all()
        new_dish = Dish(name,dish_type,dish_description,price,dish_image)
        print(new_dish)
        db.session.add(new_dish)
        db.session.commit()
        return redirect(url_for('kitchen.add'))
    all_dishes = Dish.query.all()
    return render_template('add.html',form=form,all_dishes=all_dishes)

@kitchen_blueprint.route('/add_drinks',methods = ['GET','POST'])
def adddrinks ():
    form = AddDrinkForm()
    all_drinks = Drink.query.all()
    if form.validate_on_submit():
        name = form.name.data
        drink_type = form.drink_type.data
        drink_description=form.drink_description.data
        price = form.price.data
        db.create_all()
        new_drink = Drink(name,drink_type,drink_description,price)
        db.session.add(new_drink)
        db.session.commit()
        return redirect(url_for('kitchen.adddrinks'))
    return render_template('adddrinks.html',form=form,all_drinks=all_drinks)

@kitchen_blueprint.route('/modify_dish',methods = ['GET','POST'])
def modify():
    form = ModifyForm()
    all_dishes = Dish.query.all()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        dish_description = form.dish_description.data
        dish_image = form.dish_image.data
        dish_type = form.dish_type.data
        dish_id=int(session['dish_id'])
        dish = Dish.query.get(dish_id)
        if session['option_to_modify']=='dish':
            dish.name = name
        elif session['option_to_modify']=='dish_description':
            dish.description = dish_description
        elif session['option_to_modify']=='dish_image':
            dish.image = dish_image
        elif session['option_to_modify']=='price':
            dish.price = price
        else:
            dish.type = dish_type
        db.session.add(dish)
        db.session.commit()
        return redirect(url_for('kitchen.add'))
    return render_template('modify.html',all_dishes=all_dishes,form=form)

@kitchen_blueprint.route('/modify_drinks',methods = ['GET','POST'])
def modifydrinks():
    form = ModifyDrinkForm()
    all_drinks = Drink.query.all()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        drink_description = form.drink_description.data
        drink_type = form.drink_type.data
        drink_id=int(session['drink_id'])
        drink = Drink.query.get(drink_id)
        if session['option_to_modify']=='drink':
            drink.name = name
        elif session['option_to_modify']=='drink_description':
            drink.description = drink_description
        elif session['option_to_modify']=='price':
            drink.price = price
        else:
            drink.type = drink_type
        db.session.add(drink)
        db.session.commit()
        return redirect(url_for('kitchen.adddrinks'))
    return render_template('modifydrinks.html',all_drinks=all_drinks,form=form)


@kitchen_blueprint.route('/choice_dish',methods = ['GET','POST'])
def choice():
    form = ModifyOptionForm()
    if form.validate_on_submit():
        session['option_to_modify'] = form.option_to_modify.data
        return redirect(url_for('kitchen.foodchoice'))
    return render_template('choice.html',form=form)

@kitchen_blueprint.route('/choice_drink',methods = ['GET','POST'])
def choicedrink():
    form = ModifyDrinkOptionForm()
    if form.validate_on_submit():
        session['option_to_modify'] = form.option_to_modify.data
        return redirect(url_for('kitchen.drinkchoice'))
    return render_template('choicedrink.html',form=form)

@kitchen_blueprint.route('/foodchoice_dish',methods = ['GET','POST'])
def foodchoice():
    form = ModifyIDForm()
    all_dishes = Dish.query.all()
    if form.validate_on_submit():
        if form.id:
            dish_id = form.id.data
            session['dish_id'] = dish_id
        else:
            dish_id = request.form.get('dish')
            session['dish_id'] = dish_id
        return redirect(url_for('kitchen.modify'))
    return render_template('foodchoice.html',form=form,all_dishes=all_dishes)

@kitchen_blueprint.route('/choice_drinks',methods = ['GET','POST'])
def drinkchoice():
    form = ModifyDrinkIDForm()
    all_drinks = Drink.query.all()
    if form.validate_on_submit():
        drink_id = form.id.data
        session['drink_id'] = drink_id
        return redirect(url_for('kitchen.modifydrinks'))
    return render_template('drinkchoice.html',form=form,all_drinks=all_drinks)

@kitchen_blueprint.route('/deletedish',methods = ['GET','POST'])
def deletedish ():
    form = ModifyIDForm()
    all_dishes = Dish.query.all()
    if form.validate_on_submit():
        if form.id:
            dish_id = form.id.data
            dish = Dish.query.get(dish_id)
            db.session.delete(dish)
            db.session.commit()
        else:
            dish_id = request.form.get('dish')
            dish = Dish.query.get(dish_id)
            db.session.delete(dish)
            db.session.commit()
        return redirect(url_for('kitchen.add'))
    return render_template('deletedish.html',form=form,all_dishes=all_dishes)

@kitchen_blueprint.route('/deletedrink',methods = ['GET','POST'])
def deletedrink ():
    form = ModifyDrinkIDForm()
    all_drinks = Drink.query.all()
    if form.validate_on_submit():
        if form.id:
            drink_id = form.id.data
            drink = Drink.query.get(drink_id)
            db.session.delete(drink)
            db.session.commit()
        else:
            drink_id = request.form.get('drink')
            drink = Drink.query.get(drink_id)
            db.session.delete(drink)
            db.session.commit()
        return redirect(url_for('kitchen.adddrink'))
    return render_template('deletedrink.html',form=form,all_drinks=all_drinks)

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,validators, TextAreaField,DecimalField, SelectField, RadioField
from wtforms.fields.html5 import URLField
from wtforms.validators import url,DataRequired
class AddForm(FlaskForm):
    name = StringField('Enter the dish name: ', validators=[DataRequired(message='You have to enter the dish')])
    price = DecimalField ('Enter the price: ',validators=[DataRequired(message='You have to enter the price')],places = 2)#
    dish_type = StringField('Enter the type of dish : ',validators=[DataRequired(message='You have to enter the dish type')])
    dish_image = URLField('URL of dish image : ', validators=[DataRequired(message='Provide image URL'),url(message='Invalid URL format')])
    dish_description = TextAreaField('Enter dish description: ')
    submit = SubmitField('Submit')
class AddDrinkForm(FlaskForm):
    name = StringField('Enter the drink name: ', [validators.DataRequired(message='You have to enter the drink')])
    price = DecimalField ('Enter the price: ',[validators.DataRequired(message='You have to enter the price')],places = 2)#
    drink_type = StringField('Enter the type of drink : ', [validators.DataRequired(message='You have to enter the drink type')])
    drink_image = URLField('URL of drink image : ', validators=[DataRequired(message='Provide image URL'),url(message='Invalid URL format')])
    drink_description = TextAreaField('Enter drink description: ')
    submit = SubmitField('Submit')

class ModifyOptionForm(FlaskForm):
    option_to_modify = RadioField('Please select which details of the dish you want to modify: ',choices = [('dish','Dish name'),('dish_type','Dish Type'),('dish_description','Dish Description'),('price','Price'),('image','Dish Image')])
    submit=SubmitField('Submit')

class ModifyDrinkOptionForm(FlaskForm):
    option_to_modify = RadioField('Please select which details of the drink you want to modify: ',choices = [('drink','Drink name'),('drink_type','Drink Type'),('drink_description','Drink Description'),('price','Price'),('image','Drink Image')])
    submit=SubmitField('Submit')

class ModifyForm(FlaskForm):
    name = StringField('Enter the new dish name: ')
    price = DecimalField ('Enter the new price: ',places = 2)
    dish_type = StringField('Enter the type of dish : ')
    dish_description = TextAreaField('Enter dish description: ')
    dish_image = StringField('URL of the dish:')
    submit = SubmitField('Enter')
class ModifyDrinkForm(FlaskForm):
    name = StringField('Enter the new dish name: ')
    price = DecimalField ('Enter the new price: ',places = 2)
    drink_type = StringField('Enter the type of drink : ')
    drink_description = TextAreaField('Enter drink description: ')
    drink_image = StringField('URL of the drink')
    submit = SubmitField('Enter')

class SubmitForm(FlaskForm):
    option_to_modify = RadioField('Please select which details of the dish you want to modify: ', choices = [('dish','Dish name'),('dish_type','Dish Type'),('dish_description','Dish Description'),('price','Price'),('image','Dish Image')])
    submit = SubmitField('Submit')
class SubmitDrinkForm(FlaskForm):
    option_to_modify = RadioField('Please select which details of the drink you want to modify: ', choices = [('drink','Drink name'),('drink_type','Drink Type'),('drink_description','Drink Description'),('price','Price'),('image','Drink Image')])
    submit = SubmitField('Submit')

class ModifyIDForm(FlaskForm):
    id = IntegerField('Enter the ID of the dish:')
    submit = SubmitField('Submit')

class ModifyDrinkIDForm(FlaskForm):
    id = IntegerField('Enter the ID of the drink:')
    submit = SubmitField('Submit')

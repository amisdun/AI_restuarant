from flask_wtf import FlaskForm
from wtforms import StringField,RadioField,IntegerField, SubmitField,validators,BooleanField

class BuyForm(FlaskForm):
    name = StringField('Please enter your name: ',[validators.DataRequired(message='You have to enter your name')])
    num = IntegerField ('How many plates do you want? ',[validators.DataRequired(message='You have to enter the number of plates')])
    id = IntegerField ('Enter the ID of the dish you want to order: ',[validators.DataRequired(message='You have to enter the ID of the dish')])
    order_num = IntegerField ('Enter the number of orders you want: ',[validators.DataRequired(message='You have to enter number of orders')])
    submit = SubmitField('Submit')
class DeleteForm(FlaskForm):
    id = IntegerField ('Enter the ID of the product you want to delete from your order: ',[validators.DataRequired(message='You have to enter the number of plates')])
    submit = SubmitField('Submit')
class ChoiceForm(FlaskForm):
    choice = RadioField('Do you want to buy more?',choices=[('y','Yes'),('n','No')])
    submit = SubmitField('Enter')

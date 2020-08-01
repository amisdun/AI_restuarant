 # project/customers/views.py
from flask import Blueprint,render_template,redirect,url_for,session
from project import db
from project.customers.models import Customer
from project.kitchen.models import Dish
from project.customers.forms import BuyForm,ChoiceForm,DeleteForm

customers_blueprint = Blueprint('customers',__name__,template_folder='templates/customers')
@customers_blueprint.route('/select',methods = ['GET','POST'])
def select ():
    return render_template('select.html')

@customers_blueprint.route('/addchoice',methods = ['GET','POST'])
def addchoice ():
    customer_dishes = Dish.query.filter_by(customer_id=session['customer_id']).all()
    form = ChoiceForm()
    if form.validate_on_submit():
        ans = form.choice.data
        if ans == 'n':
            return redirect (url_for('customers.bill'))
        else:
            print ('kofi')
            print (customer_dishes[0].name)
            return redirect (url_for('customers.buyagain'))
    return render_template ('addchoice.html',form=form,customer_dishes=customer_dishes)

@customers_blueprint.route('/purchase',methods = ['GET','POST'])
def purchase ():
    form = DeleteForm()
    a = 3
    if form.validate_on_submit():
        a = 10
    return render_template('purchase.html',form=form,a=a)

@customers_blueprint.route('/buy',methods = ['GET','POST'])
def buy ():
    form = BuyForm()
    a = 3
    customer_dishes=''
    new_dish = Dish.query.get(1)
    new_customer='???'
    all_dishes=Dish.query.all()
    all_customers = Customer.query.all()
    if form.validate_on_submit():
        a = 10
        print('Kofi')
        name = form.name.data
        id = form.id.data
        order_num = form.order_num.data
        num = form.num.data
        new_dish = Dish.query.get(id)
        print (new_dish.name)
        new_customer = Customer(num,name)
        session['customer_id'] = new_customer.id
        new_dish.customer_id = new_customer.id
        db.session.add(new_customer)
        db.session.commit()
        return redirect (url_for('customers.addchoice'))
    return render_template('buy.html',customer_dishes=customer_dishes,all_customers=all_customers,new_dish=new_dish,new_customer=new_customer,form=form,a=a,all_dishes=all_dishes)


@customers_blueprint.route('/buyagain',methods = ['GET','POST'])
def buyagain ():
    form = BuyForm()
    a = 3
    customer_dishes=''
    new_dish = Dish.query.get(1)
    new_customer='???'
    all_dishes=Dish.query.all()
    all_customers = Customer.query.all()
    if form.validate_on_submit():
        a = 10
        print('Kofi')
        id = form.id.data
        num = form.num.data
        new_dish = Dish.query.get(id)
        print (new_dish.name)
        new_customer = Customer.query.get(session['customer_id'])
        new_dish.customer_id = new_customer.id
        db.session.add(new_customer)
        db.session.commit()
        return redirect (url_for('customers.addchoice'))
    return render_template('buyagain.html',customer_dishes=customer_dishes,all_customers=all_customers,new_dish=new_dish,new_customer=new_customer,form=form,a=a,all_dishes=all_dishes)

# delete in progress
@customers_blueprint.route('/delete',methods = ['GET','POST'])
def delete ():
    all_dishes=Dish.query.all()
    all_customers = Customer.query.all()
    if form.validate_on_submit():
        id = form.id.data
        new_dish = Dish.query.get(id)
        new_customer = Customer.query.get(session['customer_id'])
        new_dish.customer_id = new_customer.id
        db.session.add(new_customer)
        db.session.commit()
        return redirect (url_for('customers.buy'))
    return render_template('delete.html',customer_dishes=customer_dishes,all_customers=all_customers,new_dish=new_dish,new_customer=new_customer,form=form,a=a,all_dishes=all_dishes)

# customer's bill in progress 
@customers_blueprint.route('/bill',methods = ['GET','POST'])
def bill ():
    all_dishes=Dish.query.all()
    all_customers = Customer.query.all()
    if form.validate_on_submit():
        id = form.id.data
        new_dish = Dish.query.get(id)
        new_customer = Customer.query.get(session['customer_id'])
        new_dish.customer_id = new_customer.id
        db.session.add(new_customer)
        db.session.commit()
        return redirect (url_for('customers.buy'))
    return render_template('bill.html',customer_dishes=customer_dishes,all_customers=all_customers,new_dish=new_dish,new_customer=new_customer,form=form,a=a,all_dishes=all_dishes)

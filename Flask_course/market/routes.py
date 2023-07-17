from market import app,db
from flask import render_template,redirect,url_for,flash,request
from market.models import Item,User
from market.forms import RegisterForm,LoginForm,PurchaseItemForm,SellItemForm
from flask_login import login_user,logout_user,login_required,current_user
# keeping all routes in this single file

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template("home.html",item_name='market')


@app.route('/homepage')
def homepage():
    return render_template("homepage.html")


@app.route('/about/<user>')
def about_page(user):
    return f'<h1>This is about {user}</h1>'


@app.route('/market')
@login_required   #this will be used whenever we try to access this below page, login has to be mandatory
def market_page():
    items = [
        {"id":1,"name":"phone","barcode":4354,"price":450},
        {"id": 2, "name": "tablet", "barcode": 34214, "price": 750},
        {"id": 3, "name": "laptop", "barcode": 543, "price": 1250}
    ]
    return render_template('market.html',items=items)


@app.route('/dbmarket',methods=['GET','POST'])
@login_required
def db_market_page():
    purchase_form=PurchaseItemForm()
    selling_form = SellItemForm()
    items = Item.query.filter_by(owner=None) #we are collecting the items which is not owned by anyone
    # to display the owned/purchased item by the user
    owned_items = Item.query.filter_by(owner=current_user.id)

    # print(purchase_form) #when we click on purchase button in modal, purchase_form will convert like this
    # print(purchase_form.__dict__)
    # print(purchase_form['submit']) #--> <input id="submit" name="submit" type="submit" value="Purchase">
    #getting data from html page because we have the post operation also,so we can get data from html input tag

    # we can avoid the "confirm from  submission" error by checking the  whether it is post
    if request.method =="POST": #we are checking this condition because we have to display only when we use post action
        print(request.form.get('item_purchased'))
        #after purchase, we need to collect the details of purchased item and we need to update details
        purchased_item = request.form.get('item_purchased')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.check_budget(p_item_object.price):
                #we need to update the budget for the user and ownership of the iem as well
                #by using curren_user function from flask, we can get the details for the loggedin user
                p_item_object.buy_item(current_user)
                flash(f"congrats. you have purchased {p_item_object.name} for the price {p_item_object.price}/-",category='success')
            else:
                flash(f"Sorry. you cannot purchase {p_item_object.name} due to low money",category='danger')
            print(current_user.budget)
        # after selling, we need to collect the details of sold item and we need to update details
        sold_item = request.form.get('item_sold')
        # we are collecting the details when user clicks on sell item
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            # we are checking that current user has the iem in his lis or not
            if current_user.can_sell(s_item_object):
                s_item_object.sell_item(current_user)
                flash(f"congrats. you have sold {s_item_object.name} back to market",category='success')
            else:
                flash(f"Sorry. you cannot sell {s_item_object.name} back to market", category='danger')

        # return render_template('dbmarket.html', items=items, purchase_form=purchase_form)
        return redirect(url_for('db_market_page'))
    elif request.method == "GET":
        '''
        #to reset the market page, we can uncomment this part and refresh
        current_user.budget =1000
        items=Item.query.all()
        for item in items:
            item.owner=None
        db.session.commit()'''

        return render_template('dbmarket.html',items=items,purchase_form=purchase_form,selling_form=selling_form,owned_items=owned_items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit(): #if all conditions are paseed in register form
        #creating the user instance to store details of new user
        create_user=User(username=form.username.data,
                         email=form.email.data,
                         password=form.password.data) #we are using password instead of password_has bcaz of using property decorator
        db.session.add(create_user)
        db.session.commit()
        #whenever user created account,we have to inform to user about registration  success
        flash(f'You have created the account successfully as {create_user.username}',category='success')
        #we have to login and and store the session details
        login_user(create_user)
        return redirect(url_for('db_market_page'))
    if form.errors != {}: #if user not followed the specified condition for email and password submit
        for error_msg in form.errors.values():
            flash(f'{error_msg}',category='danger') #sending error msg and category details as flash to html page

    return render_template('registerform.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        existing_email=User.query.filter_by(email=form.email.data).first() #this wil give the details fo user if email exists other wise return none
        if existing_email and existing_email.check_password_match(given_password=form.password.data):
            flash(f'logged in successfully with {existing_email.email}',category='success') #to provide success message
            login_user(existing_email)
            #login_user function takes care of setting the user as "logged in" in the current session. It assigns the user ID to the session and updates the session cookie accordingly.
            # Additionally, the login_user function updates the user's "remember me" cookie, if enabled, to allow the user to stay logged in across multiple sessions or after the browser is closed.

            return redirect(url_for('db_market_page'))
        else:
            flash(f'Given credentials are wrong please try again.',category='danger')
    return render_template('login.html',form=form)
@app.route("/logout")
def logout_page():
    #this logout_user() will remove all our loggen in data from session and close the session as well.
    logout_user()
    flash(f'You have logged out successfully',category='info')
    return redirect(url_for('homepage'))
from market import db,bcrypt,login_manager
from flask_login import UserMixin
# keeping all models i.e. table related class in this file

# This below callback is used to reload the user object from the user ID stored in the session.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#UserMixin will be used to make session active after login and after refresh also
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    username=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(50),nullable=False,unique=True)
    password_hash=db.Column(db.String(length=50),nullable=False)
    budget=db.Column(db.Integer,nullable=False,default=1000)
    items=db.relationship('Item',backref='owned_user',lazy=True)
    # here lazy=True will help to grab all items from Item table
    #backref will be used to create link between owner user for the  items in table

    #this will be send to display the name in SQLalchemy list after running query
    def __repr__(self):
        return f'item {self.username}'

    #https://www.freecodecamp.org/news/python-property-decorator/#:~:text=The%20%40property%20is%20a%20built,define%20properties%20in%20a%20class.

    @property
    def prettier_budget(self):
        if len(str(self.budget))>=4:
            return f'{self.budget[:-3]},{self.budget[-3:]}'
        else:
            return f'{self.budget}'

    @property
    def password(self):
        return self.password #we will use this as the variable to handle the password

    @password.setter
    def password(self,text_password):
        #the below line will change the text password to crypted password and
        # we can use this attribute by using password variable
        # because we have created the property for this variable
        self.password_hash=bcrypt.generate_password_hash(text_password).decode('UTF-8')

    #the below method will help to check for password match while logging
    def check_password_match(self,given_password):
        return bcrypt.check_password_hash(self.password_hash,given_password) #returns true/false

    #checking the budget to purchase the item
    def check_budget(self,item_price):
        return self.budget >= item_price

    #we have to check that real owner of the item by checking items owned by user
    def can_sell(self,owned_item):
        return owned_item in self.items



class Item(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(50),nullable=False,unique=True)
    price=db.Column(db.Integer,nullable=False)
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(200))
    owner=db.Column(db.Integer,db.ForeignKey('user.id')) #create the link with foreign key

    def __repr__(self):
        return f'item {self.name}'

    #updating the details of item and budget of user after purchasing the item
    def buy_item(self,purchased_user):
        purchased_user.budget -= self.price
        self.owner = purchased_user.id
        db.session.commit()

    #updating the details of item and user after selling back to the market
    def sell_item(self,sold_user):
        self.owner = None #removing the ownership of the item sold
        sold_user.budget+= self.price #adding price of item to user budget after selling to market
        db.session.commit()
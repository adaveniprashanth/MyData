from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# for reference --> https://www.youtube.com/watch?v=Qr4QMBUPxWo&list=PPSV
# keeping all required code for package in this file

app = Flask(__name__)

# adding the values for config
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///market.db"  #dont use any other dialets i.e before  :///
#                              just use sqlite:///
app.config['SECRET_KEY']='2ee408b638d41fa3c4d99fe1'

# the below line create the connection with app
db=SQLAlchemy(app)

# below line helps to support crypting in all over the project
bcrypt=Bcrypt(app)

#below line helps to support login mechanism through the app
login_manager=LoginManager(app)

login_manager.login_view ="login_page" #we have to inform to login_manager where to redirect when login is manadatory
login_manager.login_message_category="info" # we are giving the category for flash to manager
login_manager.login_message ="You need to login before look into this page"

from market import routes  #importing routes here to avoid circular imports error because app is importing in routes

# to avoid with app.app_context() in interpreter
# push a context manually if using a plain python shell.
#
# $ python
# >>> from project import app, db
# >>> app.app_context().push()
# >>> db.create_all()
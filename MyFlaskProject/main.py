
from flask import *
import sqlite3
from config import DevConfig



#from blueprints.sessionscode import sessions_page
app = Flask('FlaskApp')
#app.register_blueprint(sessions_page)
app.config.from_object(DevConfig) #we are using to set the configurations of app i.e constants,secrtes etc.
app.secret_key = 'abc'

# For reference --> https://realpython.com/flask-blueprint/#how-flask-blueprints-work


#app.route(rule, options)
@app.route('/') #home page('/') bound with home function
def home():
    return '<h1>Hello World!</h1>'


def bind():  #binding the method to the route
    return "this is returned from add url rule method"
app.add_url_rule('/abc','bind',bind)
# add_url_rule(<url rule>, <endpoint>, <view function>)
# endpoint – the endpoint for the registered URL rule.
# Flask itself assumes the name of the view function as endpoint.
def userstatus(username):
    return f'Hello {username}!'
app.add_url_rule('/username/<username>', 'userstatus', userstatus)

#adding the variable data to the url
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/hello/<int:age>')
def hello_age(age):
   return 'Age= %d' % age

@app.route('/hello/<float:data>')
def hello_data(data):
   return 'Float value is %f!' % data

@app.route('/hello/<path:path_value>')
def hello_path(path_value):
   return 'given path is %s' % path_value

# Dynamic url building i.e rerouting
@app.route('/sum/<int:a>/<int:b>')
def sum_method(a,b):
    return "sum of {} and {} is {}".format(a,b,a+b)

@app.route('/diff/<int:a>/<int:b>')
def diff_method(a,b):
    return f"difference of {a} and {b} is {a-b}"

@app.route('/mul/<int:a>/<int:b>')
def mul_method(a,b):
    return "multiplication of %d and %d is %d"%(a,b,a*b)

@app.route('/div/<int:a>/<int:b>')
def div_method(a,b):
    return "division of "+str(a)+" and "+str(b)+" is "+str(a/b)


@app.route('/div1')
def div_method1():
    return "division is "+str("called")

def div_method2(a,b):
    return f"division of {a} and {b} is {a/b}"
app.add_url_rule('/div2/<int:a>/<int:b>','div_method2',div_method2)

#redirect(url_for(method name,<params>))
@app.route('/dynamic/<name>/<int:val1>/<int:val2>')
def function(name,val1,val2):
    if name == 'sum':
        return redirect(url_for('sum_method',a=val1,b=val2))
    elif name == 'diff':
        return redirect(url_for('diff_method',a=val1,b=val2))
    elif name == 'mul':
        return redirect(url_for('mul_method',a=val1,b=val2))
    elif name == 'div':
        return redirect(url_for('div_method',a=val1,b=val2))
    elif name == 'div1':
        return redirect(url_for('div_method1'))
    elif name == 'div2':
        return redirect(url_for('div_method2',a=val1,b=val2))

# URL Handling #load the html page from folder
# HTTP Methods
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        uname=request.form['uname']
        passwd = request.form['pwd']
        if uname=='prashanth' and passwd == 'pj':
            return 'welcome prashanth'
        else:
            return 'credentials are wrong'
    elif request.method == 'GET':
        uname = request.args.get('uname')
        passwd = request.args.get('pwd')
        if uname == 'prashanth' and passwd == 'pj':
            return 'welcome prashanth from get method'
        else:
            return 'credentials are wrong from get method'


# Werkzeug’s routing module.
# If we provide route name as /template/ it will support for both /template and /template/
# If we provide route as /template it will support only for /template but not for /template/
# Flask Templates i.e sending the response in html format
@app.route('/template/')
def template():
    return '<html><body><h1>Hi, welcome to the website</h1></body></html>'

@app.route('/templateresponse')
def templateresponse():
    return render_template('response.html')

# response with delimiters
@app.route('/responsewithdelimiter/<username>')
def response_with_delimiter(username):
    return render_template('response_with_delimiter.html',name=username)

@app.route('/table/<int:num>')
def table(num):
    return render_template('tables_page.html',n=num)

# Flask request object
# In the client-server architecture,
# the request object contains all the data that is sent from the client to the server

'''
Form	It is the dictionary object which contains key-value pair of form parameters and their values.
args	It is parsed from the URL. 
        It is the part of the URL which is specified in the URL after question mark (?).

Cookies	It is the dictionary object containing cookie names and the values. 
        It is saved at the client-side to track the user session.

files	It contains the data related to the uploaded file.
method	It is the current request method (get or post).
'''

@app.route('/customer')
def customer_details():
    return render_template('customer_details.html')

@app.route('/success',methods=['POST','GET'])
def stored_data():
    print(request.form)
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template('success_report.html',result=result)

# app.add_url_rule('/success','stored_data',stored_data,methods=['POST','GET'])

# Flask Cookies
def cookie():
    response = make_response('<h1>Cookie is set</h1>')
    response.set_cookie('foo','bar')
    return response
app.add_url_rule('/setcookie','cookie',cookie)

# Flask cookie example with login

@app.route('/cookielogin')
def cookie_login():
    return render_template('cookie_login.html')

@app.route('/cookiesuccess',methods=['POST','GET'])
def cookie_success():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        if password == 'abcd':
            res = make_response(render_template('cookie_success.html',name=email))
            res.set_cookie("email",email)
            res.set_cookie("name",name)
            return res
        else:
            return redirect(url_for('cookie_error',name=name))

@app.route('/cookieviewprofile')
def cookie_viewprofile():
    name = request.cookies.get("name")
    email = request.cookies.get("email")
    return render_template('cookie_viewprofile.html',name=name,email=email)

@app.route('/cookieerror/<name>')
def cookie_error(name):
    return render_template('cookie_error.html',name=name)


# Flask session
'''
The session can be defined as the duration for which a user logs into the server and logs out. 
The data which is used to track this session is stored into the temporary directory on the server.
The session data is stored on the top of cookies and signed by the server cryptographically.
'''


def start_session():
    session['response']='session#1'
    return render_template('/start_session.html')
app.add_url_rule('/startsession','start_session',start_session)

@app.route('/getsession')
def get_session():
    if 'response' in session:
        value = session['response']
        return render_template('session_details.html',name=value)


# Login application with session
@app.route('/sessionhome')
def session_home():
    return render_template('session_home.html')

@app.route('/sessionlogin')
def session_login():
    return render_template('session_login.html')

@app.route('/sessionloginsuccess',methods=['POST'])
def session_login_success():
    if request.method == 'POST':
        email = request.form['email']
        session['email']=request.form['email']
        return render_template('session_login_success.html',name=email)

def session_logout():
    if 'email' in session:
        email = session['email']
        session.pop('email',None)
        print("email ",session)
        return render_template('session_logout.html',email=email)
    else:
        return render_template('session_logout_error.html')
app.add_url_rule('/sessionlogout','session_logout',session_logout)

def session_profile_view():
    if 'email' in session:
        email = session['email']
        return render_template('session_profile_view.html',name=email)
    else:
        return render_template('session_error.html')
app.add_url_rule('/sessionprofileview','session_profile_view',session_profile_view)

# File upload
@app.route('/fileupload')
def file_upload():
    return render_template('file_upload_form.html')

@app.route('/fileuploadsuccess',methods=['POST'])
def file_upload_success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('/file_upload_success.html',name=f.filename)

# Flask redirect logic
@app.route('/redirecthome')
def redirect_home():
    return render_template('redirect_home.html')

@app.route('/redirectlogin')
def redirect_login():
    return render_template('redirect_login.html')

@app.route('/redirectvalidate',methods=['POST'])
def redirect_validate():
    print(request.form['password'])
    if request.method == 'POST' and request.form['password'] == 'abcd':
        return redirect(url_for("redirect_success"))
    else:
        abort(401)
@app.route('/redirectsuccess')
def redirect_success():
    return render_template('redirect_success.html')


@app.route('/flashlogin')
def flash_login():
    return render_template('flash_login.html')

@app.route('/flashsuccess',methods=['POST','GET'])
def flash_success():
    error = None
    if request.method=='POST':
        if request.form['password'] != 'abc':
            error = 'Wrong password'
        else:
            flash("successfully logged in")
            return redirect(url_for('flash_login'))
    return render_template('flash_success.html',error=error)

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS Employees;')
cursor.execute('''CREATE TABLE Employees(id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,email TEXT NOT NULL UNIQUE);''')
cursor.close()
db.close()

@app.route('/sqlitehome')
def sqlit_home():
    return render_template('sqlite_home.html')

def sqlite_add():
    return render_template('sqlite_add.html')
app.add_url_rule('/sqliteadd','sqlite_add',sqlite_add)


def sqlite_save():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        try:
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute('INSERT INTO Employees(name,email) VALUES (?,?);',(name,email))
            db.commit()
            msg='Data saved successfully.'
        except:
            db.rollback()
            msg='We cannot add the data to database.'
        finally:
            return render_template('sqlite_success.html',msg=msg)
            db.close()
app.add_url_rule('/sqlitesave','sqlite_save',sqlite_save,methods=['POST','GET'])

@app.route('/sqliteview')
def sqlite_view():
    db=sqlite3.connect('database.db')
    db.row_factory=sqlite3.Row
    cursor= db.cursor()
    cursor.execute('SELECT * FROM Employees;')
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return render_template('sqlite_view.html',rows=rows)

@app.route('/sqlitedelete')
def sqlite_delete():
    return render_template('sqlite_delete.html')

@app.route('/sqlitedeletedata',methods=['POST'])
def sqlite_delete_data():
    if request.method == 'POST':
        id = request.form['id']

        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM Employees where id=?;",id)
            msg='Data deleted successfully.'
        except:
            msg='Data cannot be deleted'
        finally:
            db.commit()
            db.close()

        return render_template('sqlite_delete_status.html',msg=msg)

'''****** NOT WORKING *******
from flask_mail import *  
#instantiate the Mail class
mail = Mail(app)
#configure the Message class object and send the mail from a URL
@app.route('/sendemail')
def index():
    msg = Message('subject', sender = 'mydata232@gmail.com', recipients=['adaveniprashanth@gmail.com'])
    msg.body = 'hi, this is the mail sent by using the flask web application'
    return "Mail Sent, Please check the mail id"
'''

#Flask WTF
from forms import ContactForm

@app.route('/wtfcontact', methods=['GET','POST'])
def contact():
   form = ContactForm()
   if form.validate() == False:
      flash('All fields are required.')
   return render_template('wtf_contact.html', form=form)

@app.route('/wtfsuccess',methods = ['GET','POST'])
def success():
   return render_template("wtf_success.html")
'''****** NOT WORKING *******
#flask sqlalchemy

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY'] = "secret key"
db = SQLAlchemy(app)

class Employees(db.Model):
    def __init__(self,name,salary,age,pin):
        self.name = name
        self.salary = salary
        self.age=age
        self.pin = pin

    id = db.Column('employee_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    salary = db.Column(db.String(50))
    age = db.Column(db.String(10))
    pin = db.Column(db.String(10))

@app.route('/alchemylist')
def alchemy_list():
    return render_template('alchemy_list.html',Employees= Employees.query.all())

@app.route('/alchemyadd',methods=['GET','POST'])
def alchemy_add():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['salary'] or not request.form['age'] or not request.form['pin']:
            flash('Please enter all the fields','error')
        else:
            employee = Employees(request.form['name'],request.form['salary'],request.form['age'],request.form['pin'])
            db.session.add(employee)
            db.session.commit()
            flash('Record added successfully')
        return redirect(url_for('alchemy_list'))
    return render_template('alchemy_add.html')
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.create_all()
    app.run()
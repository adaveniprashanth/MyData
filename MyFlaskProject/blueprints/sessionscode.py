'''
from flask import *
#from flask import Blueprint, render_template

sessions_page = Blueprint('sessions_page', __name__,
                        template_folder='templates')

def start_session():
    session['response']='session#1'
    return render_template('/start_session.html')
sessions_page.add_url_rule('/startsession','start_session',start_session)

@sessions_page.route('/getsession')
def get_session():
    if 'response' in session:
        value = session['response']
        return render_template('session_details.html',name=value)

'''
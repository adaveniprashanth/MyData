from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig) #we are using to set the configurations of app i.e constants,secrtes etc.

@app.route('/') #home page
def home():
    return '<h1>Hello World!</h1>'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

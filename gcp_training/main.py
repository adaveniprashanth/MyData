import os
from utils.run import run
from flask import Flask,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def main():
    print('flow is started')
    envelope={'project':'develop-488306',
              'test-bucket':'us-test-bucket1',
              'stage-bucket':'us-stage-bucket1',
              'file_name': 'sample_data.xlsx',
              'secret-name':'secret_manager_value'}
    run(envelope)

@app.route('/home')
def home():
    return {'message':'this is the home function'},200

if __name__ == '__main__':
    server_port=os.environ.get('PORT','8080')
    # PROJECT_SETTINGS= {
    #     'test-bucktet': 'us-test-bucket1'
    # }
    app.run(debug=False,port=server_port,host='0.0.0.0')
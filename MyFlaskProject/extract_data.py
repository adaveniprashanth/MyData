

from PIL import Image
import pytesseract
from flask import *
import json
app = Flask('FlaskApp')
app.debug=False
app.secret_key = 'abc'

def extract_text(filename):
    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe path'

    a = pytesseract.image_to_string(Image.open(filename))

    f = open(filename.split(".")[0]+".json",'w')
    a = a.split("\n")
    a = [x for x in a if ":" in x]
    d = {}
    for i in a:
        l = i.split(":")
        d[l[0].strip()] = l[1].strip()
    json.dump(d,f)
    f.close()


# File upload
@app.route('/fileupload')
def file_upload():
    return render_template('file_upload_form.html')


@app.route('/fileuploadsuccess',methods=['POST'])
def file_upload_success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        extract_text(f.filename)
        return render_template('/file_upload_success.html',name=f.filename)

if __name__ == '__main__':
    app.run()
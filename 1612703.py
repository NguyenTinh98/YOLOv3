from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os
from darknet import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file_1():
   return render_template('index.html')


def main():
    return render_template('index.html')




@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        filename = str(f.filename)
        os.system('./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights '+filename)
        os.system('mv predictions.jpg pred'+filename)
        os.system('cp pred'+filename+' static/')
        os.system('cp '+filename+ ' static/')
        filename1 = '/static/' +filename
        filename2 = '/static/pred'+filename
        listfile = []
        listfile.append(filename1)
        listfile.append(filename2)
	#net = load_net("cfg/yolov3.cfg", "yolov3.weights", 0)
    	#meta = load_meta("cfg/coco.data")
    	#r = detect(net, meta, filename)
        return render_template('result.html', variable = listfile)


@app.route('/more', methods=['GET', 'POST'])
def upload_file_2():
   return render_template('more.html')


def main():
    return render_template('more.html')


@app.route('/uploadermore', methods=['GET', 'POST'])
def upload_file_3():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        filename = str(f.filename)
        os.system('./darknet detector test succulent_obj.data succulent-yolov3.cfg succulent-yolov3.backup '+filename)
        os.system('mv predictions.jpg pre'+filename)
        os.system('cp pre'+filename +' static/')
        os.system('cp '+filename+ ' static/')
        filename1 = '/static/' +filename
        filename2 = '/static/pre'+filename
        listfile = []
        listfile.append(filename1)
        listfile.append(filename2)
        return render_template('result.html', variable = listfile)


if __name__ == '__main__':
    app.run(debug = True)

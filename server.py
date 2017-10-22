import os
from flask import Flask, request, redirect, url_for, render_template
#from werkzeug.utils import secure_filename
from test import getVideo, modifyVideo
UPLOAD_FOLDER = '/Users/neovlad/PycharmProjects/flaskserver/static/videos/'
ALLOWED_EXTENSIONS = {'.mp4'}

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#   return '.' in filename
#          filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    #if request.args.get()

    # check if the post request has the file part

    if len(request.args) > 0:
        outfile = "./static/video/test.mp4"
        poc = "./static/processed/test.mp4"
        if os.path.isfile(outfile):
            os.remove(outfile)
        if os.path.isfile(outfile):
            os.remove(outfile)

        getVideo(request.args['input'], outfile)
        modifyVideo(outfile, poc)
        return render_template('res.html', vidpath="/static/processed/test.mp4")
    # if user does not select file, browser also
    # submit a empty part without filename
    # if len(os.listdir(UPLOAD_FOLDER)) > 10:
    #   for fil in os.listdir(UPLOAD_FOLDER):
    #     os.remove(UPLOAD_FOLDER + fil)
    #
    #     if file.filename == '':
    #         return redirect(request.url)
    #     elif len(file.filename) > 10:
    #         outfile = "./static/video/test.mp4"
    #         poc = "./static/processed/test.mp4"
    #         getVideo(file, outfile)
    #         modifyVideo(outfile, poc)
    #         return render_template('res.html', vidpath="poc")

    # request.args
    return render_template('index.html')




app.run(host='127.0.0.1', port=10080, threaded= True)


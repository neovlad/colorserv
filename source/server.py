import os
from flask import Flask, request, render_template
from proc import getVideo, modifyVideo


app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload_file():
    #if request.args.get()

    # check if the post request has the file part

    if len(request.args) > 0:
        outfile = "./static/video/temp.mp4"
        poc = "./static/processed/processed.mp4"

        if os.path.isfile(outfile):
            os.remove(outfile)
        if os.path.isfile(outfile):
            os.remove(outfile)

        getVideo(request.args['input'], outfile)
        modifyVideo(outfile, poc)
        return render_template('res.html', vidpath="/static/processed/test7.mp4")

    return render_template('index.html')




app.run(threaded= True)


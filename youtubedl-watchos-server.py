import youtube_dl
from flask import Flask
from flask import jsonify, make_response
from flask import send_file

app = Flask(__name__)
downloads = dict()

@app.route("/<string:vidid>/")
def hello(vidid):
    options = {
        'format': 'worst'
    }
    ydl = youtube_dl.YoutubeDL(options)
    out = ydl.extract_info(vidid)
    filename = ydl.prepare_filename(out)
    downloads[vidid] = '/tmp/' + filename
    response_body = {
        'path': filename 
    }
    res = make_response(jsonify(response_body), 200)
    return res

@app.route("/dl/<string:vidid>/")
def dl(vidid):
    return send_file(downloads[vidid], as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

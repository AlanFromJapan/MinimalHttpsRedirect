from flask import Flask, redirect
from config import conf

app = Flask(__name__, static_url_path='')

#Default URL without pages
@app.route('/')
def homepage():
    return redirect(conf["target"], code=302)

#in case a page asked (double the slash should work...)
@app.route('/<path>')
def otherpage(path):
    return redirect(conf["target"] + "/" + path, code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=conf.get("debug", False), port=int(conf["app_port"]))
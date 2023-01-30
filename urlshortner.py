from flask import Flask
from flask import request
from hashids import Hashids
from random import randint

app = Flask(__name__)

@app.route('/')
def urlshortener():
    urlid=request.base_url()
    return f'<h1>here: {urlid}</h1>'

if __name__=='__main__':
    app.run(debug=True)
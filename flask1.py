from flask import Flask
from flask import request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hi There! This is Abbas Mirza</h1>'

@app.route('/useragent')
def user_agent():
    browser_info=request.headers.get('User-Agent')
    return f"<h2>browser info: </h2> <p>{browser_info}</p>"

@app.route('/user/<name>')
def user(name):
    return f'<h2>hi this page belongs to: {name}</h2>'

@app.route('/user_latin/<name>')
def user_latin(name):
    if name[-1]=='y':
        username=name[:-1]+'iful'
    else:
        username=name+'y'
    return f'<h1>Hi {name}! Your latin name is {username}</h1>'

@app.route('/redirectme')
def redirect_me():
    return redirect(url_for('/useragent'))

if __name__=='__main__':
    app.run()
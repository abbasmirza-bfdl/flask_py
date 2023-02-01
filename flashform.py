from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?')
    submit=SubmitField('Send')

@app.route('/',methods=['GET','POST'])
def index():
    form=InfoForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash(f"You are a {session['breed']}")
        return redirect(url_for('index'))
    return render_template('catform.html',form=form)


if __name__=='__main__':
    app.run()
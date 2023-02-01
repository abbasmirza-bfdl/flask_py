from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

# class TestForm(FlaskForm):
#     cat_breed=StringField('What is your cat\'s breed?')
#     submit=SubmitField('Submit')

# @app.route('/',methods=['GET','POST'])
# def index():
#     cat_breed=''
#     form = TestForm()
#     if form.validate_on_submit():
#         cat_breed=form.cat_breed.data
#         form.cat_breed.data=''
#     return render_template('catform.html',cat_breed=cat_breed,form=form)

# if __name__=='__main__':
#     app.run()

# class InfoForm(FlaskForm):
#     breed= StringField('whta breed are you?',validators=[DataRequired()])
#     mood=BooleanField('Please choose your mood:',choices=[('mood_one','Hungry'),('mood_two','grumpy')])
#     food_choice=SelectField('Pick your fav food:',choices=[('chi','chicken'),('bef','beef'),('fi','fish')])
#     feedback=TextAreaField()
#     when_is_this=DateTimeField()
#     submit=SubmitField('Send')

# @app.route('/',methods=['GET','POST'])
# def index():
#     form = InfoForm()
#     if form.validate_on_submit():
#         session['breed']=form.breed.data
#         session['mood']=form.mood.data
#         session['food_choice']=form.food_choice.data
#         session['feedback']=form.feedback.data
#         session['when_is_this']=form.when_is_this.data
#         return redirect(url_for('thankyou'))
#     return render_template('catform.html',form=form)

# @app.route('/thankyou')
# def thankyou():
#     return render_template('thankyou.html')

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

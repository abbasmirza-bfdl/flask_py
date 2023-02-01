from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField, IntegerField
from wtforms.validators import DataRequired
import templates.petshop.petregdb as dbc

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class PetForm(FlaskForm):
    own_name=StringField('Enter your name:')
    pet_type=SelectField('Choose Cat or Dog:',choices=[('cat','Cat'),('dog','Dog')])
    pet_breed=StringField(f'Enter the pet breed:')
    pet_name=StringField(f'Enter the pet name:')
    pet_age=StringField(f'Enter the pet age:')
    pet_update=IntegerField('Enter pet ID:')
    submit=SubmitField('Submit')

class DelPet(FlaskForm):
    del_pet_name=StringField('Enter pet name to be deleted:')
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=PetForm()
    if form.validate_on_submit():
        pet=dbc.Pet(form.pet_type.data,form.pet_breed.data,form.pet_name.data,form.pet_age.data,form.own_name.data)
        pets_db=dbc.DBConnection()
        pets_db.connect_db()
        pets_db.create_pets()
        pets_db.insert_pets(pet)
        return redirect(url_for('pet_details'))
    return render_template('index.html',form=form)

@app.route('/pet_details',methods=['GET','POST'])
def pet_details():
    pets_db=dbc.DBConnection()
    petdetails=pets_db.read_pets()
    return render_template('pet_details.html',petdetails=petdetails)
    
@app.route('/pet_deleted',methods=['GET','POST'])
def pet_delete():
    form=DelPet()
    if form.validate_on_submit():
        delid=form.del_pet_name.data
        pets_db=dbc.DBConnection()
        pets_db.connect_db()
        pets_db.delete_pets(delid)
        return redirect(url_for('pet_details'))
    return render_template('del_pet.html',form=form)

@app.route('/pet_update',methods=['GET','POST'])
def pet_update():
    form=PetForm()
    if form.validate_on_submit():
        pets_db=dbc.DBConnection()
        pets_db.connect_db()
        pet=dbc.Pet(form.pet_type.data,form.pet_breed.data,form.pet_name.data,form.pet_age.data,form.own_name.data)
        pets_db.update_pets(pet)
        return redirect(url_for('pet_details'))
    return render_template('index.html',form=form)



if __name__=='__main__':
    app.run()
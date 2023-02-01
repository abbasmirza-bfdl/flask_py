from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField, IntegerField
from wtforms.validators import DataRequired
import petshop.petregdb as dbc

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class PetForm(FlaskForm):
    own_name=StringField('Enter your name:')
    # own_mob=StringField('Enter you 10 digit mobile number:')
    # own_add=StringField('Enter your city:')
    pet_type=SelectField('Choose Cat or Dog:',choices=[('cat','Cat'),('dog','Dog')])
    pet_breed=StringField(f'Enter the pet breed:')
    pet_name=StringField(f'Enter the pet name:')
    pet_age=StringField(f'Enter the pet age:')
    pet_update=IntegerField('Enter pet ID:')
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=PetForm()
    if form.validate_on_submit():
        # dbc.cur.execute(f"insert into pets(ptype,pbreed,pname,page,pown) values('{form.pet_type.data}','{form.pet_breed.data}','{form.pet_name.data}',{form.pet_age.data},'{form.own_name.data}');")
        # dbc.con.commit()

        pet=dbc.Pet(form.pet_type.data,form.pet_breed.data,form.pet_name.data,form.pet_age.data,form.own_name.data)
        pets_db=dbc.DBConnection()
        pets_db.connect_db()
        pets_db.create_pets()
        pets_db.insert_pets(pet)

        return redirect(url_for('pet_details'))
    return render_template('index.html',form=form)

@app.route('/pet_details',methods=['GET','POST'])
def pet_details():
    # dbc.cur.execute('select * from pets;')
    # dbc.con.commit()
    # petdetails=dbc.cur.fetchall()
    # return render_template('pet_details.html',petdetails=petdetails)

    pets_db=dbc.DBConnection()
    petdetails=pets_db.read_pets()


    return render_template('pet_details.html',petdetails=petdetails)
    
@app.route('/pet_deleted',methods=['GET','POST'])
def pet_delete():
    pets_db=dbc.DBConnection()
    pets_db.connect_db()
    petdetails=pets_db.read_pets()
    session['petid']=petdetails[-1][0]
    delid=session['petid']
    pets_db.delete_pets(delid)
    del session
    return '<p>your data has been deleted<p>'

@app.route('/pet_update',methods=['GET','POST'])
def pet_update():
    form=PetForm()
    if form.validate_on_submit():
        pets_db=dbc.DBConnection()
        pets_db.connect_db()
        pet=dbc.Pet(form.pet_type.data,form.pet_breed.data,form.pet_name.data,form.pet_age.data,form.own_name.data)
        pets_db.update_pets(pet)
        return redirect(url_for('pet_details'))



if __name__=='__main__':
    app.run()
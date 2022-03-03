from application import app,db
from application.models import Subjects,Staff
from flask import render_template, redirect, url_for, request
from application.forms import StaffForm

@app.route('/', methods = ['GET'])
def read():
    form = StaffForm()
    subjs = db.session.query(Subjects).all()
    for i in subjs:
        form.subjectID.choices.append((i.id,i.subject_name))
    return render_template('index.html', form=form)



    return 
@app.route('/square/<int:number>')
def square(number):
    return str(number**2)


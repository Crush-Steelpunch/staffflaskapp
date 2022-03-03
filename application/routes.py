from application import app,db
from application.models import Subjects,Staff
from flask import render_template, redirect, url_for, request
from application.forms import StaffForm
import pdb

@app.route('/', methods = ['GET', 'POST'])
def read():
    form = StaffForm()
    staff = Staff.query.join(Subjects).all()
    subjs = db.session.query(Subjects).all()
    for i in subjs:
        form.subjectID.choices.append((i.id,i.subject_name))

    if request.method == 'POST':
        staffin = Staff(staff_name=form.name.data,subject_id=form.subjectID.data)
        db.session.add(staffin)
        db.session.commit()
        return redirect(url_for('read'))


    return render_template('index.html', form=form, staffs=staff)



    return 
@app.route('/square/<int:number>')
def square(number):
    return str(number**2)


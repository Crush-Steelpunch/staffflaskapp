from application import db
from application.models import Subjects,Staff
import pdb

db.drop_all()
db.create_all()

for subj in ['Jenkins','Python','Flask']:
    subjects = Subjects(subject_name=subj)
    db.session.add(subjects)
db.session.commit()
for i in db.session.query(Subjects):
    print(i.id, i.subject_name)
data1 = {'Leon':2,'Earl':1,'Adam':2,'Harry':3}
for nme in data1:
    staff = Staff(staff_name=nme,subject_id=data1[nme])
    db.session.add(staff)
db.session.commit()
#pdb.set_trace()
for row in db.session.query(Staff).join(Subjects).all():
    print(row.staff_name,row.subject_idbr.subject_name)

pdb.set_trace()

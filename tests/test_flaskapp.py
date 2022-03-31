from flask_testing import TestCase
from flask import url_for
from application import app, db 
from application.models import Subjects

class TestBase(TestCase):

    def create_app(self):
       # set up some app config specific for our tests
       app.config.update(
           SQLALCHEMY_DATABASE_URI='sqlite:///',
           DEBUG=True,
           WTF_CSRF_ENABLED=False
       )
       return app

    def setUp(self):
        # create needed resources before each test
        db.create_all()
        for subj in ['Jenkins','Python','Flask']:
            subjects = Subjects(subject_name=subj)
            db.session.add(subjects)
        db.session.commit()

    def tearDown(self):
        # tear down resources after each test
        db.session.remove()
        db.drop_all()


class TestRead(TestBase):
    def test_conflaskapp(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask",response.data)
        self.assertIn(b"Jenkins",response.data)
        self.assertIn(b"Python",response.data)

    def test_readSubj(self):
        response = self.client.get(url_for('addsubjects'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add",response.data)


class TestAdd(TestBase):
    def test_addSubject(self):
        response = self.client.post(url_for('addsubjects'), data=dict(name="TestSubj"),follow_redirects=True )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestSubj",response.data)

    def test_addStaff(self):
        response = self.client.post(url_for('read'), data=dict(name="TestStaff",subjectID=1),follow_redirects=True )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestStaff",response.data)

class TestSquare(TestBase):

    def test_sqar(self):
        response = self.client.get(url_for('square',number=5))
        self.assertIn(b"25",response.data)
        self.assertEqual(response.status_code, 200)
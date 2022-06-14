import pdb
from selenium import webdriver
from flask_testing import LiveServerTestCase
from application import app, db
from application.models import Subjects, Staff

class TestBase(LiveServerTestCase):

    def create_app(self):
#        app.config.update(
#                   SQLALCHEMY_DATABASE_URI='sqlite:///selendb',
#                   DEBUG=True,
#                   WTF_CSRF_ENABLED=False
#         )
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///selendb" # change to a test sqlite database
        app.config['LIVESERVER_PORT'] = 5050
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless') # must be headless

        self.driver = webdriver.Chrome(options=chrome_options) 

        db.create_all() # create schema before we try to get the page
        for subj in ['Jenkins','Python','Flask']:
            subjects = Subjects(subject_name=subj)
            db.session.add(subjects)
        db.session.commit()
        self.driver.get(f'http://localhost:5050/')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()


class AddWibbleUser(TestBase):
    def test_something(self):
        element = self.driver.find_element_by_xpath('//*[@id="name"]') # Set up an object for the text input box
        # element.click()
        element.send_keys('whibble')  # put some text in the text box
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()  # Click Submit button

        assert self.driver.current_url == 'http://localhost:5050/'
        users = Staff.query.first()  # check user is in db
        help(self.driver)
        print(users.staff_name)
        self.assertIn("whibble", users.staff_name)
        self.assertIn("whibble", self.driver.page_source)
        #self.assertIn("whibble",self.driver)

#//*[@id="submit"]

#  /html/body/div[1]/form/span/a

class AddASubject(TestBase):
    def test_Add_Subject(self):
        element = self.driver.find_element_by_xpath('/html/body/div[1]/form/span/a')  # set up an object for the add subject link
        element.click()  # follow the link!

        assert self.driver.current_url == 'http://localhost:5050/addsubjects'

        element1 = self.driver.find_element_by_xpath('//*[@id="name"]') # find the text box
        element1.send_keys('seleniumisasubject')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click() # click the submit subject button

        
        assert self.driver.current_url == 'http://localhost:5050/'

        element2 = self.driver.find_element_by_xpath('//*[@id="subjectID"]') # find the drop down
        
#        pdb.set_trace()
    
        self.assertIn("seleniumisasubject",element2.text)  # check the new item is in the drop down box



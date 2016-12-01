from django.test import TestCase
from django.test import Client
import json

# Create your tests here.

class ExampleMethodTests(TestCase):

    def test_basic_example_addition(self):
        self.assertIs(1+1, 2)
    
    def test_basic_example_strings(self):
        self.assertIs("this is a test", "this is a test")

class DepartmentTests(TestCase):
    
    def setUP(self):
        self.client = Client()
        
    def test_good_post(self):
        department0 = self.client.post('/department/',
        {
            "name": "Trash Department",
            "college": "College of Garbology"
        })
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        
        # status code 201 created
        self.assertEqual(department0.status_code, 201)
        self.assertEqual(d0_json_string['name'], "Trash Department")
        self.assertEqual(d0_json_string['college'], "College of Garbology")
        
    def test_bad_post_no_name(self):
        department0 = self.client.post('/department/',
        {
            "college": "College of Art"
        })
        self.assertEqual(department0.status_code, 400)
        
    def test_bad_post_null_name(self):
        department0 = self.client.post('/department/',
        {
            "name": None,
            "college": "College of the Void"
        })
        self.assertEqual(department0.status_code, 400)
        
    def test_bad_post_noStr_name(self):
        department0 = self.client.post('/department/',
        {
            "name": 42,
            "college": "College of Everything"
        })
        self.assertEqual(department0.status_code, 400)
        
    
    def test_bad_post_no_college(self):
        department0 = self.client.post('/department/',
        {
            "Name": "Department of Nothingness"
        })
        self.assertEqual(department0.status_code, 400)
        
    def test_bad_post_null_college(self):
        department0 = self.client.post('/department/',
        {
            "name": "The Department",
            "college": None
        })
        self.assertEqual(department0.status_code, 400)
        
    def test_bad_post_noStr_college(self):
        department0 = self.client.post('/department/',
        {
            "name": "Department of One",
            "college": 1234
        })
        self.assertEqual(department0.status_code, 400)

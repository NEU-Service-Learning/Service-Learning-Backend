from django.test import TestCase
from django.test import Client
from base.models import *
import json

class DepartmentTests(TestCase):
    
    def setUP(self):
        self.client = Client()
        
    def test_good_post(self):
        college = College(name='College of Garbology')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": "Trash Department",
            "college": college.name
        })
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 201)
        self.assertEqual(d0_json_string['name'], "Trash Department")
        self.assertEqual(d0_json_string['college'], "College of Garbology")
        
    def test_bad_post_no_name(self):
        college = College(name='College of Art')
        college.save()
        department0 = self.client.post('/department/',
        {
            "college": college.name
        })
        self.assertEqual(department0.status_code, 400)
        
    def test_bad_post_null_name(self):
        college = College(name='College of the Void')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": None,
            "college": college.name
        })
        self.assertEqual(department0.status_code, 400)
        
    def test_bad_post_noStr_name(self):
        college = College(name='College of Everything')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": 42,
            "college": college.name
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
        
    def test_get_good(self):
        college = College(name='College of the Cabinet')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": "Department of Defence",
            "college": college.name
        })
        self.assertEqual(department0.status_code, 201)
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        department1 = self.client.get('/department/' + str(d0_json_string['id']) + '/')
        d1_json_string = json.loads(department1.content.decode('utf-8'))
        self.assertEqual(d1_json_string['id'], d0_json_string['id'])
        self.assertEqual(d1_json_string['name'], d0_json_string['name'])
        self.assertEqual(d1_json_string['college'], d0_json_string['college'])

    def test_bad_get(self):
        college = College(name='School of Glitches')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": "MissingNo  Department",
            "college": college.name
        })
        self.assertEqual(department0.status_code, 201)
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        department1 = self.client.get('/department/' + str(d0_json_string['id'] + 1) + '/')

    def test_good_put(self):
        college = College(name='College of Enterprise')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": "Department of Red Shirts",
            "college": college.name
        })
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 201)
        
        college1 = College(name='College of Australia')
        college1.save()
        department1 = self.client.put('/department/' + str(d0_json_string['id']) + '/',
        {
            "name": "Department of Yellow Shirts",
            "college": college1.name
        })
        d1_json_string = json.loads(department1.content.decode('utf-8'))
        self.assertEqual(d1_json_string['id'], d0_json_string['id'])
        self.assertEqual(d1_json_string['name'], "Department of Yellow Shirts")
        self.assertEqual(d1_json_string['college'], "College of Australia")
        
    def test_bad_put(self):
        college = College(name='College of Oceanography')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": "Deep Department",
            "college": college.name
        })
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 201)
        
        department1 = self.client.put('/department/' + str(d0_json_string['id']) + '/', {})
        d1_json_string = json.loads(department1.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 400)
        

    def test_good_delete(self):
        college = College(name='College of Ephemerality')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": "Expendible Department",
            "college": college.name
        })
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 201)
        
        department1 = self.client.delete('/department/' + str(d0_json_string['id']) + '/')
        d1_json_string = json.loads(department1.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 204)
        

    def test_bad_delete(self):
        college = College(name='College of Eternity')
        college.save()
        department0 = self.client.post('/department/',
        {
            "name": "Indestructible Department",
            "college": college.name
        })
        d0_json_string = json.loads(department0.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 201)
        
        department1 = self.client.delete('/department/' + str(d0_json_string['id'] + 1) + '/')
        d1_json_string = json.loads(department1.content.decode('utf-8'))
        self.assertEqual(department0.status_code, 400)
        
        
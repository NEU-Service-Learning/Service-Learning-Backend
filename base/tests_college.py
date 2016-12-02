from django.test import TestCase
from django.test import Client
from base.models import *
import json

class ProjectTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_good_post(self):
        college0 = self.client.post('/college/',
        {
            "name": "College of Computer and Information Science"
        })
        self.assertEqual(college0.status_code, 201)
        c0_json_string = json.loads(college0.content.decode('utf-8'))
        self.assertEqual(c0_json_string['name'], "College of Computer and Information Science")
        
    def test_bad_post_no_name(self):
        college0 = self.client.post('/college/', {})
        self.assertEqual(college0.status_code, 400)
        
    def test_get_good(self):
        college0 = self.client.post('/college/', 
        {
            "name": "School of Law"
        })
        self.assertEqual(college0.status_code, 201)
        c0_json_string = json.loads(college0.content.decode('utf-8'))
        college1 = self.client.get('/college/' + str(c0_json_string['name']) + '/')
        self.assertEqual(college1.status_code, 201)
        c1_json_string = json.loads(college1.content.decode('utf-8'))
        self.assertEqual(c1_json_string['name'], "School of Law")
        
    def test_bad_get(self):
        college0 = self.client.get('/college/01822/')
        self.assertEqual(college1.status_code, 404)
        
    def test_good_put(self):
        college0 = self.client.post('/college/', 
        {
            "name": "College of Engineering"
        })
        self.assertEqual(college0.status_code, 201)
        c0_json_string = json.loads(college0.content.decode('utf-8'))
        
        temp_dict = {
            "name": "School of Engineering"
        }
        college1 = self.client.put('/college/' + str(c0_json_string['name']) + '/', json.dumps(temp_dict), content_type="application/json")
        
        self.assertEqual(college1.status_code, 201)
        c1_json_string = json.loads(college1.content.decode('utf-8'))
        self.assertEqual(c1_json_string['name'], "School of Engineering")
        college2 = self.client.get('/college/' + str(c1_json_string['name']) + '/')
        self.assertEqual(college2.status_code, 201)
        c2_json_string = json.loads(college2.content.decode('utf-8'))
        self.assertEqual(c1_json_string['name'], "School of Engineering")
        
    def test_bad_put(self):
        college0 = self.client.post('/college/', 
        {
            "name": "Boovy College of Health Sciences"
        })
        self.assertEqual(college0.status_code, 201)
        c0_json_string = json.loads(college0.content.decode('utf-8'))
        college1 = self.client.put('/college/' + str(c0_json_string['name']) + '/', json.dumps({}), content_type="application/json")
        self.assertEqual(college1.status_code, 400)
        
    def test_delete(self):
        college0 = self.client.post('/college/', 
        {
            "name": "School of Money"
        })
        self.assertEqual(college0.status_code, 201)
        c0_json_string = json.loads(college0.content.decode('utf-8'))
        college1 = self.client.delete('/college/' + str(c0_json_string['name']) + '/')
        self.assertEqual(college1.status_code, 204)

from django.test import TestCase
from django.test import Client
from base.models import *
import json

# Create your tests here.

class ExampleMethodTests(TestCase):

	def test_basic_example_addition(self):
		self.assertIs(1+1, 2)

	def test_basic_example_strings(self):
		self.assertIs("this is a test", "this is a test")

		
class SemesterTests(TestCase):
	def setUp(self):
		self.client = Client()
	
	def basic_post_semester(self):
	
		semester = self.client.add('/semester/',
		{
			"name": "FALL2016",
			"start date": "2016-09-01",
			"end date": "2016-12-31",
			"is active": true
		})
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(semester.context['name'], "FALL2016")
		self.assertEqual(semester.context['is active'], true)
		semester = self.client.add('/semester/',
		{
			"name": "FALL2017",
			"start date": "2017-09-01",
			"end date": "2017-12-31",
			"is active": false
		})
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(semester.context['name'], "FALL2017")
		self.assertEqual(semester.context['is active'], false)
		
	def bad_post_semester(self):
	
		# Semester with inconsistent dates
		semester = self.client.add('/semester/',
		{
			"name": "FALL2016",
			"start date": "2016-12-31",
			"end date": "2016-09-01",
			"is active": false
		})
		self.assertEqual(semester.status_code, 422)
		
		# Semester with non-string name
		semester = self.client.add('/semester/',
		{
			"name": True,
			"start date": "2016-09-01",
			"end date": "2016-12-31",
			"is active": true
		})
		self.assertEqual(semester.status_code, 422)
		
		# Semester with non-date start
		semester = self.client.add('/semester/',
		{
			"name":	 "FALL2016",
			"start date": "Yesterday",
			"end date": "2016-12-31",
			"is active": true
		})
		self.assertEqual(semester.status_code, 422)
		
		# Semester with non-date end
		semester = self.client.add('/semester/',
		{
			"name":	 "FALL2016",
			"start date": "2016-09-01",
			"end date": 45,
			"is active": true
		})
		self.assertEqual(semester.status_code, 422)
	
	def basic_put_semester(self):
	
		# Set up semester
		semester = self.client.add('/semester/',
		{
			"name":	 "FALL2016",
			"start date": "2016-09-01",
			"end date": "2016-12-31",
			"is active": false
		})
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(semester.context['is active'], false)
		
		# Modify the semester
		semester.client.put('/semester/{semester_id}'.format(semester_id = semester.context['id']),
		{
			"id": semester.context['id']
			"name":	"FALL2016",
			"start date": "2016-09-01",
			"end date": "2016-12-31",
			"is active": true
		})
		self.assertEqual(semester.status_code, 200)
		self.assertEqual(semester.context['is active'], true)
		
	def bad_put_semester(self):
		
		# Set up semester
		semester = self.client.add('/semester/',
		{
			"name":	 "FALL2016",
			"start date": "2016-09-01",
			"end date": "2016-12-31",
			"is active": false
		})
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(semester.context['is active'], false)
		
		# Modify the semester with bad is_active
		semester.client.put('/semester/{semester_id}'.format(semester_id = semester.context['id']),
		{
			"name":	 "FALL2016",
			"start date": "2016-09-01",
			"end date": "2016-12-31",
			"is active": "sometimes"
		})
		self.assertEqual(semester.status_code, 422)
		
		# Modify the semester with bad start_date
		semester.client.put('/semester/{semester_id}'.format(semester_id = semester.context['id']),
		{
			"name":	 "FALL2016",
			"start date": "2017-09-01",
			"end date": "2016-12-31",
			"is active": false
		})
		self.assertEqual(semester.status_code, 422)
		
		# Modify the semester with bad end_date
		semester.client.put('/semester/{semester_id}'.format(semester_id = semester.context['id']),
		{
			"name":	 "FALL2016",
			"start date": "2016-09-01",
			"end date": "2016-08-31",
			"is active": false
		})
		self.assertEqual(semester.status_code, 422)
		
	def start_semester(self):
		
		# Set up current semester
		first_semester = self.client.add('/semester/',
		{
			"name": "FALL2016",
			"start date": "2016-09-01",
			"end date": "2016-12-31",
			"is active": true
		})
		self.assertEqual(first_semester.status_code, 201)
		self.assertEqual(first_semester.context['name'], "FALL2016")
		self.assertEqual(first_semester.context['is active'], true)
		
		# Set up the semester to transition to
		second_semester = self.client.add('/semester/',
		{
			"name": "FALL2017",
			"start date": "2017-09-01",
			"end date": "2017-12-31",
			"is active": false
		})
		self.assertEqual(second_semester.status_code, 201)
		self.assertEqual(second_semester.context['name'], "FALL2017")
		self.assertEqual(second_semester.context['is active'], false)
		
		# Change semester
		next_semester = self.client.get('/semester/start_next')
		self.assertEqual(next_semester.status_code, 200)
		
		# Verify that first is inactivated and second is activated
		next_semester = self.client.get('/semester/', second_semester.context['id'])
		assertEqual(next_semester.context['is active'], true)
		
		first_semester = self.client.get('/semester/', first_semester.context['id'])
		assertEqual(first_semester.context['is active'], false)
		

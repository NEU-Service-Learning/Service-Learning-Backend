from django.test import TestCase
from django.test import Client
from base.models import *
import json
from datetime import datetime


class SemesterTests(TestCase):
	def setUp(self):
		self.client = Client()

	def test_basic_post_semester(self):


		semester = self.client.post('/semester/',
		{
			"name": "FALL2019",
			"start_date": "2019-09-01",
			"end_date": "2019-12-31",
			"is_active": 'true'
		})
		s0_json = json.loads(semester.content.decode('utf-8'))
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(s0_json['name'], "FALL2019")
		self.assertEqual(s0_json['is_active'], True)
		semester = self.client.post('/semester/',
		{
			"name": "FALL2020",
			"start_date": "2020-09-01",
			"end_date": "2020-12-31",
			"is_active": 'false'
		})
		s1_json = json.loads(semester.content.decode('utf-8'))
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(s1_json['name'], "FALL2020")
		self.assertEqual(s1_json['is_active'], False)

	def test_bad_get_semester(self):

		# Semester that does not exist
		semester = self.client.get('/semester/SPRING93/')
		self.assertEqual(semester.status_code, 404)

	def test_bad_post_semester(self):

		# Semester with inconsistent_dates
		semester = self.client.post('/semester/',
		{
			"name": "FALL2016",
			"start_date": "2016-12-31",
			"end_date": "2016-09-01",
			"is_active": 'false'
		})
		self.assertEqual(semester.status_code, 400)

		# Semester with no data
		semester = self.client.post('/semester/', {})
		self.assertEqual(semester.status_code, 400)

	def test_basic_put_semester(self):

		# Set up semester
		semester = self.client.post('/semester/',
		{
			"name":	 "FALL2016",
			"start_date": "2016-09-01",
			"end_date": "2016-12-31",
			"is_active": 'false'
		})
		s0_json = json.loads(semester.content.decode('utf-8'))
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(s0_json['is_active'], False)

		# Modify the semester
		semester = self.client.put('/semester/{semester_id}/'.format(semester_id = s0_json['name']),json.dumps(
		{
			"name":	"FALL2016",
			"start_date": "2016-09-01",
			"end_date": "2016-12-31",
			"is_active": 'true'
		}), content_type="application/json")
		s1_json = json.loads(semester.content.decode('utf-8'))
		self.assertEqual(semester.status_code, 200)
		self.assertEqual(s1_json['is_active'], True)

	def test_bad_put_semester(self):

		# Set up semester
		semester = self.client.post('/semester/',
		{
			"name":	 "FALL2016",
			"start_date": "2016-09-01",
			"end_date": "2016-12-31",
			"is_active": 'false'
		})
		s0_json = json.loads(semester.content.decode('utf-8'))
		self.assertEqual(semester.status_code, 201)
		self.assertEqual(s0_json['is_active'], False)

		# Modify the semester with bad is_active
		semester = self.client.put('/semester/{semester_id}/'.format(semester_id = s0_json['name']),json.dumps(
		{
			"name":	 "FALL2016",
			"start_date": "2016-09-01",
			"end_date": "2016-12-31",
			"is_active": None,
		}), content_type="application/json")
		self.assertEqual(semester.status_code, 400)

		# Modify the semester with bad start_date
		semester = self.client.put('/semester/{semester_id}/'.format(semester_id = s0_json['name']),json.dumps(
		{
			"name":	 "FALL2016",
			"start_date": "2017-09-01",
			"end_date": "2016-12-31",
			"is_active": 'false'
		}), content_type="application/json")
		self.assertEqual(semester.status_code, 400)

		# Modify the semester with bad end_date
		semester = self.client.put('/semester/{semester_id}/'.format(semester_id = s0_json['name']),json.dumps(
		{
			"name":	 "FALL2016",
			"start_date": "2016-09-01",
			"end_date": "2016-08-31",
			"is_active": 'false'
		}), content_type="application/json")
		self.assertEqual(semester.status_code, 400)

	def test_start_semester(self):

		# Set up current semester
		first_semester = self.client.post('/semester/',
		{
			"name": "FALL2016",
			"start_date": "2016-09-01",
			"end_date": "2016-12-31",
			"is_active": 'true'
		})
		s0_json = json.loads(first_semester.content.decode('utf-8'))
		self.assertEqual(first_semester.status_code, 201)
		self.assertEqual(s0_json['name'], "FALL2016")
		self.assertEqual(s0_json['is_active'], True)

		# Set up the semester to transition to
		second_semester = self.client.post('/semester/',
		{
			"name": "FALL2017",
			"start_date": "2017-09-01",
			"end_date": "2017-12-31",
			"is_active": 'false'
		})
		self.college = College("hello")
		self.college.save()
		self.department = Department("test", self.college.name)
		self.department.save()
		self.course = Course("CS4500", "Software Dev", self.department.name)
		self.course.save()
		self.user = User(username="kename.f@neu.edu", first_name="Fa", password="password1")
		self.user.save()
		self.semester = Semester(name="sem1", start_date=datetime.now(), end_date=datetime.now(), is_active=False)
		self.semester.save()
		enrollment = Enrollment(user=self.user, course=self.course, semester=self.semester, meeting_days="MWF", meeting_start_time=datetime.now().time(), meeting_end_time=datetime.now().time(), crn="12345", is_active=False)
		enrollment.save()
		self.semester = Semester(name="sem2", start_date=datetime.now(), end_date=datetime.now(), is_active=False)
		self.semester.save()
		enrollment = Enrollment(user=self.user, course=self.course, semester=self.semester, meeting_days="MWF", meeting_start_time=datetime.now().time(), meeting_end_time=datetime.now().time(), crn="12345", is_active=False)
		enrollment.save()

		s1_json = json.loads(second_semester.content.decode('utf-8'))
		self.assertEqual(second_semester.status_code, 201)
		self.assertEqual(s1_json['name'], "FALL2017")
		self.assertEqual(s1_json['is_active'], False)

		# Change semester
		next_semester = self.client.post('/semester/startnext/')
		self.assertEqual(next_semester.status_code, 200)

		# Verify that first is inactivated and second is activated
		next_semester = self.client.get('/semester/'+ s1_json['name'] + '/')
		s1_json = json.loads(next_semester.content.decode('utf-8'))
		self.assertEqual(s1_json['is_active'], True)

		first_semester = self.client.get('/semester/'+ s0_json['name'] + '/')
		s0_json = json.loads(first_semester.content.decode('utf-8'))
		self.assertEqual(s0_json['is_active'], False)

		# Verify that we can't move to the next semester if there is none
		next_semester = self.client.post('/semester/startnext/')
		self.assertEqual(next_semester.status_code, 404)

	def test_start_semester_2(self):

		# Set up current semester
		first_semester = self.client.post('/semester/',
		{
			"name": "FALL2016",
			"start_date": "2016-09-01",
			"end_date": "2016-12-31",
			"is_active": 'true'
		})
		s0_json = json.loads(first_semester.content.decode('utf-8'))
		self.assertEqual(first_semester.status_code, 201)
		self.assertEqual(s0_json['name'], "FALL2016")
		self.assertEqual(s0_json['is_active'], True)

		# Set up the semester to transition to
		second_semester = self.client.post('/semester/',
		{
			"name": "FALL2017",
			"start_date": "2017-09-01",
			"end_date": "2017-12-31",
			"is_active": 'false'
		})
		self.college = College("hello")
		self.college.save()
		self.department = Department("test", self.college.name)
		self.department.save()
		self.course = Course("CS4500", "Software Dev", self.department.name)
		self.course.save()
		self.user = User(username="kename.f@neu.edu", first_name="Fa", password="password1")
		self.user.save()
		self.semester = Semester(name="sem1", start_date=datetime.now(), end_date=datetime.now(), is_active=False)
		self.semester.save()
		enrollment = Enrollment(user=self.user, course=self.course, semester=self.semester, meeting_days="MWF", meeting_start_time=datetime.now().time(), meeting_end_time=datetime.now().time(), crn="12345", is_active=True)
		enrollment.save()
		self.semester = Semester(name="sem2", start_date=datetime.now(), end_date=datetime.now(), is_active=False)
		self.semester.save()
		enrollment = Enrollment(user=self.user, course=self.course, semester=self.semester, meeting_days="MWF", meeting_start_time=datetime.now().time(), meeting_end_time=datetime.now().time(), crn="12345", is_active=True)
		enrollment.save()

		s1_json = json.loads(second_semester.content.decode('utf-8'))
		self.assertEqual(second_semester.status_code, 201)
		self.assertEqual(s1_json['name'], "FALL2017")
		self.assertEqual(s1_json['is_active'], False)

		# Change semester
		next_semester = self.client.post('/semester/startnext/')
		self.assertEqual(next_semester.status_code, 200)

		# Verify that first is inactivated and second is activated
		next_semester = self.client.get('/semester/'+ s1_json['name'] + '/')
		s1_json = json.loads(next_semester.content.decode('utf-8'))
		self.assertEqual(s1_json['is_active'], True)

		first_semester = self.client.get('/semester/'+ s0_json['name'] + '/')
		s0_json = json.loads(first_semester.content.decode('utf-8'))
		self.assertEqual(s0_json['is_active'], False)

		# Verify that we can't move to the next semester if there is none
		next_semester = self.client.post('/semester/startnext/')
		self.assertEqual(next_semester.status_code, 404)
		

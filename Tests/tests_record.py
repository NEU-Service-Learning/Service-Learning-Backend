import unittest
import sys
from django.test import TestCase
from django.test import Client
from base.models import Record


# Unit Tests for Record Model


class ExampleTest(TestCase):
    def test_equal(self):
        self.assertEquals(True, True)
        self.assertEquals("test", "test")

    def test_addition(self):
        self.assertEquals(1 + 1, 2)


# POST TESTS #
class RecordPostTest(TestCase):
    def setUp(self):
        self.Client = Client()

    # Simple creation of Record
    # -(id is auto-incremented in database)
    # -optional fields: start_time, Location, comments, extra_field
    def test_basic_post(self):
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4.5,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': "{'employees':[{'firstName':'John', 'lastName':'Doe'}, "
                                                     "{'firstName':'Peter', 'lastName':'Jones'}]}"
                                  })
        self.assertEquals(record.status_code, 200)
        self.assertEquals(record.context['enrollment'], 1)
        self.assertEquals(record.context['project'], 1002)
        self.assertEquals(record.context['date'], "2016-11-27")
        self.assertEquals(record.context['start_time'], "08:00")
        self.assertEquals(record.context['total_hours'], 4)
        self.assertEquals(record.context['longitude'], 42.3399)
        self.assertEquals(record.context['latitude'], 71.0891)
        self.assertEquals(record.context['category'], 2)
        self.assertEquals(record.context['comments'], "Comments")
        self.assertEquals(record.context['extra_field'], None)

    # invalid or missing enrollment
    def test_enrollment(self):
        # null enrollment
        record = self.client.post('/record/',
                                  {
                                      'enrollment': None,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid enrollment (negative int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': -1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid enrollment (zero)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 0,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid enrollment (decimal)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 10.1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # valid enrollment (max int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': sys.maxsize,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # invalid enrollment (max int + 1)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': sys.maxsize + 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid or missing project
    def test_project(self):
        # null project
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': None,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid project (negative int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': -1001,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid project (zero)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 0,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid project (decimal)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1001.2,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # valid project (max int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': sys.maxsize,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # invalid project (max int + 1)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': sys.maxsize + 1,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid or missing date
    def test_date(self):
        # null date
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 2,
                                      'project': 1002,
                                      'date': None,
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid date (incomplete entry)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid date (non-date string)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "apples",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid date (decimal)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': 12.2,
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid start_time
    def test_start_time(self):
        # null start_time (int) --> VALID
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': None,
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # invalid start_time (int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': 8,
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid start_time (time doesn't exist)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "24:01",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid start_time (non-time string)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': "1",
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "apples",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid or missing total_hours
    def test_total_hours(self):
        # null total_hours
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': None,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid total_hours (negative number)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': -4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid total_hours (must be greater than zero)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 0,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # valid total_hours (24 hours)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 24,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # invalid total_hours (24.01 hours)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 25,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid longitude
    def test_longitude(self):
        # null longitude (and latitude) --> VALID
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': None,
                                      'latitude': None,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # null longitude (latitude correct) --> INVALID
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': None,
                                      'latitude': 34.8954,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid longitude (non-Decimal)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': "56.8908",
                                      'latitude': 34.8954,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid longitude (max-int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': sys.maxsize,
                                      'latitude': 34.8954,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid latitude
    def test_latitude(self):
        # null latitude (and longitude) --> VALID
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': None,
                                      'latitude': None,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # null latitude (longitude correct) --> INVALID
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 65.9880,
                                      'latitude': None,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid latitude (non-Decimal)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 56.8908,
                                      'latitude': "34.8954",
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid latitude (max-int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 56.8908,
                                      'latitude': sys.maxsize,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid or missing category
    def test_category(self):
        # null category
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 2,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': None,
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid category (negative int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': -2,
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid category (zero)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': 0,
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid category (max int)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': sys.maxsize,
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid category (max int + 1)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': sys.maxsize + 1,
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid category (non-enum String)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TS",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid or missing active indicator
    def test_is_active(self):
        # on creation of new model, should default to True
        # null is_active
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': None,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid is_active (non-boolean)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': "Hello",
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # valid is_active (1)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': 1,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # invalid is_active (False)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': False,  # should default to True on creation
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid comments
    def test_comments(self):
        # null comments --> VALID
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # invalid comments (empty string)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "",
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid comments (decimal)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': "4",
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': 12.1,
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 400)

    # invalid extra_field
    def test_extra_field(self):
        # null extra_field --> VALID
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': None,
                                      'extra_field': None
                                  })
        self.assertEqual(record.status_code, 200)

        # invalid extra_field (non-json)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': 12
                                  })
        self.assertEqual(record.status_code, 400)

        # invalid extra_field (json of invalid format)
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 3,
                                      'longitude': 42.3399,
                                      'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': "{'employees':[{'firstName':'John', 'lastName':'Doe'}, "
                                                     "{'firstName':'Peter'}]}"
                                  })
        self.assertEqual(record.status_code, 400)


# GET TESTS #
class RecordGetTests(TestCase):
    # simple get request for Record
    def test_basic_get(self):
        # create a basic record
        tempRecord = self.client.post('/record/',
                                      {
                                          'enrollment': 1,
                                          'project': 1002,
                                          'date': "2016-11-27",
                                          'start_time': "08:00",
                                          'total_hours': 4.5,
                                          'longitude': 42.3399,
                                          'latitude': 71.0891,
                                          'category': "TO",
                                          'is_active': True,
                                          'comments': "Comments",
                                          'extra_field': "{'employees':[{'firstName':'John', 'lastName':'Doe'}, "
                                                         "{'firstName':'Peter', 'lastName':'Jones'}]}"
                                      })
        record = self.client.get('/record/', tempRecord.context['id'])
        self.assertEqual(record.context['enrollment'], tempRecord.context['enrollment'])
        self.assertEqual(record.context['date'], tempRecord.context['date'])
        self.assertEqual(record.context['start_time'], tempRecord.context['start_time'])
        self.assertEqual(record.context['total_hours'], tempRecord.context['total_hours'])
        self.assertEqual(record.context['category'], tempRecord.context['category'])
        self.assertEqual(record.context['is_active'], tempRecord.context['is_active'])
        self.assertEqual(record.context['comments'], tempRecord.context['comments'])
        self.assertEqual(record.context['extra_field'], tempRecord.context['extra_field'])

    # invalid get request --> id does not exist
    def test_no_id(self):
        record = self.client.get('/record/', sys.maxsize)
        self.assertEqual(record.status_code, 400)

    # invalid get request --> null or non-int id
    def test_invalid_id(self):
        record = self.client.get('/record/', None)
        self.assertEqual(record.status_code, 400)
        record = self.client.get('/record/', "12")
        self.assertEqual(record.status_code, 400)


# PUT TESTS ##
class RecordPutTests(TestCase):
    # simple put request for Record
    def test_basic_put(self):
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4.5,
                                      'longitude': 42.3399, 'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': "{'employees':[{'firstName':'John', 'lastName':'Doe'}, "
                                                     "{'firstName':'Peter', 'lastName':'Jones'}]}"
                                  })
        self.assertEqual(record.status_code, 200)
        self.assertTrue(record.context['is_active'])
        self.client.put('/record', {
            'enrollment': 1,
            'project': 1002,
            'date': "2016-11-27",
            'start_time': "08:00",
            'total_hours': 4.5,
            'longitude': 42.3399,
            'latitude': 71.0891,
            'category': "TO",
            'is_active': False,
            'comments': "Comments",
            'extra_field': "{'employees':[{'firstName':'John', 'lastName':'Doe'}, "
                           "{'firstName':'Peter', 'lastName':'Jones'}]}"
        })
        self.assertEqual(record.status_code, 200)
        self.assertFalse(record.context['is_active'])

    # invalid put request --> update non-is_update field
    def test_invalid_put(self):
        record = self.client.post('/record/',
                                  {
                                      'enrollment': 1,
                                      'project': 1002,
                                      'date': "2016-11-27",
                                      'start_time': "08:00",
                                      'total_hours': 4.5,
                                      'longitude': 42.3399, 'latitude': 71.0891,
                                      'category': "TO",
                                      'is_active': True,
                                      'comments': "Comments",
                                      'extra_field': "{'employees':[{'firstName':'John', 'lastName':'Doe'}, "
                                                     "{'firstName':'Peter', 'lastName':'Jones'}]}"
                                  })
        self.assertEqual(record.status_code, 200)
        self.assertTrue(record.context['is_active'])
        self.client.put('/record', {
            'enrollment': 1,
            'project': 1003,  # edited
            'date': "2016-11-27",
            'start_time': "08:00",
            'total_hours': 4.5,
            'longitude': 42.3399,
            'latitude': 71.0891,
            'category': "TO",
            'is_active': True,
            'comments': "Comments",
            'extra_field': "{'employees':[{'firstName':'John', 'lastName':'Doe'}, "
                           "{'firstName':'Peter', 'lastName':'Jones'}]}"
        })
        self.assertEqual(record.status_code, 400)

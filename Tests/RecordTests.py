import unittest
from django.test import TestCase
from record.model import Record

#Unit Tests for Record Model


class ExampleTest(TestCase):

    def equalTest(self):
        self.assertEquals(True, True)
        self.assertEquals("test", "test")

    def additionTest(self):
        self.assertEquals(1+1,2)


##POST TESTS##
class RecordPostTest(TestCase):
    #Simple creation of Record
    # -(id is auto-incremented in database)
    # -optional fields: start_time, Location, comments, extra_field
    def basicPostTest(self):
        record = self.client.add('/record/',
            {
                enrollment: 1,
                project: 1002,
                date: "2016-11-27",
                start_time: "08:00",
                total_hours: 4.5,
                longitude: 42.3399,
                latitude: 71.0891,
                category: 2,
                is_active: True,
                comments: "Comments",
                extra_field: "{'employees':[{'firstName':'John', 'lastName':'Doe'}, {'firstName':'Peter', 'lastName':'Jones'}]}"
            })
        self.assertEquals(record.status_code, 201)
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

    #invalid or missing enrollment
    def badEnrollmentTest(self):
        #null enrollment
        record = self.client.add('/record/',
                                 {
                                     enrollment: None,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid enrollment (negative int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: -1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        #invalid enrollment (zero)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 0,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        #invalid enrollment (decimal)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 10.1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        #valid enrollment (max int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: sys.maxsize,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        #invalid enrollment (max int + 1)
        record = self.client.add('/record/',
                                 {
                                     enrollment: sys.maxsize + 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid or missing project
    def badProjectTest(self):
        # null project
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: None,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid project (negative int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: -1001,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid project (zero)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 0,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid project (decimal)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1001.2,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # valid project (max int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: sys.maxsize,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # invalid project (max int + 1)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: sys.maxsize + 1,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid or missing date
    def badDateTest(self):
        # null date
        record = self.client.add('/record/',
                                 {
                                     enrollment: 2,
                                     project: 1002,
                                     date: None,
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid date (incomplete entry)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid date (non-date string)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "apples",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid date (decimal)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: 12.2,
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid start_time
    def badStartTest(self):
        # null start_time (int) --> VALID
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: None,
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # invalid start_time (int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: 8,
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        #invalid start_time (time doesn't exist)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "24:01",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid start_time (non-time string)
        record = self.client.add('/record/',
                                 {
                                     enrollment: "1",
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "apples",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid or missing total_hours
    def badTotalHoursTest(self):
        # null total_hours
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: None,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid total_hours (negative number)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: -4,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid total_hours (must be greater than zero)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 0,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # valid total_hours (24 hours)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 24,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # invalid total_hours (24.01 hours)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 25,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid longitude
    def badLongitudeTest(self):
        # null longitude (and latitude) --> VALID
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: None,
                                     latitude: None,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # null longitude (latitude correct) --> INVALID
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: None,
                                     latitude: 34.8954,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid longitude (non-Decimal)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: "56.8908",
                                     latitude: 34.8954,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)


        # invalid longitude (max-int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: sys.maxsize,
                                     latitude: 34.8954,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid latitude
    def badLatitudeTest(self):
        # null latitude (and longitude) --> VALID
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: None,
                                     latitude: None,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # null latitude (longitude correct) --> INVALID
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 65.9880,
                                     latitude: None,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid latitude (non-Decimal)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 56.8908,
                                     latitude: "34.8954",
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)


        # invalid latitude (max-int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 56.8908,
                                     latitude: sys.maxsize,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid or missing category
    def badCategoryTest(self):
        # null category
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 2,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: None,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid category (negative int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: -2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid category (zero)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 0,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid category (decimal)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 2.4,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # valid category (max int)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: sys.maxsize,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # valid category (max int + 1)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: sys.maxsize + 1,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

    #invalid or missing active indicator
    def badIsActiveTest(self):
        #on creation of new model, should default to True
        # null is_active
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: None,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid is_active (non-boolean)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: "Hello",
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid is_active (non-boolean)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: 0, #zero is not False for the Record Model
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid is_active (False)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: False, #should default to True on creation
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid comments
    def badCommentTest(self):
        # null comments --> VALID
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # invalid comments (empty string)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "",
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid comments (decimal)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: "4",
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: 12.1,
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 422)

    #invalid extra_field
    def badExtraField(self):
        # null extra_field --> VALID
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: None,
                                     extra_field: None
                                 })
        self.assertEqual(record.status_code, 201)

        # invalid extra_field (non-json)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: 12
                                 })
        self.assertEqual(record.status_code, 422)

        # invalid extra_field (json of invalid format)
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 3,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: "{'employees':[{'firstName':'John', 'lastName':'Doe'}, {'firstName':'Peter'}]}"
                                 })
        self.assertEqual(record.status_code, 422)


##GET TESTS ##
class RecordGetTests(TestCase):

    #simple get request for Record
    def basicGetTest(self):
        #create a basic record
        tempRecord = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4.5,
                                     longitude: 42.3399,
                                     latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: "{'employees':[{'firstName':'John', 'lastName':'Doe'}, {'firstName':'Peter', 'lastName':'Jones'}]}"
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

    #invalid get request --> id does not exist
    def badGetNoIDTest(self):
        record = self.client.get('/record/', sys.maxsize)
        self.assertEqual(record.status_code, 422)

    #invalid get request --> null or non-int id
    def badGetInvalidTest(self):
        record = self.client.get('/record/', None)
        self.assertEqual(record.status_code, 422)
        record = self.client.get('/record/', "12")
        self.assertEqual(record.status_code, 422)


#PUT TESTS ##
class RecordPutTests(TestCase):

    #simple put request for Record
    def basicPutTest(self):
        record = self.client.add('/record/',
                                     {
                                         enrollment: 1,
                                         project: 1002,
                                         date: "2016-11-27",
                                         start_time: "08:00",
                                         total_hours: 4.5,
                                         longitude: 42.3399,                 latitude: 71.0891,
                                         category: 2,
                                         is_active: True,
                                         comments: "Comments",
                                         extra_field: "{'employees':[{'firstName':'John', 'lastName':'Doe'}, {'firstName':'Peter', 'lastName':'Jones'}]}"
                                     })
        self.assertEqual(record.status_code, 201)
        self.assertTrue(record.context['is_active'])
        self.client.put('/record', {
                                         enrollment: 1,
                                         project: 1002,
                                         date: "2016-11-27",
                                         start_time: "08:00",
                                         total_hours: 4.5,
                                         longitude: 42.3399,
                                         latitude: 71.0891,
                                         category: 2,
                                         is_active: False,
                                         comments: "Comments",
                                         extra_field: "{'employees':[{'firstName':'John', 'lastName':'Doe'}, {'firstName':'Peter', 'lastName':'Jones'}]}"
                                     })
        self.assertEqual(record.status_code, 201)
        self.assertFalse(record.context['is_active'])

    #invalid put request --> update non-is_update field
    def badPutTest(self):
        record = self.client.add('/record/',
                                 {
                                     enrollment: 1,
                                     project: 1002,
                                     date: "2016-11-27",
                                     start_time: "08:00",
                                     total_hours: 4.5,
                                     longitude: 42.3399,                 latitude: 71.0891,
                                     category: 2,
                                     is_active: True,
                                     comments: "Comments",
                                     extra_field: "{'employees':[{'firstName':'John', 'lastName':'Doe'}, {'firstName':'Peter', 'lastName':'Jones'}]}"
                                 })
        self.assertEqual(record.status_code, 201)
        self.assertTrue(record.context['is_active'])
        self.client.put('/record', {
            enrollment: 1,
            project: 1003, #edited
            date: "2016-11-27",
            start_time: "08:00",
            total_hours: 4.5,
            longitude: 42.3399,
            latitude: 71.0891,
            category: 2,
            is_active: True,
            comments: "Comments",
            extra_field: "{'employees':[{'firstName':'John', 'lastName':'Doe'}, {'firstName':'Peter', 'lastName':'Jones'}]}"
        })
        self.assertEqual(record.status_code, 422)

from django.test import TestCase

# Create your tests here.

class ExampleMethodTests(TestCase):

    def test_basic_example_addition(self):
        self.assertIs(1+1, 2)

    def test_basic_example_strings(self):
        self.assertIs("this is a test", "this is a test")

class ProjectTests(TestCase):

    def setUp(self):
        self.client = Client()

    def basic_post_test(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })
        self.assertEqual(project0.status_code, 201)
        self.assertEqual(project0.context['name'], "Service Learning Time Tracker")
        self.assertEqual(project0.context['community_partner'], communityPartner0.context['id'])
        self.assertEqual(project0.context['description'], "Time Tracking")
        self.assertEqual(project0.context['start_date'], "2016-12-12")
        self.assertEqual(project0.context['end_date'], "2016-12-13")
        self.assertEqual(project0.context['longitude'], "40.0")
        self.assertEqual(project0.context['latitude'], "30.0")

    def bad_post_no_name(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })
        self.assertEqual(project0.status_code, 422)

    def bad_post_no_community_partner(self):
        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })
        self.assertEqual(project0.status_code, 422)

    def bad_post_no_description(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })
        self.assertEqual(project0.status_code, 422)

    def bad_post_no_start_date(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })
        self.assertEqual(project0.status_code, 422)

    def bad_post_no_end_date(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "longitude": "40.0",
            "latitude": "30.0"
        })
        self.assertEqual(project0.status_code, 422)

    def bad_post_no_longitude(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "latitude": "30.0"
        })
        self.assertEqual(project0.status_code, 422)

    def bad_post_no_latitude(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
        })
        self.assertEqual(project0.status_code, 422)

    def update_test(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })

        communityPartner1 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 1"
        })

        project0Updated = self.client.update('/project/', project0.context['id'],
        {
            "id": project0.context['id'],
            "name": "Updated SL Time Tracker",
            "community_partner": communityPartner1.context['id'],
            "description": "Updated Time Tracking",
            "start_date": "2017-11-11",
            "end_date": "2017-12-11",
            "longitude": "20.0",
            "latitude": "10.0"
        })
        self.assertEqual(project0Updated.status_code, 201)
        self.assertEqual(project0Updated.context['name'], "Updated SL Time Tracker")
        self.assertEqual(project0Updated.context['community_partner'], communityPartner1.context['id'])
        self.assertEqual(project0Updated.context['description'], "Updated Time Tracking")
        self.assertEqual(project0Updated.context['start_date'], "2017-11-11")
        self.assertEqual(project0Updated.context['end_date'], "2017-12-11")
        self.assertEqual(project0Updated.context['longitude'], "20.0")
        self.assertEqual(project0Updated.context['latitude'], "10.0")

    def bad_update_test(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })

        project0Updated = self.client.update('/project/', project0.context['id'], {})
        self.assertEqual(project0Updated.status_code, 422)

    def get_test(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })

        project0 = self.client.add('/project/',
        {
            "name": "Service Learning Time Tracker",
            "community_partner": communityPartner0.context['id'],
            "description": "Time Tracking",
            "start_date": "2016-12-12",
            "end_date": "2016-12-13",
            "longitude": "40.0",
            "latitude": "30.0"
        })

        project1 = self.client.get('/project/', project0.context['id'])
        self.assertEqual(project1.context['id'], project0.context['id'])
        self.assertEqual(project1.context['community_partner'], project0.context['community_partner'])
        self.assertEqual(project1.context['description'], project0.context['description'])
        self.assertEqual(project1.context['start_date'], project0.context['start_date'])
        self.assertEqual(project1.context['end_date'], project0.context['end_date'])
        self.assertEqual(project1.context['longitude'], project0.context['longitude'])
        self.assertEqual(project1.context['latitude'], project0.context['latitude'])

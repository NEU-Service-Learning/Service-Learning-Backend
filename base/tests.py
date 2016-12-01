from django.test import TestCase

# Create your tests here.

class ExampleMethodTests(TestCase):

    def test_basic_example_addition(self):
        self.assertIs(1+1, 2)

    def test_basic_example_strings(self):
        self.assertIs("this is a test", "this is a test")

class CommunityPartnerTests(TestCase):

    def setUp(self):
        self.client = Client()

    def basic_post_test(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })
        self.assertEqual(communityPartner0.status_code, 201)
        self.assertEqual(communityPartner0.context['name'], "Example Community Partner 0")

    def post_no_name_test(self):
        communityPartner0 = self.client.add('/communityPartner/', {})
        self.assertEqual(communityPartner0.status_code, 422)

    def update_test(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })
        CPid = communityPartner0.context['id']
        communityPartner0Updated = self.client.update('/communityPartner/', CPid,
        {
            "id": CPid,
            "name": "Updated Community Partner Name"
        })
        self.assertEqual(communityPartner0Updated.context['id'], CPid)
        self.assertEqual(communityPartner0Updated.context['name'], "Updated Community Partner Name")

    def get_test(self):
        communityPartner0 = self.client.add('/communityPartner/',
        {
            "name": "Example Community Partner 0"
        })
        CPid = communityPartner0.context['id']
        communityPartner1 = self.client.get('/communityPartner/', CPid)
        self.assertEqual(communityPartner1.context['id'], communityPartner0.context['id'])
        self.assertEqual(communityPartner1.context['name'], communityPartner0.context['name'])

    def bad_get_test(self):
        communityPartner0 = self.client.get('/communityPartner/', 99999)
        self.assertEqual(communityPartner0.status_code, 422)
        communityPartner0 = self.client.get('/communityPartner/', "99999")
        self.assertEqual(communityPartner0.status_code, 422)

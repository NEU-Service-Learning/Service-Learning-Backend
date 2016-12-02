from django.test import TestCase
from django.test import Client
from base.models import *
import json

class ProjectTests(TestCase):

    def setUp(self):
        self.client = Client()

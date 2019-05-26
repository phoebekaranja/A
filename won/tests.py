from django.test import TestCase
from .models import Profile, Project


# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile(photo="image.jpeg",bio="this is to test if it can work",contact = "0798164370")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
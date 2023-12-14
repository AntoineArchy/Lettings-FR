from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.test import TestCase

from oc_lettings_site.profiles.models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        User.objects.create(username="john_doe", password="password123")

    def test_profile_str(self):
        user = User.objects.get(username="john_doe")
        profile = Profile.objects.create(user=user, favorite_city="Lille")
        self.assertEqual(str(profile), "john_doe")

    def test_profile_validation_ok(self):
        user = User.objects.get(username="john_doe")
        profile = Profile(user=user, favorite_city="Lille")
        self.assertEqual(profile.full_clean(), None)

    def test_profile_validation_ko(self):
        profile = Profile(user=None, favorite_city="")
        with self.assertRaises(ValidationError):
            profile.full_clean()

    def test_profile_not_exist(self):
        with self.assertRaises(ObjectDoesNotExist):
            Profile.objects.get(user=42)

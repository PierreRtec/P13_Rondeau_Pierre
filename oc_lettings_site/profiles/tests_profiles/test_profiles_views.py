from assertpy import assert_that
from django.contrib.auth.models import User
from django.test import Client, TestCase

from profiles.models import Profile

client = Client()


class TestProfilesViews(TestCase):
    def setUp(self):
        user = User.objects.create(username="Michel")
        Profile.objects.create(user=user, favorite_city="Barcelona")

    def test_get_profile_favorite_city(self):
        # init
        favorite_city = Profile.objects.get(favorite_city="Barcelona")

        # expectation
        expected_result = favorite_city

        # method call
        result = Profile.objects.get(favorite_city="Barcelona")

        # assertions
        assert_that(result).is_equal_to(expected_result)

    def test_get_profile_user(self):
        # init
        user = User.objects.get(username="Michel")
        profile_user = Profile.objects.get(user=user)

        # expectation
        expected_result = profile_user

        # method call
        result = Profile.objects.get(user=user)

        # assertions
        assert_that(result).is_equal_to(expected_result)

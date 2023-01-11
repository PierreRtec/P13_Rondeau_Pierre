from assertpy import assert_that
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from lettings.models import Address, Letting
from profiles.models import Profile

client = Client()


class TestOcLettingsSiteViews(TestCase):
    def setUp(self):
        user = User.objects.create(username="Michel")
        address = Address.objects.create(
            number=157,
            street="Argyle Avenue",
            city="East Meadow",
            state="NY",
            zip_code=11547,
            country_iso_code="USA",
        )
        Profile.objects.create(user=user, favorite_city="Barcelona")
        Letting.objects.create(title="Underground Hygge", address=address)

    def test_get_success_url_index(self):
        # expectation
        expected_status_code = 200

        # method call
        response = client.get("")

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

    def test_get_success_url_profiles(self):
        # expectation
        expected_status_code = 200
        profile_url = reverse("profiles_index")

        # method call
        response = self.client.get(profile_url)

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

    def test_get_success_url_profiles_username(self):
        # expectation
        expected_status_code = 200
        user = User.objects.get(username="Michel")
        profile_url = reverse("profiles_index")

        # method call
        response = self.client.get(profile_url, args=user.username)

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

    def test_get_success_url_lettings(self):
        # expectation
        expected_status_code = 200
        letting_url = reverse("lettings_index")

        # method call
        response = self.client.get(letting_url)

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

    def test_get_success_url_lettings_id(self):
        # expectation
        expected_status_code = 200
        letting_url = reverse("lettings_index")

        # method call
        response = self.client.get(letting_url, args=1)

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

    def test_get_success_url_admin_login(self):
        # expectation
        expected_status_code = 200

        # method call
        response = client.get("/admin/login/")

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

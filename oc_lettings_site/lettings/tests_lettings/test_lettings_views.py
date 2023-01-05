from assertpy import assert_that
from django.test import TestCase, Client


client = Client()


class TestLettingsViews(TestCase):
    def test_get_success_url(self):
        # expectation
        expected_status_code = 200

        # method call
        response = client.get("/lettings")

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

    def test_get_lettings_by_id(self):
        # expectation
        expected_status_code = 200

        # method call
        response = client.get("/lettings", letting_id=1)

        # assertions
        assert_that(response.status_code).is_equal_to(expected_status_code)

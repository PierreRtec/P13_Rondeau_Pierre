from assertpy import assert_that
from django.contrib.auth.models import User
from django.test import Client, TestCase
from ..models import Address, Letting

client = Client()


class TestLettingsViews(TestCase):
    def setUp(self):
        User.objects.create(username="Claude")
        address = Address.objects.create(
            number=485,
            street="Marge Boulevard",
            city="North Way",
            state="NY",
            zip_code=22548,
            country_iso_code="USA",
        )
        Letting.objects.create(title="Fabulous Brydg", address=address)

    def test_get_address(self):
        # init
        address = Address.objects.get()

        # expectation
        expected_result = address

        # method call
        result = Address.objects.get()

        # assertions
        assert_that(result).is_equal_to(expected_result)

    def test_get_address_street(self):
        # init
        address = Address.objects.get(street="Marge Boulevard")

        # expectation
        expected_result = address

        # method call
        result = Address.objects.get(street="Marge Boulevard")

        # assertions
        assert_that(result).is_equal_to(expected_result)

    def test_letting(self):
        # init
        letting = Letting.objects.get()

        # expectation
        expected_result = letting

        # method call
        result = Letting.objects.get()

        # assertions
        assert_that(result).is_equal_to(expected_result)

from django.test import TestCase
from rest_framework.test import APIClient
from django.core.mail import EmailMessage
from ..models import Contact
from ..signals import populate_table_data, on_delete_contact


class SignalsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_populate_data(self):
        ans = populate_table_data(Contact)
        self.assertEqual(ans, True)

    def test_send_mail(self):
        class TestInstance(object):
            email = 'foo@foo.com'

        out = on_delete_contact(None, instance=TestInstance)

        class TestInstance(object):
            email = 'foo_test_yes@foo.com'

        out_g = on_delete_contact(None, instance=TestInstance)

        self.assertEqual(out, False)
        self.assertEqual(out_g.__class__, EmailMessage)
        self.assertEqual(out_g.body, f'The email {TestInstance.email} was deleted successefully! Thanks!')

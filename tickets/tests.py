from django.test import TestCase
from .models import Ticket

# Create your tests here.
class TicketTest(TestCase):
    """
    Here we'll define the tests that we'll 
    run against our Ticket models
    """
    def test_str(self):
        test_name = Ticket(title='A bug')
        self.assertEqual(str(test_name), 'A bug')
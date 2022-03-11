from django.test import TestCase
from django.contrib.auth.models import User
from .models import Detail

class StaffTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()

        #create user's details
        test_details = Detail.objects.create(
            name='testuser1', regNO=4567, post="Sales manager", department="Sales Department", period=10, salary=50000
        )
        test_details.save()

    def test_details_content(self):
        detail = Detail.objects.get(id=1)
        name = f'{detail.name}'
        regNO = f'{detail.regNO}'
        post = f'{detail.post}'
        department  = f'{detail.department}'
        period = f'{detail.period}'
        salary = f'{detail.salary}'
        self.assertEqual(name, 'testuser1')
        self.assertEqual(regNO, '4567')
        self.assertEqual(post, "Sales manager")
        self.assertEqual(department, "Sales Department")
        self.assertEqual(period, '10')
        self.assertEqual(salary, '50000.0')
from django.test import TestCase

from django.contrib.auth.models import User

from ..forms import NewAccountForm


class TestNewAccountForm(TestCase):
    def test_success_password_procession(self):
        min_data = {
            'username': 'name',
            'password': '1',
        }
        form = NewAccountForm(data=min_data)
        form.is_valid()
        form.save()
        user = User.objects.get(username=min_data['username'])
        self.assertTrue(user.check_password("1"))

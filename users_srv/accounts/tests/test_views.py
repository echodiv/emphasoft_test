from django.test import TestCase

from django.contrib.auth.models import User


class TestUserListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Создаём 15 пользователей для выполнения тестов"""
        number_of_accounts = 15
        for account_num in range(number_of_accounts):
            user = User.objects.create_user(
                username='test%s' % account_num,
                password=str(account_num),
            )
            user.save()

    def setUp(self):
        """
        Авторизация пользователем
        """
        response = self.client.post(
            '/login/', {'username': 'test1', 'password': '1'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class TestAccountManageView(TestCase):
    pass


class TestDeleteAccountView(TestCase):
    pass


class TestUpdateAccountView(TestCase):
    pass


class TestAccountDetailView(TestCase):
    pass
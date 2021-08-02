from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse


class MainTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Создаём пользователя для выполнения тестов"""
        user = User.objects.create_user(
            username='test1', password="1",
        )
        user.save()

    def setUp(self):
        """
        Авторизация пользователем
        """
        response = self.client.post(
            '/login/', {'username': 'test1', 'password': '1'}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


class TestUserListView(MainTestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('accounts:accounts_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('accounts:accounts_list'))
        self.assertTemplateUsed(resp, 'accounts/list.html')


class TestAccountManageView(MainTestCase):
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('accounts:account_manage'))
        self.assertTemplateUsed(resp, 'accounts/create.html')

from django.test import Client, TestCase
from django.urls import resolve

from .views import index


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_url_resolves_to_home_page_view(self):
        resolve_match = resolve('/')
        self.assertEqual(resolve_match.func, index)

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')
        content: str = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(content.startswith('<!DOCTYPE html>'))
        self.assertTrue(content.endswith('</html>'))

    def test_(self):
        pass

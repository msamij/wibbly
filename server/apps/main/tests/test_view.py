from django.test import Client, TestCase


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/')

    def test_home_page_returns_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'index.html')

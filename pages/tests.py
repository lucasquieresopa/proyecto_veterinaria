from django.test import TestCase
from django.test import SimpleTestCase

class SimpleTests(TestCase):
    def test_home_page_status_code(self):       
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)         #200 es el codigo que referencia a que la página existe

    # def test_profile_page_status_code(self):
    #     response = self.client.get('/profile/')
    #     self.assertEqual(response.status_code, 200)


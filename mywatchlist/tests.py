from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class TestViews(TestCase):
    def test_show_watchlist(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_watchlist'))
        self.assertEquals(response.status_code,200)

    def test_show_xml(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEquals(response.status_code,200)
        
    def test_show_json(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEquals(response.status_code,200)

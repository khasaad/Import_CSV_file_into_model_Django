from django.test import Client
from django.urls import reverse

client = Client()

def test_url(self):
    # Generate the URL using the view name passed as a parameter
    response = self.client.get(reverse('/' + str(self.path_name) + '/')) # path_name: norms
    self.assertEqual(response.status_code, 200) # Check if the URL is correct
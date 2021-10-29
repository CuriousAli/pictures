from django.urls import reverse
from rest_framework.test import APITestCase



class PicApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('picture-list')
        print(url)
        response = self.client.get(url)
        print(response.data)


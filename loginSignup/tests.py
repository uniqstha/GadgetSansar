from django.test import Client, SimpleTestCase, TestCase
# from product.models import Item
from app.views import home
from django.contrib.auth.models import User
from django.urls import reverse, resolve

# Create your tests here.
class TestViews(TestCase):

    def test_home(self):

        #create new user with username and password
        user = User.objects.create(username='test12')
        user.set_password('1234')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test12", password="1234")
        response = client.get(reverse(home))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage.html")
from urllib import response
from django.test import Client, SimpleTestCase, TestCase
from adminpage.views import add, updatepage
from django.test import Client 
# from product.models import Item
from app.views import home
from django.contrib.auth.models import User
from django.urls import reverse, resolve

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
      self.user = User.objects.create(username='testuser')
      self.user.set_password('12345')
      self.user.save()
      self.c = Client()
      self.c.login(username='testuser', password='12345')
      self.admin_user = User.objects.create_superuser('admin1', 'admin@example.com', 'adminpass')
      self.admin = Client()
      self.admin.login(username='admin1', password='adminpass')

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
        

    def test_product_create_url(self):
        url = reverse("add")
        self.assertEquals(resolve(url).func,add)
    
    def test_product_update_url(self):
          self.assertEqual(
          reverse('updatepage' ,kwargs={'id': "1"}),
          '/admin/updatepage/1')
    
    def test_product_delete_url(self):
        self.assertEqual(
        reverse('delete' ,kwargs={'id': "1"}),
        '/admin/delete/1')

    def test_phone_detail_url(self):
        self.assertEqual(
        reverse('phonedetails' ,kwargs={'id': "1"}),
        '/products/phone/productdetails/1')
    def test_audio_detail_url(self):
        self.assertEqual(
        reverse('audiodetails' ,kwargs={'id': "1"}),
        '/products/audio/productdetails/1')
    def test_fitness_detail_url(self):
        self.assertEqual(
        reverse('fitnessdetails' ,kwargs={'id': "1"}),
        '/products/fitness/productdetails/1')
    def test_power_detail_url(self):
        self.assertEqual(
        reverse('powerdetails' ,kwargs={'id': "1"}),
        '/products/power/productdetails/1')

    def test_add_product(self):
        response = self.c.post(reverse('add'),{
        "id":"12",
        "name": "test_product",
        "productBrand": "test",
        "price": "123",
        "productCategory": "phone",
        "description":"description",
        "techSpec":"techspec",
        "whatsIncluded": "nothing",
        "image": "default.jpg",
        "img1": "default.jpg",
        "img2": "default.jpg",
      }) 
        self.assertEqual(response.status_code, 302)


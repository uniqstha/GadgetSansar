from django.test import TestCase
from django.urls import resolve, reverse
from adminpage.views import adminlogin,adminhome, order
from django.contrib.auth import get_user_model
# Create your tests here.
User = get_user_model
class TestViews(TestCase):

    def test_admin_home_Render12(self):
        url = reverse(adminhome)
        response= self.assertEquals(resolve(url).func,adminhome)
        self.assertTemplateUsed(response, "admin/adminhome.html")
    
    
    def test_order(self):
        url = reverse(order)
        response= self.assertEquals(resolve(url).func,order)
        self.assertTemplateUsed(response, "admin/userorder.html")
  
      
    def test_admin_login(self):
        url = reverse(adminlogin)
        response= self.assertEquals(resolve(url).func,adminlogin)
        self.assertTemplateUsed(response, 'admin/adminlogin.html')

           




    
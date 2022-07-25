from django.test import TestCase
from django.urls import resolve, reverse
from adminpage.views import adminlogin,adminhome, order
from django.contrib.auth import get_user_model

from products.views import audio, audioDetails, fitness, fitnessDetails, phone, phoneDetails, power, powerDetails
# Create your tests here.
User = get_user_model
class TestViews(TestCase):

    def test_product_phone(self):
        url = reverse(phone)
        response= self.assertEquals(resolve(url).func,phone)
        self.assertTemplateUsed(response, "phones.html")
    
    
    def test_product_audio(self):
        url = reverse(audio)
        response= self.assertEquals(resolve(url).func,audio)
        self.assertTemplateUsed(response, "audio.html")

    
    def test_product_power(self):
        url = reverse(power)
        response= self.assertEquals(resolve(url).func,power)
        self.assertTemplateUsed(response, "power.html")

    
    def test_product_fitness(self):
        url = reverse(fitness)
        response= self.assertEquals(resolve(url).func,fitness)
        self.assertTemplateUsed(response, "fitness.html")
    
    def test_product_phonedetails(self):
        url = reverse(phoneDetails,kwargs={'id': "1"})
        response= self.assertEquals(resolve(url).func,phoneDetails)
        self.assertTemplateUsed(response, "productDetails/phoneDetails.html")
    
    
    def test_product_audiodtails(self):
        url = reverse(audioDetails, kwargs={'id': "1"})
        response= self.assertEquals(resolve(url).func,audioDetails)
        self.assertTemplateUsed(response, "productDetails/audioDetails.html")

    
    def test_product_powerdetails(self):
        url = reverse(powerDetails, kwargs={'id': "1"})
        response= self.assertEquals(resolve(url).func,powerDetails)
        self.assertTemplateUsed(response, "productDetails/powerDetails.html")

    
    def test_product_fitnessdetails(self):
        url = reverse(fitnessDetails,kwargs={'id': "1"})
        response= self.assertEquals(resolve(url).func,fitnessDetails)
        self.assertTemplateUsed(response, "productDetails/fitnessDetails.html")
    


           




    
from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    productBrand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    productCategory = models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    techSpec=models.CharField(max_length=255)
    whatsIncluded=models.CharField(max_length=255)

    image=models.FileField(upload_to="static/images/products",default="default.jpg")
    img1=models.FileField(upload_to="static/images/products",default="default.jpg")
    img2=models.FileField(upload_to="static/images/products",default="default.jpg")


    class Meta:
        db_table="Product"
        verbose_name_plural = 'product'
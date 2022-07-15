from django.contrib import admin
from products.models import Product
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=('id','productBrand','name','price','description', 'techSpec','whatsIncluded', 'image','img1','img2')
admin.site.register(Product,ProductsAdmin)

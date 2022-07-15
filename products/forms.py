from dataclasses import field
from django import forms
from products.models import Product


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
from django.forms import ModelForm
from .models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('brand', 'title', 'description', 'price', 'created_at', 'image')

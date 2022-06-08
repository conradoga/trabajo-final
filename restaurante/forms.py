from django import forms
from restaurante.models import hamburguesas
class Product_form(forms.ModelForm):
    class Meta:
        model = hamburguesas
        fields = '__all__'
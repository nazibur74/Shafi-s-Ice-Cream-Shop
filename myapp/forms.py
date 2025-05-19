from django import forms
from myapp.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'quantity']

from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    price = forms.CharField(label="price", max_length=100)
    qty = forms.CharField(label="qty", max_length=100)
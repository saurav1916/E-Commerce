from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES=(("S","Stripe"),("P","Paytm"))


class CheckoutForm(forms.Form):
    house_address=forms.CharField(max_length=50,widget=forms.TextInput(attrs=
    {'placeholder':'#1234','class':"form-control"}))
    area_address=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
    'placeholder':'Street No.','class':"form-control" }))
    mobile_number=forms.IntegerField(widget=forms.TextInput(attrs={
        'class':"form-control"
    }))
    country=CountryField(blank_label="Select Country").formfield(widget=CountrySelectWidget(attrs=
    {'class':"custom-select d-block w-100"}))
    zipcode=forms.IntegerField(widget=forms.TextInput(attrs={'class':"form-control" }))
    payment=forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)
   




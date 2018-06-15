from django import forms
from DefectsNotification.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

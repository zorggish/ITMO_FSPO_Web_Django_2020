from django import forms
from .models import Car_owner

class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = Car_owner
        fields = {
            "firstName",
            "secondName",
            "birthday",
        }
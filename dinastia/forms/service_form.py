from django import forms
from ..models.services import Services


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['code', 'name', 'price', 'conditional_unit_of_labor',
                  'external', 'category']

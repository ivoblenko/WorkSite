from django import forms
from ..models.patients import Patients


class ServicesRenderedForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patients.objects.all(), initial=0, empty_label=None)
    services = forms.JSONField()

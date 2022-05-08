from django import forms
from ..models.inspection_templates import InspectionsTemplates


class InspectionTemplateForm(forms.ModelForm):

    class Meta:
        model = InspectionsTemplates
        fields = ['template_name', 'complaints', 'anamnesis', 'diagnosis', 'additionally']

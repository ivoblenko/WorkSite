from django.shortcuts import render, get_object_or_404
from ..models.inspection_templates import InspectionsTemplates
from ..models.inspections import Inspections
from django.http import HttpResponse
from django.views import generic


def menu(request):
    return render(request, 'inspections/menu.html')


def new(request, inspection_type_id):
    template = get_object_or_404(InspectionsTemplates, departemnts_id=inspection_type_id)
    return render(request, 'inspections/inspection.html', {
        'inspection_type': inspection_type_id,
        'template': template
    })


class CreateView(generic.CreateView):
    model = Inspections
    fields = Inspections.get_fields()
    template_name = 'inspections/inspection.html'

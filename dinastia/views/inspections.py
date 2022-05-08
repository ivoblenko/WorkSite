from django.shortcuts import render, get_object_or_404, redirect
from ..models.inspection_templates import InspectionsTemplates
from ..models.inspections import Inspections
from ..models.patients import Patients
from ..forms.inspection_form import InspectionForm
from django.views.generic.edit import UpdateView
from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.models import Permission


def menu(request):
    return render(request, 'inspections/menu.html')


def inspection_new(request, department_id):
    if request.method == "POST":
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save(commit=False)
            patient = Patients(surname=request.POST.get('surname'), name=request.POST.get('name'),
                               patronymic=request.POST.get('patronymic'))
            patient.save()
            inspection.patient = patient
            inspection.save()
            return redirect('inspection_update', pk=inspection.pk)
    else:
        form = InspectionForm()
        template = InspectionsTemplates.objects.get(department=department_id)
        form.initial = {
            'complaints': template.complaints,
            'anamnesis': template.anamnesis,
            'diagnosis': template.diagnosis,
            'additionally': template.additionally
        }

    return render(request, 'inspections/inspection.html', {'form': form})


def inspection_update(request, inspection_id):
    if request.method == "POST":
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save()
            patient = Patients(surname=inspection.surname, name=inspection.name, patronymic=inspection.patronymic)
            patient.save()
            inspection.patient = patient.id
            inspection.save()
            return redirect('inspection_update', pk=inspection.pk)
    else:
        instance = get_object_or_404(Inspections, id=inspection_id)
        form = InspectionForm(instance=instance)
    return render(request, 'inspections/inspection.html', {'form': form})


class InspectionUpdate(UpdateView):
    model = Inspections
    fields = ['patient', 'complaints', 'anamnesis', 'diagnosis', 'additionally']
    template_name = 'inspections/inspection.html'


def inspection_templates(request):
    templates = InspectionsTemplates.objects.all()
    return render(request, 'inspections/inspection_templates.html', {'templates': templates})


class InspectionTemplateUpdate(UpdateView):
    model = InspectionsTemplates
    fields = ['template_name', 'complaints', 'anamnesis', 'diagnosis', 'additionally']
    template_name = 'inspections/inspection_template_update.html'


def inspection_table(request):
    return render(request, 'inspections/table.html')


class PermissionAjaxDatatableView(AjaxDatatableView):

    model = Inspections
    title = 'Осмотры'
    initial_order = [["date", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'patient', 'visible': False, },
        {'name': 'staff', 'visible': True, },
        {'name': 'date', 'visible': True, },
        # {'name': 'app_label', 'foreign_field': 'content_type__app_label', 'visible': True, },
        # {'name': 'model', 'foreign_field': 'content_type__model', 'visible': True, },
    ]

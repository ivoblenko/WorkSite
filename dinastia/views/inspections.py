from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.forms import inlineformset_factory

from ..models.inspection_templates import InspectionsTemplates
from ..models.inspections import Inspections
from ..models.patients import Patients
from ..forms.inspection_form import InspectionForm
from django.views.generic.edit import UpdateView
from ajax_datatable.views import AjaxDatatableView


def menu(request):
    return render(request, 'inspections/menu.html')


def inspection_new(request, department_id):
    if request.method == "POST":
        form = InspectionForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            inspection = form.save(commit=False)
            patient = Patients(
                surname=request.POST.get('surname'),
                name=request.POST.get('name'),
                patronymic=request.POST.get('patronymic'),
                phone=(request.POST.get('phone') != '') if request.POST.get('phone') else None,
                dob=(request.POST.get('dob') != '') if request.POST.get('dob') else None)
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

#TODO: переписать способ сохранения, поискать как сохранять связные модели
def inspection_update(request, pk):
    if request.method == "POST":
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = get_object_or_404(Inspections, pk=pk)

            data_from_form = form.save(commit=False)
            inspection.complaints = data_from_form.complaints
            inspection.anamnesis = data_from_form.anamnesis
            inspection.additionally = data_from_form.additionally
            inspection.diagnosis = data_from_form.diagnosis
            inspection.patient.surname = request.POST.get('surname')
            inspection.patient.name = request.POST.get('name')
            inspection.patient.patronymic = request.POST.get('patronymic')
            inspection.patient.dob = (request.POST.get('dob') != '') if request.POST.get('dob') else None
            inspection.patient.phone = (request.POST.get('phone') != '') if request.POST.get('phone') else None
            inspection.save(force_update=True)
            inspection.patient.save(force_update=True)

            return redirect('inspection_update', pk=inspection.pk)
    else:
        inspection = get_object_or_404(Inspections, id=pk)

        form = InspectionForm(data={
            'surname': inspection.patient.surname,
            'name': inspection.patient.name,
            'patronymic': inspection.patient.patronymic,
            'dob': inspection.patient.dob,
            'phone': inspection.patient.phone,
            'complaints': inspection.complaints,
            'anamnesis': inspection.anamnesis,
            'additionally': inspection.additionally,
            'diagnosis': inspection.diagnosis
        })

    return render(request, 'inspections/inspection.html', {'form': form})


# class InspectionUpdateView(UpdateView):
#     model = Inspections
#     fields = ['patient', 'complaints', 'anamnesis', 'diagnosis', 'additionally']
#     template_name = 'inspections/inspection.html'
#     child_fields = '__all__'
#
#     # def get_context_data(self, **kwargs):
#     #     context = super(InspectionUpdateView, self).get_context_data(**kwargs)
#     #     context['surname'] =


def inspection_templates(request):
    templates = InspectionsTemplates.objects.all()
    return render(request, 'inspections/inspection_templates.html', {'templates': templates})


class InspectionTemplateUpdateView(UpdateView):
    model = InspectionsTemplates
    fields = ['template_name', 'complaints', 'anamnesis', 'diagnosis', 'additionally']
    template_name = 'inspections/inspection_template_update.html'


def inspection_table(request):
    return render(request, 'inspections/table.html')


class InspectionAjaxDatatableView(AjaxDatatableView):
    model = Inspections
    title = 'Осмотры'
    initial_order = [["date", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = False
    show_column_filters = False

    column_defs = [
        {'name': 'patient', 'visible': True, },
        {'name': 'staff', 'visible': True, },
        {'name': 'date', 'visible': True, },
    ]

    def customize_row(self, row, obj):
        row['patient'] = '<a href="%s">%s</a>' % (
            reverse('inspection_update', args=(obj.id,)),
            obj.patient
        )
        return

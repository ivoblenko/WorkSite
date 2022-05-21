from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models.inspection_templates import InspectionsTemplates
from ..models.inspections import Inspections
from ..models.patients import Patients
from ..models.files import Files
from ..models.departments import Departments
from ..forms.inspection_form import InspectionForm
from django.views.generic.edit import UpdateView
from ajax_datatable.views import AjaxDatatableView
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from WorkSite.settings import DATE_INPUT_FORMATS


@login_required
def menu(request):
    user = request.user
    print(user.groups.all())
    if user.groups.filter(name='admin').exists():
        departments = Departments.objects.all()
    else:
        departments = [{'id': user.staff.department.id,
                        'name': user.staff.department.name
                        }]
    return render(request, 'inspections/menu.html', {'departments': departments})


@login_required
def inspection_new(request, department_id):
    error = ""
    if request.method == "POST":
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            inspection = form.save(commit=False)
            inspection.staff = request.user.staff
            inspection.save()

            for file in request.FILES.getlist('files'):
                new_file = Files(
                    patient=inspection.patient,
                    file=file,
                    name='Test'
                )
                new_file.save()

            request.session['print'] = 1 if request.POST.get('print') != None else 0

            return redirect('inspection_update', pk=inspection.pk)
        else:
            error = "Неверно заполненная форма!"
    else:
        form = InspectionForm()
        template = InspectionsTemplates.objects.get(department=department_id)
        form.initial = {
            'complaints': template.complaints,
            'anamnesis': template.anamnesis,
            'diagnosis': template.diagnosis,
            'additionally': template.additionally
        }

    return render(request, 'inspections/inspection.html', {'form': form,
                                                           'error': error})


# TODO: переписать способ сохранения, поискать как сохранять связные модели
@login_required
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
            inspection.staff = request.user.staff
            inspection.save(force_update=True)

            for file in request.FILES.getlist('files'):
                new_file = Files(
                    patient=inspection.patient,
                    file=file,
                    name='Test'
                )
                new_file.save()

            request.session['print'] = 1 if request.POST.get('print') != None else 0

            return redirect('inspection_update', pk=inspection.pk)
    else:
        inspection = get_object_or_404(Inspections, id=pk)
        files_list = Files.objects.filter(patient=inspection.patient)

        form = InspectionForm(data={
            'patient': inspection.patient,
            'complaints': inspection.complaints,
            'anamnesis': inspection.anamnesis,
            'additionally': inspection.additionally,
            'diagnosis': inspection.diagnosis
        })

    return render(request, 'inspections/inspection.html',
                  {'form': form, 'pk': pk,
                   'print': request.session.get('print', False),
                   'files_list': files_list,
                   })


@login_required
def print_inspection(request, pk):
    inspection = get_object_or_404(Inspections, pk=pk)
    return render(request, 'inspections/print/1.html',
                  {'inspection': inspection})


@login_required
def file_delete(request):
    file = get_object_or_404(Files, pk=request.GET.get('file_id'))
    file.file.delete()
    file.delete()
    return JsonResponse({'data': 1}, status=200)


@login_required
def inspection_templates(request):
    templates = InspectionsTemplates.objects.all()
    return render(request, 'inspections/inspection_templates.html', {'templates': templates})


class InspectionTemplateUpdateView(UpdateView):
    model = InspectionsTemplates
    fields = ['template_name', 'complaints', 'anamnesis', 'diagnosis', 'additionally']
    template_name = 'inspections/inspection_template_update.html'


@login_required
def inspection_table(request):
    return render(request, 'inspections/table.html')


# TODO:доделать поиск для даты и связных полей
class InspectionAjaxDatatableView(AjaxDatatableView):
    model = Inspections
    title = 'Осмотры'
    initial_order = [["date", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'Все']]

    column_defs = [
        {'name': 'patient', 'visible': True},
        {'name': 'staff', 'visible': True, 'foreign_field': 'staff__surname'},
        {'name': 'date', 'visible': True, 'searchable': True, 'lookup_field': '__icontains'},
        {'name': 'Печать', 'visible': True, 'searchable': False}
    ]

    def customize_row(self, row, obj):
        row['patient'] = '<a href="%s">%s</a>' % (
            reverse('inspection_update', args=(obj.id,)),
            obj.patient
        )
        row['staff'] = str(obj.staff)
        row['Печать'] = '<a onclick="window.open(\'%s\')">Печать</a>' % (
            reverse('inspection_print', args=(obj.id,))
        )
        return

# TODO: переписать по образцу
# class FileFieldFormView(FormView):
#     form_class = FileFieldForm
#     template_name = 'upload.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

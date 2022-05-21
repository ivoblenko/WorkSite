from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from ..models.patients import Patients
from ..models.files import Files
from ajax_datatable.views import AjaxDatatableView
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from ..forms.patient_form import PatientForm


@login_required
def patient_new(request):
    error = ""
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()

            for file in request.FILES.getlist('files'):
                new_file = Files(
                    patient=patient,
                    file=file,
                    name='Test'
                )
                new_file.save()

            return redirect('patient_update', pk=patient.pk)
        else:
            error = "Неверно заполненная форма!"
    else:
        form = PatientForm()

    return render(request, 'patients/patient.html', {'form': form,
                                                     'error': error})


@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patients, id=pk)
    files_list = Files.objects.filter(patient=patient)
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.id = pk
            patient.save(force_update=True)

            for file in request.FILES.getlist('files'):
                new_file = Files(
                    patient=patient,
                    file=file,
                    name='Test'
                )
                new_file.save()

            return redirect('patient_update', pk=pk)
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients/patient.html',
                  {'form': form,
                   'pk': pk,
                   'files_list': files_list,
                   })


@login_required
def file_delete(request):
    file = get_object_or_404(Files, pk=request.GET.get('file_id'))
    file.file.delete()
    file.delete()
    return JsonResponse({'data': 1}, status=200)


@login_required
def patient_table(request):
    return render(request, 'patients/table.html')


class PatientAjaxDatatableView(AjaxDatatableView):
    model = Patients
    title = 'Зарегистрированные пациенты'
    initial_order = [["surname", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'Все']]

    column_defs = [
        {'name': 'surname', 'visible': True},
        {'name': 'name', 'visible': True, },
        {'name': 'patronymic', 'visible': True, },
        {'name': 'phone', 'visible': True, },
        {'name': 'dob', 'visible': True, }
    ]

    def customize_row(self, row, obj):
        row['surname'] = '<a href="%s">%s</a>' % (
            reverse('patient_update', args=(obj.id,)),
            obj.surname
        )
        if obj.phone != None:
            row['phone'] = "+7 (%s) %s %s %s" % (
                str(obj.phone)[:3],
                str(obj.phone)[3:6],
                str(obj.phone)[6:8],
                str(obj.phone)[8:],

            )
        return

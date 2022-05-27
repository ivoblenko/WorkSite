from django.urls import path
from .views import login
from .views import menu
from .views import inspections, patients

urlpatterns = [
    path('login', login.login, name='login'),
    path('logout', login.logout, name='logout'),

    path('', menu.menu, name='main_menu'),
    path('inspections/menu', inspections.menu, name='inspections_menu'),

    path('inspections/new/<int:department_id>', inspections.inspection_new, name='inspection_new'),
    path('inspections/update/<int:pk>', inspections.inspection_update, name='inspection_update'),

    path('inspections/templates', inspections.inspection_templates, name='inspection_templates'),
    path('inspections/templates/update/<int:pk>', inspections.InspectionTemplateUpdateView.as_view(),
         name='inspection_template_update'),

    path('inspections/table', inspections.inspection_table, name='inspections_table'),
    path('inspections/table/get', inspections.InspectionAjaxDatatableView.as_view(), name='inspections_table_get'),

    path('inspection/print/<int:pk>', inspections.print_inspection, name='inspection_print'),

    path('patient/new', patients.patient_new, name='patient_new'),
    path('patient/update/<int:pk>', patients.patient_update, name='patient_update'),
    path('patient/table', patients.patient_table, name='patient_table'),
    path('patient/table/get', patients.PatientAjaxDatatableView.as_view(), name='patient_table_get'),
    path('patient/get_patient_files', patients.get_patient_files, name='get_patient_files'),
    path('patient/delete_patient_files', patients.delete_patient_files, name='delete_patient_files'),
]

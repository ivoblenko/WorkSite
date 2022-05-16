from django.urls import path
from .views import login
from .views import menu
from .views import inspections
from django.contrib.auth.views import LoginView, LogoutView
from django import forms

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
    path('inspection/file_delete', inspections.file_delete, name='inspection_file_delete')
]

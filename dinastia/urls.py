from django.urls import path

from .views import menu
from .views import inspections

urlpatterns = [
    path('', menu.menu, name='main_menu'),
    path('inspections/menu', inspections.menu, name='inspections_menu'),
    path('inspections/new/<int:department_id>', inspections.inspection_new, name='inspection_new'),
    path('inspections/update/<int:pk>', inspections.InspectionUpdate.as_view(), name='inspection_update'),
    path('inspections/templates', inspections.inspection_templates, name='inspection_templates'),
    path('inspections/templates/update/<int:pk>', inspections.InspectionTemplateUpdate.as_view(), name='inspection_template_update'),
    path('inspections/table', inspections.inspection_table, name='inspections_table'),
    path('inspections/table/get', inspections.InspectionAjaxDatatableView.as_view(), name='inspections_table_get'),
]
from django.urls import path

from .views import menu
from .views import inspections

urlpatterns = [
    path('', menu.menu, name='main_menu'),
    path('inspections/menu', inspections.menu, name='inspections_menu'),
    path('inspections/new/<int:inspection_type_id>', inspections.CreateView.as_view(), name='inspection')
]
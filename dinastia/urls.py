from django.urls import path
from .views import login, finance
from .views import menu
from .views import inspections, patients
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import WorkSite.settings as settings

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

    path('finance', finance.menu, name='finance_menu'),

    path('finance/guides', finance.guides_menu, name='finance_guides_menu'),

    path('finance/guides/services', finance.services_table, name='services'),
    path('finance/guides/service/new', finance.ServiceCreateView.as_view(), name='service_new'),
    path('finance/guides/service/update/<int:pk>', finance.update_service, name='service_update'),
    path('finance/guides/services/get', finance.ServicesAjaxDatatableView.as_view(), name='get_services_table'),

    path('finance/guides/service-categories', finance.service_categories_table, name='service_categories'),
    path('finance/guides/service-category/new', finance.ServiceCategoryCreateView.as_view(),
         name='service_category_new'),
    path('finance/guides/service-category/update/<int:pk>', finance.ServiceCategoryUpdateView.as_view(),
         name='service_category_update'),
    path('finance/guides/service-category/get', finance.ServiceCategoriesAjaxDatatableView.as_view(),
         name='get_service_categories_table'),

    path('finance/guides/cash-receipts', finance.cash_receipts_table, name='cash_receipts'),
    path('finance/guides/cash-receipt/new', finance.CashReceiptCreateView.as_view(), name='cash_receipt_new'),
    path('finance/guides/cash-receipt/update/<int:pk>', finance.CashReceiptUpdateView.as_view(),
         name='cash_receipt_update'),
    path('finance/guides/cash-receipt/get', finance.CashReceiptsAjaxDatatableView.as_view(),
         name='get_cash_receipts_table'),

    path('finance/guides/expenses', finance.expenses_table, name='expenses'),
    path('finance/guides/expense/new', finance.ExpenseCreateView.as_view(), name='expense_new'),
    path('finance/guides/expense/update/<int:pk>', finance.ExpenseUpdateView.as_view(),
         name='expense_update'),
    path('finance/guides/expense/get', finance.ExpensesAjaxDatatableView.as_view(),
         name='get_expenses_table'),

    path('finance/new_services_rendered', finance.new_services_rendered, name='new_services_rendered'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

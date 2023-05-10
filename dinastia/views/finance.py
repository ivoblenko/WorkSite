from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views.generic.edit import UpdateView, CreateView
from ajax_datatable.views import AjaxDatatableView
from django.contrib.auth.decorators import login_required

from ..forms.service_rendered_form import ServicesRenderedForm
from ..models.service_categories import ServiceCategories
from ..models.services import Services

from ..models.cash_receipts import CashReceipts
from ..models.expenses import Expenses

from ..forms.service_form import ServiceForm


@login_required
def menu(request):
    return render(request, 'finance/menu.html', {})


@login_required
def guides_menu(request):
    return render(request, 'finance/guides/menu.html', {})


class ServiceCreateView(CreateView):
    model = Services
    fields = '__all__'
    template_name = 'finance/guides/services/service.html'


@login_required
def update_service(request, pk):
    if request.method == "POST":
        old_service = get_object_or_404(Services, pk=pk)
        form = ServiceForm(request.POST, initial=model_to_dict(old_service))

        if form.is_valid() and form.has_changed():
            old_service.active = False

            new_service = form.save(commit=False)
            new_service.active = True
            new_service.save()
            old_service.save()

            return redirect('service_update', pk=new_service.pk)
    else:
        service = get_object_or_404(Services, id=pk)
        form = ServiceForm(instance=service)

    return render(request, 'finance/guides/services/service.html',
                  {'form': form,
                   'pk': pk,
                   })


@login_required
def services_table(request):
    return render(request, 'finance/guides/services/services.html',
                  {
                      'row_grouping': True,
                      'group_column': 0,
                      'columns_count': 6,
                  })


class ServicesAjaxDatatableView(AjaxDatatableView):
    model = Services
    title = 'Услуги'
    initial_order = [["category", "asc"], ["code", "asc"]]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'Все']]

    column_defs = [
        {'name': 'category', 'visible': False, 'searchable': True, 'orderable': True},
        {'name': 'code', 'visible': True, 'searchable': True, 'orderable': True},
        {'name': 'name', 'visible': True, 'searchable': True, 'orderable': False},
        {'name': 'price', 'visible': True, 'searchable': True, 'orderable': False},
        {'name': 'conditional_unit_of_labor', 'visible': True, 'searchable': True, 'orderable': False},
        {'name': 'external', 'visible': True, 'searchable': True, 'boolean': True, 'orderable': False},
        {'name': 'active', 'visible': False, 'searchable': False, 'boolean': True, 'orderable': False},
        {'name': 'Редактировать', 'visible': True, 'searchable': False, 'orderable': False}
    ]

    def customize_row(self, row, obj):
        row['Редактировать'] = '<a onclick="window.open(\'%s\')">Редактировать</a>' % (
            reverse('service_update', args=(obj.id,))
        )
        return

    def filter_queryset(self, params, qs):
        qs = self.filter_queryset_by_date_range(params.get('date_from', None), params.get('date_to', None), qs)

        if 'search_value' in params:
            qs = self.filter_queryset_all_columns(params['search_value'], qs)

        for column_link in params['column_links']:
            if column_link.searchable and column_link.search_value:
                qs = self.filter_queryset_by_column(column_link.name, column_link.search_value, qs)

        qs = self.filter_queryset_by_column('active', 1, qs)

        return qs


class ServiceCategoryCreateView(CreateView):
    model = ServiceCategories
    fields = '__all__'
    template_name = 'finance/guides/service_categories/service_category.html'


class ServiceCategoryUpdateView(UpdateView):
    model = ServiceCategories
    fields = '__all__'
    template_name = 'finance/guides/service_categories/service_category.html'


@login_required
def service_categories_table(request):
    return render(request, 'finance/guides/service_categories/service_categories.html')


class ServiceCategoriesAjaxDatatableView(AjaxDatatableView):
    model = ServiceCategories
    title = 'Категори услуг'
    initial_order = [["name", "asc"]]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'Все']]

    column_defs = [
        {'name': 'name', 'visible': True, 'searchable': True},
        {'name': 'Редактировать', 'visible': True, 'searchable': False}
    ]

    def customize_row(self, row, obj):
        row['Редактировать'] = '<a onclick="window.open(\'%s\')">Редактировать</a>' % (
            reverse('service_category_update', args=(obj.id,))
        )
        return


class CashReceiptCreateView(CreateView):
    model = CashReceipts
    fields = '__all__'
    template_name = 'finance/guides/cash_receipts/cash_receipt.html'


class CashReceiptUpdateView(UpdateView):
    model = CashReceipts
    fields = '__all__'
    template_name = 'finance/guides/cash_receipts/cash_receipt.html'


@login_required
def cash_receipts_table(request):
    return render(request, 'finance/guides/cash_receipts/cash_receipts.html')


class CashReceiptsAjaxDatatableView(AjaxDatatableView):
    model = CashReceipts
    title = 'Денежные поступления'
    initial_order = [["name", "asc"]]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'Все']]

    column_defs = [
        {'name': 'name', 'visible': True, 'searchable': True},
        {'name': 'Редактировать', 'visible': True, 'searchable': False}
    ]

    def customize_row(self, row, obj):
        row['Редактировать'] = '<a onclick="window.open(\'%s\')">Редактировать</a>' % (
            reverse('cash_receipt_update', args=(obj.id,))
        )
        return


class ExpenseCreateView(CreateView):
    model = Expenses
    fields = '__all__'
    template_name = 'finance/guides/expenses/expense.html'


class ExpenseUpdateView(UpdateView):
    model = Expenses
    fields = '__all__'
    template_name = 'finance/guides/expenses/expense.html'


@login_required
def expenses_table(request):
    return render(request, 'finance/guides/expenses/expenses.html')


class ExpensesAjaxDatatableView(AjaxDatatableView):
    model = Expenses
    title = 'Расходы'
    initial_order = [["name", "asc"]]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'Все']]

    column_defs = [
        {'name': 'name', 'visible': True, 'searchable': True},
        {'name': 'Редактировать', 'visible': True, 'searchable': False}
    ]

    def customize_row(self, row, obj):
        row['Редактировать'] = '<a onclick="window.open(\'%s\')">Редактировать</a>' % (
            reverse('expense_update', args=(obj.id,))
        )
        return


@login_required
def new_services_rendered(request):
    if request.method == "POST":
        old_service = get_object_or_404(Services, pk=pk)
        form = ServiceForm(request.POST, initial=model_to_dict(old_service))

        if form.is_valid() and form.has_changed():
            old_service.active = False

            new_service = form.save(commit=False)
            new_service.active = True
            new_service.save()
            old_service.save()

            return redirect('service_update', pk=new_service.pk)
    else:
        form = ServicesRenderedForm()

    return render(request, 'finance/guides/services/service.html',
                  {'form': form})

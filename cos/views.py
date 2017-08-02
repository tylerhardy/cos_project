from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Asset
from .forms import AssetForm, AssetCreateForm
from datetime import datetime

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['assets'] = Asset.objects.all()
        return context


class AboutView(generic.TemplateView):
    template_name = 'about.html'

from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import AssetListFilter
class AssetListView(LoginRequiredMixin, FilterView):
    model = Asset
    filterset_class = AssetListFilter
    template_name = 'cos/asset_list.html'
    paginate_by = 4

class AssetDetailView(LoginRequiredMixin, generic.DetailView):
    model = Asset
    template_name = 'cos/asset_detail.html'

class AssetCreate(LoginRequiredMixin, CreateView):
    form_class = AssetCreateForm
    model = Asset
    template_name = 'cos/asset_form.html'
    # fields = ['asset_tag', 'computer_name', 'hardware_serial_number', 'vendor_serial_number', 'equipment_role', 'equipment_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes']

    def get_context_data(self, *args, **kwargs):
        context = super(AssetCreate, self).get_context_data(**kwargs)
        context['hide'] = True
        return context

    # def get_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     form = super(AssetCreate, self).get_form(form_class)
    #     form.fields['purchase_date'].widget = form.dateInput()
    #     return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        asset_create_form = form.save(commit=False)
        asset_create_form.added_by = self.request.user
        asset_create_form = form.save()
        return super(AssetCreate, self).form_valid(form)

class AssetUpdate(LoginRequiredMixin, UpdateView):
    model = Asset
    template_name = 'cos/asset_form.html'
    fields = ['asset_tag', 'computer_name', 'hardware_serial_number', 'vendor_serial_number', 'equipment_role', 'equipment_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes']

    def form_valid(self, form):
        asset_update_form = form.save(commit=False)
        asset_update_form.modified_by = self.request.user
        asset_update_form.modified_date = datetime.now()
        asset_update_form = form.save()
        return super(AssetUpdate, self).form_valid(form)

class AssetDuplicate(LoginRequiredMixin, UpdateView):
    # https://stackoverflow.com/a/33001010
    model = Asset
    template_name = 'cos/asset_form.html'
    success_url = reverse_lazy('assets')
    fields = ['asset_tag', 'computer_name', 'hardware_serial_number', 'vendor_serial_number', 'equipment_role', 'equipment_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes']

    def get_context_data(self, *args, **kwargs):
        context = super(AssetDuplicate, self).get_context_data(**kwargs)
        context['duplicate'] = True
        return context

    def post(self, request, pk, *args, **kwargs):
        new_asset = get_object_or_404(Asset, pk = pk)
        new_asset.pk = None
        form =  AssetForm(request.POST or None, instance = new_asset)

        if form.is_valid():
            new_asset.added_by = request.user
            form.save()
            return redirect('assets')

        context = {"form": form,}
        return render(request, "cos/asset_form.html", context)


class AssetDelete(LoginRequiredMixin, DeleteView):
    model = Asset
    success_url = reverse_lazy('assets')

import csv
from django.http import HttpResponse

def export_assets_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assets.csv"'

    writer = csv.writer(response)
    writer.writerow(['asset_tag', 'computer_name', 'hardware_serial_number', 'vendor_serial_number', 'equipment_role', 'equipment_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes', 'added_date', 'added_by', 'modified_date', 'modified_by'])

    assets = Asset.objects.all().values_list('asset_tag', 'computer_name', 'hardware_serial_number', 'vendor_serial_number', 'equipment_role', 'equipment_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes', 'added_date', 'added_by', 'modified_date', 'modified_by')
    for asset in assets:
        writer.writerow(asset)

    return response
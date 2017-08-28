from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django_filters.views import FilterView

from .filters import AssetListFilter
from .models import Asset
from .forms import AssetForm

from datetime import datetime

# Create your views here.
class AssetListView(LoginRequiredMixin, FilterView):
    """
    FilterView inplace of generic ListView, provides search functionality
    using django_filters.
    Modified [get_context_data] to provide pagination to default or search
    results.
    """
    model = Asset
    template_name = 'inventory_app/asset_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AssetListView, self).get_context_data(**kwargs)
        list_assets =  Asset.objects.order_by('pk').all()
        asset_filter = AssetListFilter(self.request.GET, queryset=list_assets)
        paginator = Paginator(asset_filter.qs, 10)
        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            items = paginator.page(1)
        except(EmptyPage, InvalidPage):
            # If page is out of range (e.g. 9999), deliver last page of results.
            items = paginator.page(paginator.num_pages)
        context['items'] = items
        return context


class AssetDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Generic DetailView to provide information of the asset.
    """
    model = Asset
    template_name = 'inventory_app/asset_detail.html'


from django.forms.models import modelform_factory
class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)


class AssetCreate(LoginRequiredMixin, ModelFormWidgetMixin, CreateView):
    """
    Generic CreateView for adding assets to the database.
    Modified [get_context_data] to hide links in asset_form.html.
    Modified [form_valid] to log who created the asset.
    """
    model = Asset
    template_name = 'inventory_app/asset_form.html'
    fields = [
        'asset_tag', 'hardware_name', 'hardware_serial_number',
        'vendor_serial_number', 'hardware_role', 'hardware_condition',
        'inventory_system', 'user', 'curator', 'department', 'org_code',
        'location', 'vendor', 'requisition_number', 'purchase_order',
        'purchase_date', 'purchase_cost', 'funded_by', 'eligible_upgrade', 'hardware_type',
        'hardware_make', 'hardware_model', 'network_connection', 'ip_address',
        'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram',
        'graphics', 'os', 'os_arch', 'active_directory',
        'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder',
        'notes'
        ]
    widgets = {
        'purchase_date': forms.DateInput(attrs={'type': 'date'}),
    }

    def get_context_data(self, *args, **kwargs):
        context = super(AssetCreate, self).get_context_data(**kwargs)
        context['hide'] = True
        return context

    def form_valid(self, form):
        asset_create_form = form.save(commit=False)
        asset_create_form.added_by = self.request.user
        return super(AssetCreate, self).form_valid(form)


class AssetUpdate(LoginRequiredMixin, ModelFormWidgetMixin, UpdateView):
    """
    Generic UpdateView for Editing existing assets.
    Modified [form_valid] to log who modified the asset.
    """
    model = Asset
    template_name = 'inventory_app/asset_form.html'
    fields = [
        'asset_tag', 'hardware_name', 'hardware_serial_number',
        'vendor_serial_number', 'hardware_role', 'hardware_condition',
        'inventory_system', 'user', 'curator', 'department', 'org_code',
        'location', 'vendor', 'requisition_number', 'purchase_order',
        'purchase_date', 'purchase_cost', 'funded_by', 'eligible_upgrade', 'hardware_type',
        'hardware_make', 'hardware_model', 'network_connection', 'ip_address',
        'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram',
        'graphics', 'os', 'os_arch', 'active_directory',
        'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder',
        'notes'
        ]
    widgets = {
        'purchase_date': forms.DateInput(attrs={'type': 'date'}),
    }

    def get_context_data(self, *args, **kwargs):
        context = super(AssetUpdate, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        asset_update_form = form.save(commit=False)
        asset_update_form.modified_by = self.request.user
        asset_update_form.modified_date = datetime.now()
        return super(AssetUpdate, self).form_valid(form)

class AssetAudit(LoginRequiredMixin, ModelFormWidgetMixin, UpdateView):
    """
    Generic UpdateView for Auditing Assets
    Modified [form_valid] to log who audited the asset.
    """
    model = Asset
    template_name = 'inventory_app/asset_form.html'
    fields = [
        'notes','audited_by','audited_date'
        ]
    widgets = {
        'audited_date': forms.DateInput(attrs={'type': 'date'}),
        # 'audited_date': forms.DateInput(attrs={'type': 'date', 'readonly':'readonly'}),
    }
    def get_context_data(self, *args, **kwargs):
        context = super(AssetAudit, self).get_context_data(**kwargs)
        context['audit'] = True
        return context

    def form_valid(self, form):
        asset_update_form = form.save(commit=False)
        asset_update_form.audited_by = self.request.user
        asset_update_form.audited_date = datetime.now()
        return super(AssetAudit, self).form_valid(form)

class AssetDuplicate(LoginRequiredMixin, UpdateView):
    """
    Generic UpdateView for duplicating already created assets.
    Modified [get_context_data] to add 'duplicate' variable to context.
    Modified [post] remove the source asset pk from the duplicated asset.
    """
    form_class = AssetForm
    model = Asset
    template_name = 'inventory_app/asset_form.html'
    # success_url = reverse_lazy('assets')

    def get_context_data(self, *args, **kwargs):
        context = super(AssetDuplicate, self).get_context_data(**kwargs)
        context['duplicate'] = True
        return context

    def post(self, request, pk, *args, **kwargs):
        new_asset = get_object_or_404(Asset, pk = pk)
        new_asset.pk = None
        new_asset.added_by = None
        new_asset.added_date = None
        new_asset.modified_by = None
        new_asset.modified_date = None
        new_asset.audited_by = None
        new_asset.audited_date = None
        form = AssetForm(request.POST or None, instance = new_asset)
        if form.is_valid():
            new_asset.added_by = request.user
            form.save()
            # return redirect('assets')
            return self.form_valid(form)
        context = {"form": form,}
        return render(request, "inventory_app/asset_form.html", context)

class AssetDelete(LoginRequiredMixin, DeleteView):
    """
    Generic DeleteView to delete assets from database.
    """
    model = Asset
    success_url = reverse_lazy('assets')

import csv
from django.http import HttpResponse

def export_assets_csv(request):
    """
    Function view to allow exporting of database to csv file.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assets.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'asset_tag', 'hardware_name', 'hardware_serial_number',
        'vendor_serial_number', 'hardware_role', 'hardware_condition',
        'inventory_system', 'user', 'curator', 'department', 'org_code',
        'location', 'vendor', 'requisition_number', 'purchase_order',
        'purchase_date', 'purchase_cost', 'funded_by', 'eligible_upgrade', 'hardware_type',
        'hardware_make', 'hardware_model', 'network_connection', 'ip_address',
        'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram',
        'graphics', 'os', 'os_arch', 'active_directory',
        'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder',
        'notes', 'added_date', 'added_by', 'modified_date', 'modified_by'
        ])
    assets = Asset.objects.all().values_list(
        'asset_tag', 'hardware_name', 'hardware_serial_number',
        'vendor_serial_number', 'hardware_role', 'hardware_condition',
        'inventory_system', 'user', 'curator', 'department', 'org_code',
        'location', 'vendor', 'requisition_number', 'purchase_order',
        'purchase_date', 'purchase_cost', 'funded_by', 'eligible_upgrade', 'hardware_type',
        'hardware_make', 'hardware_model', 'network_connection', 'ip_address',
        'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram',
        'graphics', 'os', 'os_arch', 'active_directory',
        'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder',
        'notes', 'added_date', 'added_by', 'modified_date', 'modified_by'
    )
    for asset in assets:
        writer.writerow(asset)

    return response
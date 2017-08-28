from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django_filters.views import FilterView

from .filters import DirectoryListFilter
from .models import Directory
from .forms import DirectoryForm
from datetime import datetime

# Create your views here.
class DirectoryListView(LoginRequiredMixin, FilterView):
    model = Directory
    template_name = 'directory_app/directory_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DirectoryListView, self).get_context_data(**kwargs)
        list_contacts =  Directory.objects.order_by('department','pk').filter(status__icontains='current')
        contact_filter = DirectoryListFilter(self.request.GET, queryset=list_contacts)
        paginator = Paginator(contact_filter.qs, 10)
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


from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def last_visit_view(request, *args, **kwargs):
    last_visit_obj = Directory.objects.filter(pk=kwargs['pk'])
    if last_visit_obj:
        last_visit_obj = last_visit_obj[0]
        last_visit_obj.last_visit = datetime.now()
        last_visit_obj.save()
    return HttpResponseRedirect(reverse('directory_list'))

class DirectoryDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Generic DetailView to provide information of the asset.
    """
    model = Directory
    template_name = 'directory_app/directory_detail.html'


from django.forms.models import modelform_factory
class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)


from django import forms
class DirectoryCreateView(LoginRequiredMixin, ModelFormWidgetMixin, CreateView):
    """
    Generic CreateView for adding contacts to the database.
    Modified [get_context_data] to hide links in directory_form.html.
    Modified [form_valid] to log who created the contact.
    """
    model = Directory
    template_name = 'directory_app/directory_form.html'
    fields = [
        'status', 'first_name','last_name','email_address','department','job_title',
        'phone_number_1', 'phone_number_2', 'location', 'website', 'notes',
        'last_visit'
    ]
    widgets = {
        'last_visit': forms.DateInput(attrs={'type': 'date'}),
    }

    def get_context_data(self, *args, **kwargs):
        context = super(DirectoryCreateView, self).get_context_data(**kwargs)
        context['new'] = True
        return context

    def form_valid(self, form):
        asset_create_form = form.save(commit=False)
        asset_create_form.added_by = self.request.user
        return super(DirectoryCreateView, self).form_valid(form)

class DirectoryUpdateView(LoginRequiredMixin, ModelFormWidgetMixin, UpdateView):
    """
    """
    model = Directory
    template_name = 'directory_app/directory_form.html'
    fields = [
        'status', 'first_name','last_name','email_address','department','job_title',
        'phone_number_1', 'phone_number_2', 'location', 'website', 'notes',
        'last_visit'
    ]
    widgets = {
        'last_visit': forms.DateInput(attrs={'type': 'date'}),
    }
    def get_context_data(self, *args, **kwargs):
        context = super(DirectoryUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        asset_update_form = form.save(commit=False)
        asset_update_form.modified_by = self.request.user
        asset_update_form.modified_date = datetime.now()
        return super(DirectoryUpdateView, self).form_valid(form)

class DirectoryDuplicateView(LoginRequiredMixin, UpdateView):
    form_class = DirectoryForm
    model = Directory
    template_name = 'directory_app/directory_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DirectoryDuplicateView, self).get_context_data(**kwargs)
        context['duplicate'] = True
        return context

    def post(self, request, pk, *args, **kwargs):
        new_contact = get_object_or_404(Directory, pk = pk)
        new_contact.pk = None
        new_contact.added_by = None
        new_contact.added_date = None
        new_contact.modified_by = None
        new_contact.modified_date = None
        new_contact.last_visit = None
        form = DirectoryForm(request.POST or None, instance = new_contact)
        if form.is_valid():
            new_contact.added_by = request.user
            form.save()
            return self.form_valid(form)
        context = {"form": form,}
        return render(request, "inventory_app/asset_form.html", context)

class DirectoryDeleteView(LoginRequiredMixin, DeleteView):
    """
    Generic DeleteView to delete assets from database.
    """
    model = Directory
    success_url = reverse_lazy('directory_list')


import csv
from django.http import HttpResponse

def export_directory_csv(request):
    """
    Function view to allow exporting of the directory table to csv file.
    """
    response = HttpResponse(content_type='text/csv')
    today = datetime.now().date()
    response['Content-Disposition'] = 'attachment; filename="cos_directory_{0}.csv"'.format(today)

    writer = csv.writer(response)
    writer.writerow([
        'status', 'first_name','last_name','email_address','department','job_title',
        'phone_number_1', 'phone_number_2', 'location', 'website', 'notes',
        'last_visit', 'added_date', 'added_by', 'modified_date', 'modified_by'
        ])
    contacts = Directory.objects.all().values_list(
        'status', 'first_name','last_name','email_address','department','job_title',
        'phone_number_1', 'phone_number_2', 'location', 'website', 'notes',
        'last_visit', 'added_date', 'added_by', 'modified_date', 'modified_by'
    )
    for contact in contacts:
        writer.writerow(contact)

    return response
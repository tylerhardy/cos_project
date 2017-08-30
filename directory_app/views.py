from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django_filters.views import FilterView

from .filters import DirectoryListFilter
from .models import Directory
# from .models import Directory, Picture
from .forms import DirectoryForm
# from .forms import DirectoryForm, PictureForm
from datetime import datetime

# Create your views here.
class DirectoryListView(LoginRequiredMixin, FilterView):
    model = Directory
    template_name = 'directory_app/directory_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DirectoryListView, self).get_context_data(**kwargs)
        list_contacts =  Directory.objects.order_by('department','last_name').filter(status__icontains='current')
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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    # return render_to_response('directory_list.html', context, context_instance = RequestContext(request))
    # return HttpResponseRedirect(reverse('directory_list'))


class DirectoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Directory
    template_name = 'directory_app/directory_detail.html'


class DirectoryCreateView(LoginRequiredMixin, CreateView):
    model = Directory
    template_name = 'directory_app/directory_form.html'
    form_class = DirectoryForm

    def get_context_data(self, *args, **kwargs):
        context = super(DirectoryCreateView, self).get_context_data(**kwargs)
        context['new'] = True
        return context

    def form_valid(self, form):
        directory_create_form = form.save(commit=False)
        directory_create_form.added_by = self.request.user
        return super(DirectoryCreateView, self).form_valid(form)

class DirectoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Directory
    template_name = 'directory_app/directory_form.html'
    form_class = DirectoryForm

    def get_context_data(self, *args, **kwargs):
        context = super(DirectoryUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        asset_update_form = form.save(commit=False)
        asset_update_form.modified_by = self.request.user
        asset_update_form.modified_date = datetime.now()
        return super(DirectoryUpdateView, self).form_valid(form)


class DirectoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Directory
    success_url = reverse_lazy('directory_list')


import csv
from django.http import HttpResponse
def export_directory_csv(request):
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

# def model_form_upload(request):
#     if request.method == 'POST':
#         form = PictureForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('directory_list')
#     else:
#         form = PictureForm()
#     documents = Picture.objects.all()
#     return render(request, 'directory_app/directory_upload.html', {
#         'form': form,
#         'documents': documents,
#     })
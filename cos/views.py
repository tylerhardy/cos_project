from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from .forms import AssetForm, ComputerObjectForm
from .models import Asset, ComputerObject

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['assets'] = Asset.objects.all()
        context['computer_objects'] = ComputerObject.objects.all()
        return context

from django.contrib.auth.mixins import LoginRequiredMixin

class AssetListView(LoginRequiredMixin, generic.ListView):
    model = Asset
    template_name = 'cos/asset_list.html'
    paginate_by = 10
    
class AssetDetailView(LoginRequiredMixin, generic.DetailView):
    model = Asset
    template_name = 'cos/asset_detail.html'

class AssetCreate(LoginRequiredMixin, CreateView):
    model = Asset
    fields = '__all__'

    # def form_valid(self, form, *args, **kwargs):
    #     if self.form_class.is_valid():
    #         # change user stuff
    #         pass
    #     self.form_class.save()

class AssetUpdate(LoginRequiredMixin, UpdateView):
    model = Asset
    fields = '__all__'

from django.contrib.auth.mixins import PermissionRequiredMixin

class AssetDelete(PermissionRequiredMixin, DeleteView):
    model = Asset
    success_url = reverse_lazy('assets')
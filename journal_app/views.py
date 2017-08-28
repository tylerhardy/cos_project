from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django_filters.views import FilterView

from .filters import JournalListFilter
from datetime import datetime


class JournalListView(LoginRequiredMixin, FilterView):
    model = Post
    template_name = "journal_app/post_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(JournalListView, self).get_context_data(**kwargs)
        list_post =  Post.objects.order_by('pk').all()
        post_filter = JournalListFilter(self.request.GET, queryset=list_post)
        paginator = Paginator(post_filter.qs, 10)
        page = self.request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            post_list = paginator.page(1)
        except(EmptyPage, InvalidPage):
            # If page is out of range (e.g. 9999), deliver last page of results.
            post_list = paginator.page(paginator.num_pages)
        context['post_list'] = post_list
        return context

class JournalDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Generic DetailView to provide information of the asset.
    """
    model = Post
    template_name = 'journal_app/post_detail.html'


class JournalDelete(LoginRequiredMixin, DeleteView):
    """
    Generic DeleteView to delete journal_app entries from database.
    """
    model = Post
    success_url = reverse_lazy('post_list')


class JournalCreateView(LoginRequiredMixin, CreateView):
    """
    Generic CreateView for adding assets to the database.
    Modified [get_context_data] to hide links in asset_form.html.
    Modified [form_valid] to log who created the asset.
    """
    model = Post
    template_name = 'journal_app/post_form.html'
    fields = ['title', 'text',]

    def get_context_data(self, *args, **kwargs):
        context = super(JournalCreateView, self).get_context_data(**kwargs)
        context['new'] = True
        return context

    def form_valid(self, form):
        asset_update_form = form.save(commit=False)
        asset_update_form.author = self.request.user
        asset_update_form.published_date = datetime.now()
        return super(JournalCreateView, self).form_valid(form)

class JournalUpdateView(LoginRequiredMixin, UpdateView):
    """
    Generic UpdateView for Editing existing assets.
    Modified [form_valid] to log who modified the asset.
    """
    model = Post
    template_name = 'journal_app/post_form.html'
    fields = ['title', 'text',]

    def get_context_data(self, *args, **kwargs):
        context = super(JournalUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context
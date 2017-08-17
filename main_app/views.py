from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django import forms

from datetime import datetime

# Create your views here.
class HomeView(generic.TemplateView):
    """
    Homepage for the inventory system, shows how many assets are in the system
    """
    template_name = 'main_app/index.html'

class AboutView(generic.TemplateView):
    """
    About page for the inventory systm, provides basic information on using
    the inventory system
    """
    template_name = 'main_app/about.html'
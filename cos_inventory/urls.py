from django.conf.urls import url

from . import views

urlpatterns = [
    # Class TemplateView with modified [get_context_data] function
    url(r'^$', views.HomeView.as_view(), name='index'),

    # Class TemplateView
    url(r'^about/$', views.AboutView.as_view(), name='about'),

    # Class FilterView with modified [get_context_data] function
    url(r'^assets/$', views.AssetListView.as_view(), name='assets'),

    # Class DetailView
    url(r'^asset/(?P<pk>\d+)$', views.AssetDetailView.as_view(), name='asset-detail'),

    # Class CreateView with modified [get_context_data] and [form_valid] functions
    url(r'^asset/create/$', views.AssetCreate.as_view(), name='asset_create'),

    # Class UpdateView with modified [form_valid] function
    url(r'^asset/(?P<pk>\d+)/edit/$', views.AssetUpdate.as_view(), name='asset_update'),

    # Class UpdateView with modified [form_valid] function
    url(r'^asset/(?P<pk>\d+)/audit/$', views.AssetAudit.as_view(), name='asset_audit'),

    # Class UpdateView with modified [get_context_data] and [post] functions
    url(r'^asset/(?P<pk>\d+)/duplicate/$', views.AssetDuplicate.as_view(), name='asset_duplicate'),

    # Class DeleteView
    url(r'^asset/(?P<pk>\d+)/delete/$', views.AssetDelete.as_view(), name='asset_delete'),

    # Function View
    url(r'^asset/export/csv/$', views.export_assets_csv, name='export_assets_csv'),
]
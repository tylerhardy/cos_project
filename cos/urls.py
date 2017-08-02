from django.conf.urls import url
from django_filters.views import FilterView
from .filters import AssetListFilter

from . import views

# app_name = 'cos'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    # url(r'^assets/$', FilterView.as_view(filterset_class=AssetListFilter, template_name='cos/asset_list.html'), name='assets'),
    url(r'^assets/$', views.AssetListView.as_view(), name='assets'),
    # url(r'^assets/$', views.AssetListView.as_view(), name='assets'),
    url(r'^asset/(?P<pk>\d+)$', views.AssetDetailView.as_view(), name='asset-detail'),
]

urlpatterns += [
    url(r'^asset/create/$', views.AssetCreate.as_view(), name='asset_create'),
    url(r'^asset/(?P<pk>\d+)/edit/$', views.AssetUpdate.as_view(), name='asset_update'),
    url(r'^asset/(?P<pk>\d+)/delete/$', views.AssetDelete.as_view(), name='asset_delete'),
    url(r'^asset/(?P<pk>\d+)/duplicate/$', views.AssetDuplicate.as_view(), name='asset_duplicate'),
    url(r'^asset/export/csv/$', views.export_assets_csv, name='export_assets_csv'),
]
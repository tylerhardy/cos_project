from django.conf.urls import url

from . import views

# app_name = 'cos'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^assets/$', views.AssetListView.as_view(), name='assets'),
    url(r'^asset/(?P<pk>\d+)$', views.AssetDetailView.as_view(), name='asset-detail'),
]

urlpatterns += [
    url(r'^asset/create/$', views.AssetCreate.as_view(), name='asset_create'),
    url(r'^asset/(?P<pk>\d+)/edit/$', views.AssetUpdate.as_view(), name='asset_update'),
    url(r'^asset/(?P<pk>\d+)/delete/$', views.AssetDelete.as_view(), name='asset_delete'),
]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^assets/$', views.AssetListView.as_view(), name='assets'),
    url(r'^asset/(?P<pk>\d+)$', views.AssetDetailView.as_view(), name='asset_detail'),
    url(r'^asset/new/$', views.AssetCreate.as_view(), name='asset_new'),
    url(r'^asset/(?P<pk>\d+)/edit/$', views.AssetUpdate.as_view(), name='asset_update'),
    url(r'^asset/(?P<pk>\d+)/audit/$', views.AssetAudit.as_view(), name='asset_audit'),
    url(r'^asset/(?P<pk>\d+)/duplicate/$', views.AssetDuplicate.as_view(), name='asset_duplicate'),
    url(r'^asset/(?P<pk>\d+)/delete/$', views.AssetDelete.as_view(), name='asset_delete'),
    url(r'^asset/export/csv/$', views.export_assets_csv, name='export_assets_csv'),
]
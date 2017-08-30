from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contacts/$', views.DirectoryListView.as_view(), name='directory_list'),
    url(r'^contact/(?P<pk>\d+)$', views.DirectoryDetailView.as_view(), name='contact_detail'),
    url(r'^contact/new/$', views.DirectoryCreateView.as_view(), name='contact_new'),
    url(r'^contact/(?P<pk>\d+)/edit/$', views.DirectoryUpdateView.as_view(), name='contact_update'),
    url(r'^contact/(?P<pk>\d+)/date/$', views.last_visit_view, name='date_update'),
    url(r'^contact/(?P<pk>\d+)/delete/$', views.DirectoryDeleteView.as_view(), name='contact_delete'),
    url(r'^contact/export/csv/$', views.export_directory_csv, name='export_directory_csv'),
    # url(r'^contact/uploads/form/$', views.model_form_upload, name='model_form_upload'),

]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/$', views.JournalListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.JournalDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.JournalCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.JournalUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.JournalDelete.as_view(), name='post_delete'),

]
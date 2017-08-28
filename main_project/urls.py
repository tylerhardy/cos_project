from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]

urlpatterns += [
    url(r'^inventory/', include('inventory_app.urls')),
    url(r'^directory/', include('directory_app.urls')),
    url(r'^journal/', include('journal_app.urls')),
    url(r'^wiki/', include('wiki_app.urls'))
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]
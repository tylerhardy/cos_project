from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Asset

# Register your models here.
admin.site.register(Asset, SimpleHistoryAdmin)

from django.contrib import admin

from .models import Asset, ComputerObject

# Register your models here.
admin.site.register(Asset)
admin.site.register(ComputerObject)
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Post

# Register your models here.
admin.site.register(Post, SimpleHistoryAdmin)

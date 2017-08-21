from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')
    history = HistoricalRecords()
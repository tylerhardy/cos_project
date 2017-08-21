from django.db import models
from django.utils import timezone
from django.urls import reverse
from simple_history.models import HistoricalRecords


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @property
    def brief_text(self):
        if len(self.text) <= 50:
            return self.text[0:(len(self.text))]
        else:
            return self.text[:50] + "..."
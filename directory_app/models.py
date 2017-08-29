from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
import datetime
from django.utils import timezone
from simple_history.models import HistoricalRecords
import os

# def get_upload_path(instance, filename):
#     return os.path.join('faculty_pictures', filename)

# class Picture(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     image = models.FileField(upload_to=get_upload_path, blank=True, null=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     history = HistoricalRecords()

#     def __str__(self):
#         return self.description

# College of Science Departments
department_choice = (
    ('dean',"Dean's office"),
    ('bot','Botany'),
    ('chem','Chemistry'),
    ('geo','Geosciences'),
    ('math','Mathematics'),
    ('dev_math','Developmental Math'),
    ('micro','Microbiology'),
    ('phys','Physics'),
    ('planet_phys','Planetarium'),
    ('zoo','Zoology'),
    ('csme','Center of Science and Math Education'),
    ('other','Other or Unknown Department'),
    ('None','No department')
)

status_choice = (
    ('current', 'Current'),
    ('not_current', 'Not Employed'),
    ('moved', 'Moved Departments'),
    ('retired', 'Retired'),
    ('sabbatical', 'Sabbatical'),
    ('adjunct', 'Adjunct'),
    ('temporary', 'Temporary'),
)

# Create your models here.
class Directory(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    department = models.CharField("Department", max_length=200, blank=True, choices=department_choice)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    ext_regex = RegexValidator(regex=r'^\+?1?\d{4}$', message="Phone extension must be entered in the format: '+9999'. Exactly 4 digits allowed.")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number_1 = models.CharField("Office Ext.", max_length=200, validators=[ext_regex], blank=True) # validators should be a list
    phone_number_2 = models.CharField("Cell number", max_length=200, validators=[phone_regex], blank=True) # validators should be a list
    location = models.CharField(max_length=200)
    website = models.URLField(max_length=200, blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True)
    status = models.CharField(default='current', max_length=200, choices=status_choice)
    last_visit = models.DateTimeField(blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='directory_added_user', blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name='directory_modified_user', blank=True, null=True)
    # image = models.ForeignKey(Picture, blank=True, null=True)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('contact_detail', args=[str(self.id)])

    def __str__(self):
        """
        Return a string representation of the model.
        """
        return self.email_address

    @property
    def visit_past_due(self):
        d_14 = timezone.make_aware(datetime.datetime.today()) - datetime.timedelta(days=14)
        d_28 = timezone.make_aware(datetime.datetime.today()) - datetime.timedelta(days=28)
        if self.last_visit is None:
            return 'no_visit_performed'
        elif self.last_visit > d_14:
            return 'visit_good'
        elif (self.last_visit < d_14) and (self.last_visit > d_28):
            return 'visit_old'
        elif self.last_visit < d_28:
            return 'need_visit'
        else:
            return 'error'

    @property
    def current_status(self):
        if self.status is None:
            return 'no_status'
        else:
            return self.status
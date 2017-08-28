import csv,sys,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, 'cos_project')
print(BASE_DIR)
project_dir = os.path.join(BASE_DIR, "main_project")
print(project_dir)
csv_location = os.path.join(BASE_DIR, "gCOS_faculty.csv")
print(csv_location)


sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'main_project.settings.dev'

import django

django.setup()

from directory_app.models import Directory

data = csv.reader(open(csv_location),delimiter=",")

for row in data:
    if row[0] != 'first_name':
        contacts = Directory()
        contacts.first_name = row[0]
        contacts.last_name = row[1]
        contacts.email_address = row[2]
        contacts.department = row[3]
        contacts.job_title = row[4]
        contacts.phone_number_1 = row[5]
        contacts.phone_number_2 = row[6]
        contacts.location = row[7]
        contacts.website = row[8]
        contacts.notes = row[9]
        contacts.status = row[10]
        contacts.save()
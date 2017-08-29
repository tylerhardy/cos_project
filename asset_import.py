import csv,sys,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, 'cos_project')
print(BASE_DIR)
project_dir = os.path.join(BASE_DIR, "main_project")
print(project_dir)
csv_location = os.path.join(BASE_DIR, "cos_asset.csv")
print(csv_location)


sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'main_project.settings.dev'
# os.environ['DJANGO_SETTINGS_MODULE'] = 'main_project.settings.prod'

import django

django.setup()

from inventory_app.models import Asset

data = csv.reader(open(csv_location),delimiter=",")

for row in data:
    if row[0] != 'first_name':
        assets = Asset()
        assets.asset_tag = row[0]
        assets.hardware_name = row[1]
        assets.hardware_serial_number = row[2]
        assets.vendor_serial_number = row[3]
        assets.hardware_role = row[4]
        assets.hardware_condition = row[5]
        assets.inventory_system = row[6]
        assets.user = row[7]
        assets.curator = row[8]
        assets.department = row[9]
        assets.org_code = row[10]
        assets.location = row[11]
        assets.vendor = row[12]
        assets.requisition_number = row[13]
        assets.purchase_order = row[14]
        assets.purchase_date = row[15]
        assets.purchase_cost = row[16]
        assets.funded_by = row[17]
        assets.eligible_upgrade = row[18]
        assets.hardware_type = row[19]
        assets.hardware_make = row[20]
        assets.hardware_model = row[21]
        assets.network_connection = row[22]
        assets.ip_address = row[23]
        assets.mac_wired = row[24]
        assets.mac_wireless = row[25]
        assets.processor = row[26]
        assets.harddrive = row[27]
        assets.ram = row[28]
        assets.graphics = row[29]
        assets.os = row[30]
        assets.os_arch = row[31]
        assets.active_directory = row[32]
        assets.organizational_unit = row[33]
        assets.sccm = row[34]
        assets.jamf = row[35]
        assets.scep = row[36]
        assets.identity_finder = row[37]
        assets.notes = row[38]
        assets.save()
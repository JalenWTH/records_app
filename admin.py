from django.contrib import admin

from app_3.models import records

for i in range(len(records)):
    admin.site.register(records[i])
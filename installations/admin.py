from django.contrib import admin
from .models import Location, Installation, Report
# Register your models here.

admin.site.register(Location)
admin.site.register(Installation)
admin.site.register(Report)
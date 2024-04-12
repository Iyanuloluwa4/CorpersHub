from django.contrib import admin
from .models import Connect

class ConnectModelAdmin (admin.ModelAdmin):
    ordering = ('date_uploaded', 'client')
    search_fields = ('client', 'job_title')


admin.site.register(Connect, ConnectModelAdmin)

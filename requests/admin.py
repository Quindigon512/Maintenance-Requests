from django.contrib import admin
from .models import Request, Tenant

admin.site.register(Request)
admin.site.register(Tenant)

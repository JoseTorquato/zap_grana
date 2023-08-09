from django.contrib import admin
from .models import Integration

class IntegrationAdmin(admin.ModelAdmin):
    list_display = ('platform', 'status', 'user_uuid')
    search_fields = ('platform', 'status', 'user_uuid')
    fields = ('platform', 'status', 'call_count')


admin.site.register(Integration, IntegrationAdmin)

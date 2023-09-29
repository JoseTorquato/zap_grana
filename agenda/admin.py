from django.contrib import admin

from .models import WeddingRegistration


class WeddingRegistrationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'event_date', 'number_of_guests', 'status'] 
    list_filter = ['event_date']


admin.site.register(WeddingRegistration, WeddingRegistrationAdmin)

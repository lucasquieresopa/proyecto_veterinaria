from django.contrib import admin
from .models import *


class AppointmentAdmin(admin.ModelAdmin):

    model = Appointment

    list_display = ['user', 'day', 'time', 'description', 'dog', 'status']
    fieldsets = ()
    add_fieldsets = add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type',),
            }
        ),
    )
    search_fields = []
    ordering = []
    filter_horizontal = ()



admin.site.register(Appointment, AppointmentAdmin)

# Register your models here.

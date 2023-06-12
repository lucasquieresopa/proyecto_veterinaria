from django.contrib import admin

from django.contrib import admin
from .models import FoundPost

class AdoptionPostAdmin(admin.ModelAdmin):

    add_form = FoundPost
    model = FoundPost

    list_display = ['description', 'author', 'zone','age', 'sex', 'was_delivered', 'image']
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

admin.site.register(FoundPost, AdoptionPostAdmin)

# Register your models here.

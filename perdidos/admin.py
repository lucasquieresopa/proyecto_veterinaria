from django.contrib import admin
from .models import LostPost

class AdoptionPostAdmin(admin.ModelAdmin):

    add_form = LostPost
    model = LostPost

    list_display = ['name', 'author', 'zone','age', 'sex', 'was_found', 'image']
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

admin.site.register(LostPost, AdoptionPostAdmin)

from django.contrib import admin
from .models import AdoptionPost

class AdoptionPostAdmin(admin.ModelAdmin):

    add_form = AdoptionPost
    model = AdoptionPost

    list_display = ['name', 'author', 'age', 'sex']
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

admin.site.register(AdoptionPost, AdoptionPostAdmin)

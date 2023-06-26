from django.contrib import admin
from .models import Campaign

class CampaignPostAdmin(admin.ModelAdmin):

    add_form = Campaign
    model = Campaign

    list_display = ['author', 'campaign_name', 'target_date', 'target_money', 'actual_money']
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

admin.site.register(Campaign, CampaignPostAdmin)

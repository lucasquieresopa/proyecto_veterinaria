from django.contrib import admin
from .models import Campaign, Discount

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

class DiscountAdmin(admin.ModelAdmin):

    model = Discount

    list_display = ['email']
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
admin.site.register(Discount, DiscountAdmin)

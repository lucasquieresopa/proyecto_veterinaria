from django.contrib import admin
from .models import Dog, Attention, Vaccination
from django.contrib.auth.admin import UserAdmin
from .forms import DogCreationForm, AttentionRegisterForm, VaccinationRegisterForm

# Register your models here.




class DogAdmin(admin.ModelAdmin):

    #form = 
    add_form = DogCreationForm
    model = Dog

    list_display = ['id', 'name', 'date_of_birth', 'sex', 'breed', 'owner', 'hidden']
    fieldsets = ()
    add_fieldsets = add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'date_of_birth', 'sex', 'breed'),}),)
    search_fields = ['name']
    ordering = ['name']
    filter_horizontal = ()



class AttentionAdmin(admin.ModelAdmin):

    add_form = AttentionRegisterForm
    model = Attention

    list_display = ['type', 'dog']
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


class VaccinationAdmin(admin.ModelAdmin):

    add_form = VaccinationRegisterForm
    model = Vaccination

    list_display = ['type', 'dog', 'date_of_application', 'suggestions',]
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


admin.site.register(Dog, DogAdmin)
admin.site.register(Attention, AttentionAdmin)
admin.site.register(Vaccination, VaccinationAdmin)
from django.contrib import admin
from .models import Dog
from django.contrib.auth.admin import UserAdmin
from .forms import DogCreationForm

# Register your models here.



class DogAdmin(admin.ModelAdmin):

    #form = 
    add_form = DogCreationForm
    model = Dog

    list_display = ['id', 'name', 'age', 'sex', 'breed', 'owner', 'hidden']
    fieldsets = ()
    add_fieldsets = add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'age', 'sex', 'breed'),}),)
    search_fields = ['name']
    ordering = ['name']
    filter_horizontal = ()

admin.site.register(Dog, DogAdmin)
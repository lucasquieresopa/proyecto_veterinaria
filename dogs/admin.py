from django.contrib import admin
from .models import Dog
from django.contrib.auth.admin import UserAdmin
from .forms import DogCreationForm

# Register your models here.



class DogAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    #form = 
    add_form = DogCreationForm
    model = Dog
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['name', 'age', 'sex', 'breed']
    fieldsets = ()
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'age', 'sex', 'breed'),}),)
    search_fields = ['name']
    ordering = ['name']
    filter_horizontal = ()

admin.site.register(Dog, DogAdmin)
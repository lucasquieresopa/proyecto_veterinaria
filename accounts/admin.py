from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserModificationForm
from accounts.models import CustomUser
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group

#             )


# admin.site.register(CustomUser, CustomUserAdmin)    #agrega los modelos a la vista del admin


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = CustomUserModificationForm
    add_form = CustomUserCreationForm
    model = CustomUser
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['id', 'email', 'name', 'surname', 'is_veterinario', 'is_staff']
    fieldsets = ()
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'is_veterinario'),}),)
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()
    



admin.site.register(CustomUser, CustomUserAdmin)

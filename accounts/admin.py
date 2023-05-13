from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserModificationForm
from accounts.models import CustomUser
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group

# class CustomUserAdmin(UserAdmin):   #extiende el admin al formato de usuario personalizado
# #     add_form = CustomUserCreationForm
# #     form = CustomUserChangeForm
# #     model = CustomUser
#     list_display = ['email', 'name', 'surname', 'address', 'telephone', 'is_staff', ]  #-> controlar campos
#     search_fields = ('email', )
#     readonly_fields = ()
#     ordering = ('email',)
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()


#     def save_model(self, request, obj, form, change):
#         if not change and not obj.has_usable_password():
#             # Django's PasswordResetForm won't let us reset an unusable
#             # password. We set it above super() so we don't have to save twice.
#             obj.set_password(get_random_string())
#             reset_password = True
#         else:
#             reset_password = False

#         super(UserAdmin, self).save_model(request, obj, form, change)

#         if reset_password:
#             reset_form = PasswordResetForm({'email': obj.email})
#             assert reset_form.is_valid()
#             reset_form.save(
#                 subject_template_name='registration/account_creation_subject.txt',
#                 email_template_name='registration/account_creation_email.html',
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
    list_display = ['email', 'name', 'surname', 'is_veterinario', 'is_staff']
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

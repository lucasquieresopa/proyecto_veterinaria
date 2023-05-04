from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):   #extiende el admin al formato de usuario personalizado
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
    list_display = ['email', 'name', 'surname', 'address', 'telephone', 'is_staff', ]  #-> controlar campos
    search_fields = ('email', )
    readonly_fields = ()
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(CustomUser, CustomUserAdmin)    #agrega los modelos a la vista del admin

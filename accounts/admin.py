from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):   #extiende el admin al formato de usuario personalizado
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'is_staff', ]  #-> controlar campos
                                    #añadir y modificar campos
    fieldsets = UserAdmin.fieldsets + ( 
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( 
        (None, {'fields': ('name',)}),
    )



admin.site.register(CustomUser, CustomUserAdmin)

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [       #apunta a la app de auth 
    #path('', views.login_view, name="login"),      -----> pasé login a pr_vet/url para que sea /login/ y no /account/login/
    
    #LOGOUT
    path('logout/', views.logout_view, 
        name="logout"),
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    

    #MANEJO DE CLIENTES
    path('client_registration/', views.user_registration_view, 
        name='client_registration'),
    path('modif/', views.account_modif_view, 
        name='account_modif'),
    path('modif/done/', views.account_modif_done,
        name='account_modif_succeed'),


    #CAMBIO DE CONTRASEÑA
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_succeed.html'), 
        name='password_change_done'),

    #RESET DE CONTRASEÑA
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_mail_form.html'), 
        name='password_reset'),
    # path(
    #     'password_reset/', 
    #     views.password_reset_view, 
    #     name='password_reset'
    # ),


    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_pass_form.html'), name='password_reset_confirm'),
    
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_peticion_done.html'),
        name='password_reset_done'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_succeed.html'),
        name='password_reset_complete'),
    
    
    #PERFIL Y BUSQUEDA
    path('profile/<pk>', views.profile_view, name= 'profile'),
    path('search/', views.search_user, name='search_user'),
    #path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('list_users/', views.list_users, name='list_users'),

]

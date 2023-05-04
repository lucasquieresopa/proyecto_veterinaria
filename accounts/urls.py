from django.urls import path
#from .views import SignUpView
from .views import user_registration_view


urlpatterns = [
    #path('client-registration/', user_registration_view, name='signup'),   #/accounts/signup muestra la view de signup (la 
                                                            #cual es un template .html linkeado a una clase viewSignup)
]

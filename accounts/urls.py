from django.urls import path
#from .views import SignUpView
from .views import account_modif_view


urlpatterns = [
    path('modif/', account_modif_view, name='account-modif'),  
]

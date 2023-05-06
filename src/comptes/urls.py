from django.urls import path
from comptes.views import login_view

urlpatterns = [    
   path('', login_view, name="login"),
]

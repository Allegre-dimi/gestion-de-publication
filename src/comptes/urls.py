
from django.urls import path
from .views import *


urlpatterns = [
    path('connexion/', AuthentificationView.as_view(), name="connexion"),
    path('', index, name="accueil"),
    path('déconnexion/', deconnexion, name='deconnexion')
]


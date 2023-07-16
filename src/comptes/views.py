from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AuthentificationView(TemplateView):
    template_name = "comptes/pages/Auth.html"


    


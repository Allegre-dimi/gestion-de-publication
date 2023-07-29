from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.


class AuthentificationView(TemplateView):
    template_name = "comptes/pages/Auth.html"
    
def index(request):
    if not request.user.is_authenticated:
        redirect("connexion")
    return render(request, 'comptes/pages/index.html')

def deconnexion(request):
    logout(request)
    return redirect("/")

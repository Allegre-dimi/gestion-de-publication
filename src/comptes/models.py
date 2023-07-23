import bcrypt
from django.core import validators
from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="generer_nom_fichier", blank=True, null=True)

    def __str__(self):
        return self.nom
    
class Comptes(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=128, blank= False, unique = True)

    def __str__(self):
        return self.login
    
class typeProfile(models.Model):

    def __str__(self):
        return self




    
    
    







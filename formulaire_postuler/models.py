from django.db import models
from django.conf import settings

# Create your models here.
class Formulaire_postuler(models.Model):
    nom = models.CharField(blank=False, null=False, max_length=30)
    prenom = models.CharField(blank=False, null=False, max_length=30)
    telephone = models.CharField(max_length=45, null=True)
    email = models.EmailField(blank=False, null=False)
    date_envoi = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.nom
    

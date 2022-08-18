from rest_framework import serializers
from formulaire_reunion_info import *
from .models import *

class Formulaire_reunion_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulaire_reunion_info
        fields = ["id",
                  "nom",
                  "prenom",
                  "telephone",
                  "email",
                  "date_reunion",
                  "date_envoi"
                  ]
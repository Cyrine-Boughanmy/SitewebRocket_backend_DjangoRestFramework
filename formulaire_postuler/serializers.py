from rest_framework import serializers
from formulaire_postuler.models import *
from .models import *

class Formulaire_postulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulaire_postuler
        fields = ["id",
                  "nom",
                  "prenom",
                  "telephone",
                  "email",
                  "date_envoie"
                  ]
    
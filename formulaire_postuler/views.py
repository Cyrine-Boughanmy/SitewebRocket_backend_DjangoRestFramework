from django.shortcuts import render
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from formulaire_postuler.models import *
from formulaire_postuler.serializers import *

# Create your views here.

class Formulaire_postulerList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Formulaire_postuler.objects.all()
    serializer_class = Formulaire_postulerSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['date_envoi']

    def filter_queryset(self, queryset):
        queryset = super(Formulaire_postulerList, self).filter_queryset(queryset)
        return queryset.order_by('-id')
    
    
class Formulaire_postulerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Formulaire_postuler.objects.all()
    serializer_class = Formulaire_postulerSerializer

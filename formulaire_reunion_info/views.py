from django.shortcuts import render
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from formulaire_reunion_info.models import *
from formulaire_reunion_info.serializers import *


# Create your views here.
class Formulaire_reunion_infoList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Formulaire_reunion_info.objects.all()
    serializer_class = Formulaire_reunion_infoSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['date_envoi']

    def filter_queryset(self, queryset):
        queryset = super(Formulaire_reunion_infoList, self).filter_queryset(queryset)
        return queryset.order_by('-id')
    
    
class Formulaire_reunion_infoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Formulaire_reunion_info.objects.all()
    serializer_class = Formulaire_reunion_infoSerializer
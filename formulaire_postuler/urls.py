from django.urls import path
from formulaire_postuler.views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # List views
    path('liste/', Formulaire_postulerList.as_view()),
    # Detail views
    path('details/<int:pk>/', Formulaire_postulerDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from formulaire_reunion_info.views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # List views
    path('liste/', Formulaire_reunion_infoList.as_view()),
    # Detail views
    path('details/<int:pk>/', Formulaire_reunion_infoDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
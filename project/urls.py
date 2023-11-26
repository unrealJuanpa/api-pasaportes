"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('continente/', Continente_APIView_General.as_view()),
    path('continente/<int:id>/', Continente_APIView_Detail.as_view()),

    path('pais/', Pais_APIView_General.as_view()),
    path('pais/<int:id>/', Pais_APIView_Detail.as_view()),
    
    path('persona/', Personas_APIView_General.as_view()),
    path('persona/<int:id>/', Personas_APIView_Detail.as_view()),
    
    path('pasaporte/', Pasaporte_APIView_General.as_view()),
    path('pasaporte/<int:id>/', Pasaporte_APIView_Detail.as_view()),

    path('pasaporteporpersona-orm/<int:id>/', PasaportesPorPersona_APIView.as_view()),
    path('pasaporteporpais-orm/<int:id>/', PasaportesPorPais_APIView.as_view()),
    path('pasaporteporcontinente-orm/<int:id>/', PasaportesPorContinente_APIView.as_view()),

    path('pasaporteporpersona-raw/<int:id>/', PasaportesPorPersonaRAW_APIView.as_view()),
    path('pasaporteporpais-raw/<int:id>/', PasaportesPorPaisRAW_APIView.as_view()),
    path('pasaporteporcontinente-raw/<int:id>/', PasaportesPorContinenteRAW_APIView.as_view())
]

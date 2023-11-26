from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
import django
import datetime
from .baseview import *


# Vistas
# Vistas de pasaportes
class Pasaporte_APIView_General(APIView_General):
    model = Pasaporte

class Pasaporte_APIView_Detail(APIView_Detail):
    model = Pasaporte

# Vistas de personas
class Personas_APIView_General(APIView_General):
    model = Persona

class Personas_APIView_Detail(APIView_Detail):
    model = Persona

# Vistas de paises
class Pais_APIView_General(APIView_General):
    model = Pais

class Pais_APIView_Detail(APIView_Detail):
    model = Pais

# Vistas de continentes
class Continente_APIView_General(APIView_General):
    model = Continente

class Continente_APIView_Detail(APIView_Detail):
    model = Continente


# Vistas especificas - ORM
class PasaportesPorPersona_APIView(APIView):
    def get(self, request, id):
        try:
            return Response(list(Pasaporte.objects.filter(persona_id=id).values()), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)
        

class PasaportesPorPais_APIView(APIView):
    def get(self, request, id):
        try:
            return Response(list(Pasaporte.objects.filter(pais_id=id).values()), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)


class PasaportesPorContinente_APIView(APIView):
    def get(self, request, id):
        try:
            return Response(list(Pasaporte.objects.filter(pais__continente_id=id).values()), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)


# Vistas especificas - RAW
class PasaportesPorPersonaRAW_APIView(APIView):
    def get(self, request, id):
        try:
            return Response(TARS.executeQuery(f"SELECT * FROM api_pasaporte WHERE persona_id = {int(id)};"), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)
        

class PasaportesPorPaisRAW_APIView(APIView):
    def get(self, request, id):
        try:
            return Response(TARS.executeQuery(f"SELECT * FROM api_pasaporte WHERE pais_id = {int(id)};"), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)


class PasaportesPorContinenteRAW_APIView(APIView):
    def get(self, request, id):
        try:
            return Response(TARS.executeQuery(f"SELECT api_pasaporte.id, api_pasaporte.created, api_pasaporte.modified, api_pasaporte.is_removed, api_pasaporte.numeropasaporte, api_pasaporte.fechaemision, api_pasaporte.fechavence, api_pasaporte.observaciones, api_pasaporte.pais_id, api_pasaporte.persona_id FROM api_pasaporte INNER JOIN api_pais ON api_pasaporte.pais_id = api_pais.id WHERE api_pais.continente_id = {int(id)};"), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)

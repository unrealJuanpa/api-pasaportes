import django
from rest_framework.response import Response
from rest_framework import status
from django.db import connection


class TARS:
    def executeQuery(query):
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            
            data_list = []
            for row in results:
                row_dict = dict(zip([col[0] for col in cursor.description], row))
                data_list.append(row_dict)
            
            return data_list
        
    def posthelper(model:django.db.models.base.ModelBase, request):
        try:
            model.objects.create(**request.data)
            return Response({'message': 'Registro almacenado con éxito'}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': f'ERROR: {ex}'}, status=status.HTTP_400_BAD_REQUEST)
        
    def getAllHelper(model:django.db.models.base.ModelBase):
        try:
            return Response(list(model.objects.all().values()), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {ex}'}, status=status.HTTP_400_BAD_REQUEST)
            

    def getByIdHelper(model:django.db.models.base.ModelBase, id):
        try:
            return Response(list(model.objects.filter(id=id).values())[0], status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)
        
    def putHelper(model:django.db.models.base.ModelBase, request, id):
        try:
            obj = model.objects.get(id=id)
            for fname in list(request.data.keys()):
                setattr(obj, fname, request.data[fname])
            obj.save()
            return Response({'message': 'Registro modificado con éxito!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)
        
    def deleteHelper(model:django.db.models.base.ModelBase, id):
        try:
            obj = model.objects.get(id=id)
            obj.delete()
            return Response({'message': 'Registro eliminado con éxito!'}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'ERROR: {str(ex)}'}, status=status.HTTP_400_BAD_REQUEST)

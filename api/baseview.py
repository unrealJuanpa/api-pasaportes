from rest_framework.views import APIView
from .tars import *


class APIView_General(APIView):
    def post(self, request, format=None, *args, **kwargs):
        return TARS.posthelper(self.model, request)
        
    def get(self, request=None):
        return TARS.getAllHelper(self.model)
        
class APIView_Detail(APIView):
    def get(self, id, request=None):
        return TARS.getByIdHelper(self.model, id=id)
        
    def put(self, request, id):
        return TARS.putHelper(self.model, request, id=id)
        
    def delete(self, request, id):
        return TARS.deleteHelper(self.model, id=id)
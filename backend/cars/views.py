from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarsSerializer
from .models import Cars
from django.http import Http404

class CarsApiView(APIView):
    def get(self, request):
        data = Cars.objects.all()
        serializers = CarsSerializer(data, context={'request': request}, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CarDetailView(APIView):
    # Получение объекта
    def get_object(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404
    
    # GET - получение конкретной записи
    def get(self, request, pk):
        car = self.get_object(pk)
        serializer = CarsSerializer(car)
        return Response(serializer.data)
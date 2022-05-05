from django.shortcuts import render

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
    
    def patch(self,request):
        return Response(data="Este es el método patch!", status=200)

    def delete(self,request):
        return Response(data="Este es el método delete!", status=200)

    def post(self,request):
        return Response(data="Este es el método post!", status=200)

class PetListAPIView(ListAPIView):

    def get(self,request):
        return Response(data="Estas son todas mis mascotas!", status=200)

class PetAPIView(RetrieveAPIView):

    def get(self,request):
        return Response(data="Este es el método get de PetAPIView!", status=200)
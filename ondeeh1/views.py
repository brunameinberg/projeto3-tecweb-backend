from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Pais
from .serializers import PaisSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def api_pais(request, pais):
    if request.method == 'POST':
        resultado = Pais.objects.filter(pais=pais)
        if len(resultado)==0:
            pais = Pais(pais=pais,chutes=1)
        else:
            pais = resultado[0]
            pais.chutes+=1
        pais.save()
    all_paises = Pais.objects.filter(pais=pais)
    
    serialiazed_pais = PaisSerializer(all_paises,many=True)
    return Response(serialiazed_pais.data)
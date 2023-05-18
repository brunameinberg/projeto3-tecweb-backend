from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404, HttpResponseForbidden, JsonResponse
from .models import Usuario
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your views here.

@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()
@api_view(['POST'])
def api_user(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']

        user = User.objects.create_user(username, password)
        user.save()
        return Response(status=204)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) 
def api_pontuacao(request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(user=request.user)
        pontuacao = request.pontuacao
        usuario.pontuacao += pontuacao
        usuario.save()

    usuario = Usuario.objects.filter(user=request.user)
    serialized_user = UserSerializer(user=usuario)
    return Response(serialized_user.data)

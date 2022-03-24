from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import * 

# Create your views here.



@api_view(['GET'])
def overviews(request):
    api_urls = {
        'Overviews':'/',
        'All Data':'/all-data/',
        'All Data':'/all-data/',
        'Create Data':'/create-data/',
        
    }
    return Response(api_urls)



@api_view(['GET'])
def all_data(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def one_data(request,pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users)
    return Response(serializer.data)


@api_view(['GET','POST'])
def create_data(request):
    if request.method == 'POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    data = {
        "id": 1,
        "name": "jay",
        "email": "jay@gmail.com",
        "phone": "9067419521",
        "address": "surat"
    }
    return Response(data)
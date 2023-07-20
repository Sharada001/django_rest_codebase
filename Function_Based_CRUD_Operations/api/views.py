from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def CRUDView(request, pk=None, *args, **kwargs):
    if request.method == 'GET':



    elif request.method == 'POST':



    elif request.method == 'PUT':



    elif request.method == 'PATCH':



    elif request.method == 'DELETE':
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, Http404
from .models import Food
from .serializers import ItemSerializer
from django.forms.models import model_to_dict

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def CRUDView(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            instance = get_object_or_404(Food, pk=pk)   # returned 'instance' is a single object
            # below commented code set is an alternative of above single line
            # queryset = Food.objects.filter(pk=pk)
            # if not queryset.exists() :
            #     raise Http404
            serializer = ItemSerializer(instance)
            return Response(serializer.data)
        queryset = Food.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({"message":"Invalid data"}, status=400)

    elif request.method == 'PUT':
        instance = get_object_or_404(Food, pk=pk)   # used to raise error if item not found in database
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            Food.objects.filter(pk=pk).update(**serializer.data)
            return Response(serializer.data, status=200)
        return Response({"message":"Invalid data"}, status=400)

    elif request.method == 'PATCH':
        instance = get_object_or_404(Food, pk=pk)
        newData = model_to_dict(instance)
        for key, value in request.data.items():
            if key in newData:
                newData[key] = value
        serializer = ItemSerializer(data=newData)
        if serializer.is_valid():
            Food.objects.filter(pk=pk).update(**serializer.data)
            return Response(serializer.data, status=200)
        return Response({"message": "Invalid data"}, status=400)

    elif request.method == 'DELETE':
        instance = get_object_or_404(Food,pk=pk)    # used to raise error if item not found in database
        Food.objects.filter(pk=pk).delete()
        return Response({"message":"Item Deleted"}, status=204)
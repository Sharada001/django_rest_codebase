from django.shortcuts import render
from .serializers import ItemSerializer
from .models import Food
from rest_framework import generics, mixins

class ItemMixinView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




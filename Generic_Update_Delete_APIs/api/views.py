from .serializers import ItemSerializer
from rest_framework import generics
from .models import Food

class UpdateItemView(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.title = instance.title + ' updated '
        instance.save()


class DeleteItemView(generics.DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
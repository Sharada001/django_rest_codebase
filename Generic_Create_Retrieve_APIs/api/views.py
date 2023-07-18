from rest_framework import generics
from .serializers import ItemSerializer
from .models import Food


class RetrieveItemView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer


class CreateItemView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        quantity = serializer.validated_data.get('quantity')
        if quantity is None:
            quantity = 0
        serializer.save(quantity=quantity)


class ListItemsView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer


class CreateAndListItemsView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer

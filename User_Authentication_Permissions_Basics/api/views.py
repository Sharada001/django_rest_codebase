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


class UpdateItemView(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # serializer object(received from serializer argument) received here contains
        # updated(using the data in request) and validated data.
        # !!! But that data yet haven't been committed to database
        # (So object in database still contains old data)
        # we can commit that data to database with serializer.save()
        instance = serializer.save()    # returned object contains commited data from database
        instance.title = instance.title + ' updated '   # We can edit received object's values here
        instance.save()     # After making changes to object, we must commit it back to database

        # !!!! we cannot use 'serializer.data' in perform_**** methods (that generates an error)
        # Instead we can use 'serializer.validated_data' to access that details


class DeleteItemView(generics.DestroyAPIView):  # !!! view name is DestroyAPIView
    queryset = Food.objects.all()
    serializer_class = ItemSerializer

    def perform_destroy(self, instance):    # !!! method name is perform_destroy
        # Relevant object(received from instance argument) yet has not been deleted from database
        super().perform_destroy(instance)
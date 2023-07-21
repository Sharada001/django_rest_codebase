from rest_framework import generics, permissions, authentication
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
        price = serializer.validated_data.get('price')
        if quantity < 0: quantity = 0
        if price < 0: price = 0
        serializer.save(quantity=quantity, price=price)


class ListItemsView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer


class CreateAndListItemsView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    # default users are not allowed to POST, but they can get ListView


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
        if instance.quantity < 0: instance.quantity = 0   # We can edit received object's values here
        if instance.price < 0: instance.price = 0
        instance.save()     # After making changes to object, we must commit it back to database

        # !!!! we cannot use 'serializer.data' in perform_**** methods (that generates an error)
        # Instead we can use 'serializer.validated_data' to access that details


class DeleteItemView(generics.DestroyAPIView):  # !!! view name is DestroyAPIView
    queryset = Food.objects.all()
    serializer_class = ItemSerializer

    def perform_destroy(self, instance):    # !!! method name is perform_destroy
        # Relevant object(received from instance argument) yet has not been deleted from database
        super().perform_destroy(instance)
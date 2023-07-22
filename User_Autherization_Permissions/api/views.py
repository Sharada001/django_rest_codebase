from rest_framework import generics, authentication, permissions
from .serializers import ItemSerializer
from .permissions import IsStaffEditorPermission, IsStaffEditorGetPermission
from .models import Food


class RetrieveItemView(generics.RetrieveAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser ,IsStaffEditorGetPermission]
    # permissions, that must be checked first must come first in 'permission_classes' list
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
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]
    queryset = Food.objects.all()
    serializer_class = ItemSerializer


class CreateAndListItemsView(generics.ListCreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    # Problem with 'DjangoModelPermissions' is, even though we have only allowed authorized users to
    # access this API with 'POST' and 'GET'(ListView) methods, still this API allows ListView
    # for non-authorized users. (only 'POST' api is blocked)
    # That's because 'appName.view_modelName' permission is given to both DetailView and ListView,
    # and in this case, DjangoModelPermissions can't check permission to 'appName.view_modelName' because
    # this class is not responsible for handling DetailViews.
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
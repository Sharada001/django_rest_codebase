from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Food
from .serializers import ItemSerializer

@api_view(["GET"])
def get_food(request, key):
    data = {}
    try :
        instance = Food.objects.get(pk=key)
        data = ItemSerializer(instance).data
        return Response(data)                   # A dictionary should be given as argument for Response()
    except:
        return Response({"message":"item not found"},status=400)

@api_view(["POST"])         # Because of decorator we don't need to add CSRF token
def set_food(request):
    try :
        data = request.data
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            instanceSet = Food.objects.filter(item_code=serializer.data['item_code']).values()
            if len(list(instanceSet))>0:
                # item already in the database
                totalQuantity = serializer.data['quantity'] + list(instanceSet)[0]['quantity']
                Food.objects.filter(item_code=serializer.data['item_code']).update(quantity=totalQuantity)
                return Response({"message":"quantity increased !"})
            else:
                # item is new to the database
                dataDict = dict(serializer.data)    # serializer.data is a read-only dictionary. So 'discount' cannot be popped from it
                dataDict.pop('discount')
                Food.objects.create(**dataDict)
                return Response(dataDict)
        else:
            raise Exception
    except:
        return Response({"message":"invalid item details !"},status=400)
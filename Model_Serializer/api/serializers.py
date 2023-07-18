from rest_framework import serializers
from .models import Food

class ItemSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = [
            'title',
            'item_code',
            'price',
            'quantity',
            'discount'
        ]

    def get_discount(self, obj):
        try:
            return float(obj.price)*0.1
        except:
            return 0

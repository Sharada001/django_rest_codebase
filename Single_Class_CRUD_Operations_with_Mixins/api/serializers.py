from rest_framework import serializers
from .models import Food

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'title',
            'item_code',
            'price',
            'quantity'
        ]


from django.contrib import admin
from .models import Food

admin.site.register(Food)
# This allows editing access to 'Food' model, within the '/admin/' view


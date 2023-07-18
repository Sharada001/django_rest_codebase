from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:key>', views.get_food),
    path('item/', views.set_food),
]
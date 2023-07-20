from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:pk>',views.CRUDView),
    path('item/',views.CRUDView),
    path('item/<int:pk>',views.CRUDView),
]
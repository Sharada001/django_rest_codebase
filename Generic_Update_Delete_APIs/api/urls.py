from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:pk>/update', views.UpdateItemView.as_view()),
    path('item/<int:pk>/delete', views.DeleteItemView.as_view())
]
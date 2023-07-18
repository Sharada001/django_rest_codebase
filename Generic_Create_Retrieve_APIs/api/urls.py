from django.urls import path
from . import views

urlpatterns =[
    path('item/<int:pk>', views.RetrieveItemView.as_view()),
    path('item/', views.CreateItemView.as_view()),
    path('items/', views.ListItemsView.as_view()),
    path('item-set/', views.CreateAndListItemsView.as_view()),
]


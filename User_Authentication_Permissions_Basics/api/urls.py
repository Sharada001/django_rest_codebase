from django.urls import path
from . import views

# app_name = 'api'
urlpatterns =[
    path('item/<int:pk>', views.RetrieveItemView.as_view()),
    path('item/', views.CreateItemView.as_view()),
    path('items/', views.ListItemsView.as_view(), name='listview'),
    path('item-set/', views.CreateAndListItemsView.as_view()),
    path('item/<int:pk>/update', views.UpdateItemView.as_view()),
    path('item/<int:pk>/delete', views.DeleteItemView.as_view()),
    # path('login/', views.CustomLoginView.as_view(), name='login')
]


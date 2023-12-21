from .views import TodoView, TodoDetail
from django.urls import path

urlpatterns = [
    path('todo/', TodoView.as_view(), name='Todo' ),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='TodoDetail' ),
    
]

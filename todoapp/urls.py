from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>/', TodoDetail.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view()),
    path('create/', CreateTodo.as_view()),

]

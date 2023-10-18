# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', TodoList.as_view()),
#     path('<int:pk>/', TodoDetail.as_view()),
#     path('delete/<int:pk>', DeleteTodo.as_view()),
#     path('create/', CreateTodo.as_view()),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo-list'),
    path('todos/<int:pk>/', views.todo_detail, name='todo-detail'),
    path('create-todo/', views.create_todo, name='create-todo'),
    path('delete-todo/<int:pk>/', views.delete_todo, name='delete-todo'),
]

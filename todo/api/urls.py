from django.contrib import admin
from django.urls import path, include
from todo.api import views as api_views
urlpatterns = [
    path('todo-list/', api_views.ToDoListView, name='todolist')
]
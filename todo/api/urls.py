from django.contrib import admin
from django.urls import path, include
from todo.api import views as api_views
urlpatterns = [
    path('list', api_views.TodoListView.as_view(), name='todolist'),
    path('detail/<int:pk>', api_views.TodoListDetailView.as_view(), name='todolist_detail'),
    path('user-list/', api_views.UserListView.as_view(), name='userlist')
    
]
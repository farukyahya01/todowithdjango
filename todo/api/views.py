from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import TodoList
from todo.api.serializers import TodoListSerializers

@api_view(['GET', 'POST'])
def ToDoListView(request):
    if request.method == 'GET':
        todolist = TodoList.objects.all()
        serializer = TodoListSerializers(todolist, many=True)
        return Response(serializer.data)

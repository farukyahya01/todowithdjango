from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from todo.models import TodoList
from django.contrib.auth.models import User
from todo.api.serializers import TodoListSerializers, UserSerializers

### CLASS BASED ###
class TodoListView(APIView):
    def get(self, request):
        todolist = TodoList.objects.all()
        serializer = TodoListSerializers(todolist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class TodoListDetailView(APIView):
    def get_object(self, pk):
        todolist_detail = get_object_or_404(TodoList, pk=pk)
        return todolist_detail

    def get(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoListSerializers(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoListSerializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        todo = self.get_object(pk=pk)
        todo.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class UserListView(APIView):
    def get(self ,request):
        userlist = User.objects.all()
        serializer = UserSerializers(userlist, many=True, context={'request': request})
        return Response(serializer.data)



# @api_view(['GET', 'PUT', 'DELETE'])
# def TodoListDetailView(request, pk):
#     try:
#         todolist_detail = TodoList.objects.get(pk=pk)
#     except TodoList.DoesNotExist:
#         return Response(
#             {
#                 'errors' : {
#                     'code' : '404',
#                     'message' : f'Böyle bir id {{pk}} ile ilgili todo bulunamadı'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     if request.method == 'GET':
#         serializer = TodoListSerializers(todolist_detail)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         pass

#     if request.method == 'DELETE':
#         pass



#### FUNCTION BASED 
# @api_view(['GET', 'POST'])
# def ToDoListView(request):
#     if request.method == 'GET':
#         todolist = TodoList.objects.all()
#         serializer = TodoListSerializers(todolist, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = TodoListSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


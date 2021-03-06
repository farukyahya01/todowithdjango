from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from todo.models import TodoList
from django.contrib.auth.models import User
from todo.api.serializers import TodoListSerializers, UserSerializers
from todo.api.pagination import SmallPagination, MediumPagination, LargePagination

from rest_framework import generics
from rest_framework import permissions
from todo.api.permissions import IsTodoRecordOwner
# CONCRETE VIEWS
class TodoListView(generics.ListCreateAPIView):    
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializers
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MediumPagination

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)

class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializers
    permission_classes = [permissions.IsAuthenticated, IsTodoRecordOwner]


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]




# GENERICS API VIEW
# class TodoListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    
#     queryset = TodoList.objects.all()
#     serializer_class = TodoListSerializers

#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class TodoListDetailView(GenericAPIView):
#     pass

# class UserListView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers

#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

### CLASS BASED ###
# class TodoListView(APIView):
#     def get(self, request):
#         todolist = TodoList.objects.all()
#         serializer = TodoListSerializers(todolist, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TodoListSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# class TodoListDetailView(APIView):
#     def get_object(self, pk):
#         todolist_detail = get_object_or_404(TodoList, pk=pk)
#         return todolist_detail

#     def get(self, request, pk):
#         todo = self.get_object(pk=pk)
#         serializer = TodoListSerializers(todo)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         todo = self.get_object(pk=pk)
#         serializer = TodoListSerializers(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk):
#         todo = self.get_object(pk=pk)
#         todo.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)

# class UserListView(APIView):
#     def get(self ,request):
#         userlist = User.objects.all()
#         serializer = UserSerializers(userlist, many=True, context={'request': request})
#         return Response(serializer.data)



# @api_view(['GET', 'PUT', 'DELETE'])
# def TodoListDetailView(request, pk):
#     try:
#         todolist_detail = TodoList.objects.get(pk=pk)
#     except TodoList.DoesNotExist:
#         return Response(
#             {
#                 'errors' : {
#                     'code' : '404',
#                     'message' : f'B??yle bir id {{pk}} ile ilgili todo bulunamad??'
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


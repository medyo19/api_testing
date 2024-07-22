from django.shortcuts import render
from .models import TodoItem
from .serializer import TodoItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response # to return both data and status
from rest_framework import status


@api_view(['GET','POST']) # TO indicate it is a DRF view

def todo_list(request):
    if request.method == 'GET':
        list = TodoItem.objects.filter(user=request.user)# apply to the user attribute of the queryset 
        serializer = TodoItemSerializer(list)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)# to associate to a specific user 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','DELETE','PUT'])


def todo_detail(request, pk):
    try:
        todo = TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TodoItemSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = TodoItemSerializer(todo, data=request.data)# to map the existing item to the new data 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    


            


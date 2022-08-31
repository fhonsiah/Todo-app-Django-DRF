from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView): # here we get the list of todos /GET
    queryset = Todo.objects.all() # select * from todos
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
# Create your views here.

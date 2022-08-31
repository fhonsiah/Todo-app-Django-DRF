# todos/serializers.py
from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','body',)
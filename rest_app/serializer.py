from rest_framework import serializers
from .models import *

class students_serializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields="__all__"
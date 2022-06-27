from rest_framework.serializers import ModelSerializer
from .models import Student


class Student_serializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

from django.shortcuts import render
#
# Create your Model-views here.
# from rest_framework.viewsets import ModelViewSet
# from .models import Student
# from .serializers import Student_serializer
#
#
# class StudentView(ModelViewSet):
#     serializer_class = Student_serializer
#     queryset = Student.objects.all()

# create Apiview
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import Student_serializer
class StudentView(APIView):





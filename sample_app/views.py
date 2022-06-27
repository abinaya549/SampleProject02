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

"""create Apiview"""
from django.shortcuts import render, get_object_or_404
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import Student_serializer


class StudentView(APIView):
    """
    function for get
    """

    def get(self, request, pk=None):
        students = Student.objects.all().values()
        serializer = Student_serializer(students, many=True)
        return Response({"students": serializer.data})

    """
    function for post 
    """

    def post(self, request):
        students = request.data
        serializer = Student_serializer(data=students)
        if serializer.is_valid():
            students_saved = serializer.save()
        return Response({"success": "Forum '{}'created successfully".format(students_saved)})
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    function for put 
    """

    def put(self, request, pk):
        try:
            students = Student.objects.filter(id=pk).get()
            data = request.data
            #.get('students')
            serializer = Student_serializer(instance=students, data=data)
            serializer.is_valid(raise_exception=True)
            students = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            print("exception message", str(e))
            return Response({"err": "Fail to update"}, status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = Student.objects.get(id=pk)

        serializer = Student_serializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_204_NO_CONTENT)
        serializer.is_valid(raise_exception=True)
        return Response(status=HTTP_400_BAD_REQUEST)

    """
    function for delete 
    """

    def delete(self, request, pk):
        students = get_object_or_404(Student.objects.all(), pk=pk)
        students.delete()
        return Response({"message": "Forum with id `{}` has been deleted.".format(pk)}, status=204)
    # return Response(status=status.HTTP_204_NO_CONTENT)

from base.models import Course
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from base.course_serializer import CourseSerializer

class CourseDetail(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        course = CourseSerializer(course)
        return Response(course.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

# class CourseProjectList(APIView):
#     """
#     List all users, or create a new user.
#     """
#     def get(self, request, format=None):
#         projects = Project.objects.filter(course=course)
#         serializer = ProjectSerializer(courses, many=True)
#         return Response(serializer.data)

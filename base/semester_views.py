from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from base.serializers import semesterSerializer

class Semester(generics.ListCreateAPIView):
    """ API Endpoint for Semesters
    POST - Create a semester
    GET - Get info on a semester for a given semester id
    """
    #permission_classes = (permissions.IsAuthenticated, )
    def get_object(self, pk):
            try:
                return Semester.objects.get(pk=pk)
            except Semester.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
            semester = self.get_object(pk)
            semester = SemesterSerializer(semester)
            return Response(Semester.data)

    def post(self, request, format=None):
            serializer = SemesterSerializer(data=request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
            semester = self.get_object(pk)
            serializer = SemesterSerializer(semester, data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StartSemester(generics.CreateAPIView):
        """ API Endpoint to Move to the Next Semester
    POST - Deactivates all current courses and enrollments,
    activates all course and enrollments for the following semester.
    """
    def post(self, request, pk, format=none):
            permission_classes = (permissions.IsAuthenticated, )
            if request.user.groups.contains('admin'):
                return Response(status=status.HTTP_404_NOT_FOUND) 
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)            


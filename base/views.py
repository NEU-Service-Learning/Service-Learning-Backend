from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from base.models import Course, Instructor
from base.serializers import CourseSerializer
from base.serializers import UserSerializer
from base.serializers import InstructorSerializer


""" 
    THESE ARE JUST EXAMPLES, NOT GUARANTEED TO WORK
"""
class Instructors(generics.ListCreateAPIView):
    """API endpoints for Instructors.
    POST - Creates an instructor.
    GET - Gets a list of all instructors.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class InstructorsDetail(generics.RetrieveAPIView):
    """API endpoint for an Instructor.
    GET - Gets detailed info for the given instructor id.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class Users(generics.ListAPIView):
    """API endpoint for Users.
    GET - Gets a list of all Users.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """API endpoint for a User.
    GET - Gets detailed info for the given user id.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Courses(APIView):
    """API endpoints for Courses.
    POST - Creates a Course.
    GET - Gets a list of all courses.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        courses = Course.objects.filter(instructor__id=pk)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = CourseSerializer(data=request.data)
        try:
            instructor = Instructor.objects.get(pk=pk)
        except Instructor.DoesNotExist:
            return Response("Instructor not found.", status=status.HTTP_404_NOT_FOUND)
            
        if serializer.is_valid():
            serializer.save(owner=request.user, instructor=instructor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Semester(generics.ListCreateAPIView):
	""" API Endpoint for Semesters
	POST - Create a semester
	GET - Get info on a semester for a given semester id
	"""
	permission_classes = (permissions.IsAuthenticated, )i


class StartSemester(generics.CreateAPIView):
    	""" API Endpoint to Move to the Next Semester
    POST - Deactivates all current courses and enrollments,
    activates all course and enrollments for the following semester.
	"""
    def post(self, request, pk, format=none):
	    if request.user.is_authenticated:
		    if request.user.groups.contains('admin'):
			    stuff
                    else:
                         response = Response(status=status.HTTP_403_FORBIDDEN)
			 
            else:
		    response = Response(status=status.HTTP
		    response['next'] = '/semester/startnext/'
	            return response
            else:



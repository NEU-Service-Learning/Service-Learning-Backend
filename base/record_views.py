from base.models import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.http import Http404
from django.db.models import Sum
from django.http import Http404, HttpResponse
import csv

from base.record_serializer import RecordSerializer


class RecordDetail(APIView):
    """
    Post, Get, Put a Record instance
    """
    def get_object(self, pk):
        try:
            return Record.objects.filter(is_active=True).get(pk=pk)
        except Record.DoesNotExist:
            raise Http404("Object doesn't exist")

    def post(self, request, format=None):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        record = RecordSerializer(record)
        return Response(record.data)

    def put(self, request, pk, format=None):
        record = self.get_object(pk)
        record.is_active = False
        record.save()
        return self.post(request)

class RecordList(APIView):
    """
    List all active record ids(assume forever if no range is given)
    """

    def get(self, request, start_date=None, end_date=None, format=None):
        if start_date is None or end_date is None:
            records = Record.objects.filter(is_active=True)
        else:
            records = Record.objects.filter(date__range=[start_date, end_date], is_active=True)
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

class RecordListByUser(APIView):
    """
    Takes a User ID and returns all Records for that User (Active Records)
    """
    def get(self, request, user, format=None):
        records = Record.objects.filter(is_active=True, enrollment__in=Enrollment.objects.filter(user=user).
                                        values('id').distinct()).order_by('-date')
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

class RecordListByCourse(APIView):
    """
    Takes a Course ID and returns all Records for that Course
    """
    def get(self, request, course, format=None):
        records = Record.objects.filter(is_active=True,
                                        enrollment__in=Enrollment.objects.filter(course=course).values('id').distinct())
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

class RecordListByProject(APIView):
    """
    Takes a Project ID and returns all Records for that Project
    """
    def get(self, request, project, format=None):
        records = Record.objects.filter(is_active=True, project=project).order_by('-date')
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

class RecordHoursForUser(APIView):
    """
    Takes a User ID and returns their total recorded hours for the given time range
    (assumes forever if no range is given)
    """
    def get(self, request, user, start_date=None, end_date=None, format=None):
        enrollments = Enrollment.objects.filter(user=user).values('id').distinct()
        if start_date is None or end_date is None:
            records = Record.objects.filter(is_active=True, enrollment__in=Enrollment.objects.filter(user=user)
                                            .values('id').distinct()).aggregate(Sum('total_hours'))
        else:
            records = Record.objects.filter(date__range=[start_date, end_date], is_active=True, enrollment__in=Enrollment.
                                            objects.filter(user=user).values('id').distinct())\
                .aggregate(Sum('total_hours'))
        return Response({'total_hours': records['total_hours__sum'] or 0})

class RecordHoursForProject(APIView):
    """
    Takes a Project ID and returns the total recorded hours for the given time range
    (assumes forever if no range is given)
    """
    def get(self, request, project, start_date=None, end_date=None, format=None):
        if start_date is None or end_date is None:
            records = Record.objects.filter(is_active=True, project=project).aggregate(Sum('total_hours'))
        else:
            records = Record.objects.filter(is_active=True, project=project, date__range=[start_date, end_date])\
                .aggregate(Sum('total_hours'))
        return Response({'total_hours': records['total_hours__sum'] or 0})

class RecordHoursForCourse(APIView):
    """
    Takes a Course ID and returns the total recorded hours for the given time range
    (assumes forever if no range is given)
    """
    def get(self, request, course, start_date=None, end_date=None, format=None):
        if start_date is None or end_date is None:
            records = Record.objects.filter(is_active=True, enrollment__in=Enrollment.objects.filter(course=course)
                                            .values('id').distinct()).aggregate(Sum('total_hours'))
        else:
            records = Record.objects.filter(is_active=True, enrollment__in=Enrollment.objects.filter(course=course)
                                            .values('id').distinct(), date__range=[start_date, end_date])\
                .aggregate(Sum('total_hours'))
        return Response({'total_hours': records['total_hours__sum'] or 0})


class RecordsExport(APIView):
	"""
	"""
	
	def get(self, request, format=None):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="All-Records.csv"'
		writer = csv.writer(response)
		writer.writerow(['Record Number', 'Enrollment Record', 'Project', 'Date', 'Start Time', 'Total Hours', 'Longitude', 'Latitude', 'Category', 'Is Active?', 'Comments'])
		for record in Record.objects.filter(is_active=True):
			temp = RecordSerializer(record, many = False)
			writer.writerow(temp.data.values())

		return response

from django.contrib.auth.models import User
from base.models import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from base.communityPartnerSerializer import CommunityPartnerSerializer

class CommunityPartnerDetail(APIView):
    """
    Post, retrieve, update or delete a community partner instance
    """
    def get_object(self, pk):
        try:
            return CommunityPartner.objects.get(pk=pk)
        except CommunityPartner.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = CommunityPartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        communityPartner = self.get_object(pk)
        communityPartner = CommunityPartnerSerializer(communityPartner);
        return Response(communityPartner.data);

    def put(self, request, pk, format=None):
        communityPartner = self.get_object(pk)
        serializer = CommunityPartnerSerializer(communityPartner, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        communityPartner = self.get_object(pk)
        communityPartner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

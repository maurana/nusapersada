from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from v1.models.profiles import Profiles
from v1.serializers.profiles import ProfilesSerializer

class ProfilesList(APIView):

    # list all
    def get(self, request, format=None):
        profiles = Profiles.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data)

    # create
    def post(self, request, format=None):
        serializer = ProfilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilesDetail(APIView):

    # get object
    def get_object(self, pk):
        try:
            return Profiles.objects.get(pk=pk)
        except Profiles.DoesNotExist:
            raise Http404

    # get one
    def get(self, request, pk, format=None):
        profiles = self.get_object(pk)
        serializer = ProfilesSerializer(profiles)
        return Response(serializer.data)

    # update
    def put(self, request, pk, format=None):
        profiles = self.get_object(pk)
        serializer = ProfilesSerializer(profiles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # remove
    def delete(self, request, pk, format=None):
        profiles = self.get_object(pk)
        profiles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render

# Create your views here.
# pulling dependencies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from .models import Fundraiser # from this models.py file, import this class called Fundraiser
from .models import Pledge
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer
from .permissions import IsOwnerOrReadOnly

class FundraiserList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ] #For unsafe methods (post, patch, delete), they need to be authenticated. Otherwise, they only get access to Get requests

    def get(self, request):
       fundraisers = Fundraiser.objects.all()
       serializer = FundraiserSerializer(fundraisers, many=True)
       return Response(serializer.data)
   
    def post(self, request):
       serializer = FundraiserSerializer(data=request.data) ## to serialise as json
       if serializer.is_valid(): ## built in function is_valid - valid as json format
           serializer.save(owner=request.user) ## call another function to save the data
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED

           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )
   
class FundraiserDetail(APIView): ## give me back a single fundraiser
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ] 
    
    def get(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk) ## helper function get_object_or_404
        serializer = FundraiserDetailSerializer(fundraiser) ## Add the nested serializer
        return Response(serializer.data)
    
    #put response is placed in fundraiaserdetail class because it needs to refer to a specific fundraiser
    def put(self, request, pk): #primary key (pk) needs to be specified to update the required fundraiser
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        self.check_object_permissions(request, fundraiser) #trigger the auth check
        serializer = FundraiserDetailSerializer(
            instance=fundraiser,
            data=request.data,
            partial=True #special option in Django; this allows for some fields to be updated.
        )
        if serializer.is_valid():#checking if the serializer is valid
            serializer.save()
            return Response(serializer.data)#on success, return the response
        #on any failure, return a 400 status request
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class PledgesList(APIView):

    def get(self, request):
       pledges = Pledge.objects.all()
       serializer = PledgeSerializer(pledges, many=True)
       return Response(serializer.data)
   
    def post(self, request):
       serializer = PledgeSerializer(data=request.data) ## to serialise as json
       if serializer.is_valid(): ## built in function is_valid - valid as json format
           serializer.save(supporter=request.user) ## call another function to save the data
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED

           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )
   
 
    




    

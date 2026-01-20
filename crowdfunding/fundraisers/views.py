from django.shortcuts import render

# Create your views here.
# pulling dependencies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Fundraiser # from this models.py file, import this class called Fundraiser
from .models import Pledge
from .serializers import FundraiserSerializer # from the serializer file, import this class called FundraiserSerializer
from .serializers import PledgeSerializer

class FundraiserList(APIView):

   def get(self, request):
       fundraisers = Fundraiser.objects.all()
       serializer = FundraiserSerializer(fundraisers, many=True)
       return Response(serializer.data)
   
   def post(self, request):
       serializer = FundraiserSerializer(data=request.data) ## to serialise as json
       if serializer.is_valid(): ## built in function is_valid - valid as json format
           serializer.save() ## call another function to save the data
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED

           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )
   
class FundraiserDetail(APIView): ## give me back a single fundraiser
    def get(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk) ## helper function get_object_or_404
        serializer = FundraiserSerializer(fundraiser)
        return Response(serializer.data)
    
class PledgesList(APIView):

   def get(self, request):
       pledges = Pledge.objects.all()
       serializer = PledgeSerializer(pledges, many=True)
       return Response(serializer.data)
   
   def post(self, request):
       serializer = PledgeSerializer(data=request.data) ## to serialise as json
       if serializer.is_valid(): ## built in function is_valid - valid as json format
           serializer.save() ## call another function to save the data
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED

           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )
   
 
    




    

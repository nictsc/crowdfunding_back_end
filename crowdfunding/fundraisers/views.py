from django.shortcuts import render

# Create your views here.
# pulling 4 dependencies
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fundraiser # from this models.py file, import this class called Fundraiser
from .serializers import FundraiserSerializer # from the serializer file, import this class called FundraiserSerializer

class FundraiserList(APIView):

   def get(self, request):
       fundraisers = Fundraiser.objects.all()
       serializer = FundraiserSerializer(fundraisers, many=True)
       return Response(serializer.data)
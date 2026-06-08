## pulling dependencies
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
## import Fundraiser and Pledge models from models.py file
from .models import Fundraiser, Pledge
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsFundraiserSoftDeleted, IsEndUserActiveAndNotSoftDeleted

## Create your views here
class FundraiserList(APIView):
    ## for unsafe methods (post, patch, delete), they need to be authenticated. Otherwise, they only get access to GET requests
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        IsEndUserActiveAndNotSoftDeleted
    ] 

    def get(self, request):
        ## show all the non soft-deleted fundraisers
        fundraisers = Fundraiser.objects.filter(is_deleted=False)
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

    def post(self, request):
        ## to serialise as json
        serializer = FundraiserSerializer(data=request.data) 
        ## built in function is_valid - valid as json format
        if serializer.is_valid(): 
            ## call another function to save the data
            serializer.save(owner=request.user) 
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        ## if response is invalid, return error 400
        return Response( 
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


## show one fundraiser
class FundraiserDetail(APIView): 
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        IsEndUserActiveAndNotSoftDeleted
    ] 
    
    def get(self, request, pk):
        ## show one fundraiser that is not soft deleted, helper function get_object_or_404
        fundraiser = get_object_or_404(Fundraiser, pk=pk, is_deleted=False)
        ## Add the nested serializer
        serializer = FundraiserDetailSerializer(fundraiser) 
        return Response(serializer.data)
    
    '''
    put response is placed in FundraiaserDetail class because it needs to refer to a specific fundraiser
    primary key (pk) needs to be specified to update the required fundraiser
    full update
    '''
    def put(self, request, pk): 
        fundraiser = get_object_or_404(Fundraiser, pk=pk)

        ## trigger the auth check to see if the end user is the owner of the fundriaser
        self.check_object_permissions(request, fundraiser) 

        serializer = FundraiserDetailSerializer(
            instance=fundraiser,
            data=request.data,
            ## special Django option; this allows for some fields to be updated
            partial=True 
        )

        ## checking if the serializer is valid
        if serializer.is_valid():
            serializer.save()
            ## on success, return the response
            return Response(serializer.data)
        ## on failure, return error 400
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)

        ## trigger auth check to see if the end user is the fundraiser owner 
        self.check_object_permissions(request, fundraiser)

        ## change "is_deleted" attribute to True for soft deletion
        fundraiser.is_deleted = True
        fundraiser.save()

        ## soft deleted pledges in this fundraiser
        fundraiser.pledges.update(is_deleted=True)
        ## 204 means success with no content to return
        return Response(
            status=status.HTTP_204_NO_CONTENT
            )
            
    
class PledgesList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsEndUserActiveAndNotSoftDeleted,
        IsFundraiserSoftDeleted
    ]

    def get(self, request):
        ## show all the non soft-deleted pledges
        pledges = Pledge.objects.filter(is_deleted=False)
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        ## to serialise as json
        serializer = PledgeSerializer(data=request.data) 
        ## built in function is_valid - valid as json format
        if serializer.is_valid(): 
            ## call another function to save the data
            serializer.save(supporter=request.user) 
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
## show one pledge   
class PledgeDetail(APIView): 
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsEndUserActiveAndNotSoftDeleted,
        IsOwnerOrReadOnly
    ] 
    
    ## show one pledge that is not soft deleted, helper function get_object_or_404
    def get(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk, is_deleted=False) 
        serializer = PledgeSerializer(pledge) 
        return Response(serializer.data)
 
    
    def put(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk, is_deleted=False)
        self.check_object_permissions(request, pledge)
        serializer = PledgeSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
    )



    

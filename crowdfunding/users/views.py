from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
## import Fundraiser and Pledge models from the Fundraisers.models.py file
from fundraisers.models import Fundraiser, Pledge
from .serializers import CustomUserSerializer, CustomUserDetailSerializer
from .permissions import IsSelfOrReadOnly
from django.db import transaction

class CustomUserList(APIView):
  
    def get(self,request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() ## requesting that the logged in user is the owner.
            return Response(
                serializer.data, ## password is automatically taken out before reaching the API
                status=status.HTTP_201_CREATED
            )
        ## if response is invalid, return error 400
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSelfOrReadOnly
    ]
    def get(self, request, pk): ## the primary key (pk) is the ID ... /users/1
        ## print(CustomUser.objects.filter(id=pk))
        user = get_object_or_404(CustomUser,pk=pk)
        ## print(user)
        serializer = CustomUserSerializer(user) #serialize data for sending to APi
        return Response(serializer.data)

    ## put response is placed in customuserdetail class because it needs to refer to a specific user
    ## primary key (pk) needs to be specified to update the required user
    ## Full update
    def put(self, request, pk): 
        user = get_object_or_404(CustomUser, pk=pk)

        ## trigger the auth check to see if the end user is the owner of the user account
        self.check_object_permissions(request, user) 

        serializer = CustomUserDetailSerializer(
            instance=user,
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
    
    def delete (self, request, pk):
        user = get_object_or_404(CustomUser, pk = pk)

        ## trigger the auth check to see if the end user is the owner of the user account
        self.check_object_permissions(request, user) 

        ## execute the following all at once
        with transaction.atomic():

            ## soft delete fundraisers created by user account
            Fundraiser.objects.filter(
                owner=user
                ).update(is_deleted=True)

            ## soft delete corresponding pledges in the previously mentioned fundraisers
            Pledge.objects.filter(
                supporter=user,
                fundraiser__owner=user
                ).update(is_deleted=True)

            ## anonymise pledges this soon to be soft deleted end user to other fundraisers
            Pledge.objects.filter(
                supporter=user
                ).exclude(
                fundraiser__owner=user
                ).update(anonymous=True)

            ## soft delete this end user
            user.is_deleted = True
            user.is_active = False
            user.save()

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] #pluck out the user
        token, created = Token.objects.get_or_create(user=user) #get existing token or create new token

        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })
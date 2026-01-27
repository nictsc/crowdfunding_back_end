from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer

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
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CustomUserDetail(APIView):
    def get(self, request, pk): ## the primary key (pk) is the ID ... /users/1
        user = get_object_or_404(CustomUser,pk) 
        serializer = CustomUserSerializer(user) #serialize data for sending to APi
        return Response(serializer.data)

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
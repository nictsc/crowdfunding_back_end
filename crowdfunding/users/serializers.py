from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: ## shortform for Metadata; it gives you options to configure your metadata.
        model = CustomUser
        exclude = ('user_permissions', 'is_staff', 'groups', 'date_joined', 'is_active', 'last_login',)
        extra_kwargs = {'password': {'write_only': True}} #kwargs = keyword arguments, this means we are passing passwords are write only. we are going to be gonna be accepting passwords in and not sending passwords out to the API for security risks.

    def create(self, validated_data): ## override the default behaviour
        return CustomUser.objects.create_user(**validated_data) ## passing the json data
    
class CustomUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
    def delete(self, instance, validated_data):
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)

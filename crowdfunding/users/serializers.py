from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: ## shortform for Metadata; it gives you options to configure your metadata.
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}} #kwargs = keyword arguments, this means we are passing passwords are write only. we are going to be gonna be accepting passwords in and not sending passwords out to the API for security risks.

    def create(self, validated_data): ## override the default behaviour
        return CustomUser.objects.create_user(**validated_data) ## passing the json data
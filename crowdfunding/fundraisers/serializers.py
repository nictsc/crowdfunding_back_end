## declare syour dependencies
from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.id') ## treat it as read only attribute and assign it to the owner.
   class Meta:
       model = apps.get_model('fundraisers.Fundraiser')
       exclude = ('is_deleted',)

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
       model = apps.get_model('fundraisers.Pledge')
       exclude = ('is_deleted',)

# Add the nested serializer
class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True) #serialize all the records, the end user can only read the end point.

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.goal)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
    
    def delete(self, instance, validated_data):
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
## declare syour dependencies
from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.id') ## treat it as read only attribute and assign it to the owner.
   class Meta:
       model = apps.get_model('fundraisers.Fundraiser')
       fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
       model = apps.get_model('fundraisers.Pledge')
       fields = '__all__'

# Add the nested serializer
class FundraiserDetailSerializer(FundraiserSerializer):
  pledges = PledgeSerializer(many=True, read_only=True) #serialize all the records, the end user can only read the end point.

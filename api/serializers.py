from rest_framework import serializers
from api.models import Company


# create serializer for company model
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
from rest_framework import serializers
from api.models import Company, Employee


# create serializer for company model
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()# this only for display purpose
    class Meta:
        model = Company
        fields = '__all__'
# this for emoployee serializer models selializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.ReadOnlyField() # this only for display purpose
    class Meta:
        model = Employee
        fields = '__all__'
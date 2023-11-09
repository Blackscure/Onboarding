from onboard.models import Business, Customer, Location
from rest_framework import serializers
 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()
    class Meta:
        model = Business
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
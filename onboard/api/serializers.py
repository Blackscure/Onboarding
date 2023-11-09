
from rest_framework import serializers

from onboard.models import Customer
 
class CustomerSerializer(serializers.ModelSerializer):
    age_of_business = serializers.SerializerMethodField()

    def get_age_of_business(self, obj):
        from datetime import date
        today = date.today()
        return today.year - obj.business_registration_date.year

    class Meta:
        model = Customer
        fields = '__all__'

from django.db.models import Q
from onboard.api.serializers import BusinessSerializer, CustomerSerializer, LocationSerializer
from onboard.models import Business, Customer, Location
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
 
class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
            try:
                # Validate if customer with the same phone or email already exists
                phone = request.data.get('phone')
                email = request.data.get('email')

                if Customer.objects.filter(Q(phone=phone) | Q(email=email)).exists():
                    return Response({"detail": "Customer with the same phone or email already exists."}, status=status.HTTP_400_BAD_REQUEST)

                # If not, proceed to create the customer
                serializer = CustomerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"detail": "Customer created successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            customer = self.get_object(pk)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Customer updated successfully.", "data": serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, pk):
            try:
                customer = self.get_object(pk)
                customer.delete()
                return Response({"detail": "Customer deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BusinessListView(APIView):
    def get(self, request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    def post(self, request):
            try:
                # Check if a business with the same name already exists
                name = request.data.get('name')
                if Business.objects.filter(name=name).exists():
                    return Response({"detail": "A business with the same name already exists."}, status=status.HTTP_400_BAD_REQUEST)

                serializer = BusinessSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"detail": "Business created successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BusinessDetailView(APIView):
    def get_object(self, pk):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        business = self.get_object(pk)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)
    
    def put(self, request, pk):
            try:
                business = self.get_object(pk)
                serializer = BusinessSerializer(business, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"detail": "Business updated successfully.", "data": serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
                try:
                    business = self.get_object(pk)
                    business.delete()
                    return Response({"detail": "Business deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
                except Exception as e:
                    return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocationListView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            # Check if a location with the same details already exists
            customer_id = request.data.get('customer')
            county = request.data.get('county')
            sub_county = request.data.get('sub_county')
            ward = request.data.get('ward')
            building_name = request.data.get('building_name')
            floor = request.data.get('floor')

            if Location.objects.filter(
                customer=customer_id,
                county=county,
                sub_county=sub_county,
                ward=ward,
                building_name=building_name,
                floor=floor
            ).exists():
                return Response({"detail": "A location with the same details already exists."}, status=status.HTTP_400_BAD_REQUEST)

            serializer = LocationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Location created successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LocationDetailView(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk):
            try:
                location = self.get_object(pk)
                serializer = LocationSerializer(location, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"detail": "Location updated successfully.", "data": serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
            try:
                location = self.get_object(pk)
                location.delete()
                return Response({"detail": "Location deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
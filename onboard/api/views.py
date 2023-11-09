from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from onboard.models import Customer
from .serializers import CustomerSerializer

class CustomerAPIView(APIView):
    # Get all customers
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
        
    # Create a new customer
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            # Check if data already exists
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            if Customer.objects.filter(name=name, email=email).exists():
                return Response({"error": "Customer with this name and email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the new customer
            serializer.save()
            return Response({"message": "Customer created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get details of a specific customer
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update details of a specific customer
    def put(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Customer updated successfully", "data": serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

    # Delete a specific customer
    def delete(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            customer.delete()
            return Response({"message": "Customer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

from django.urls import path

from onboard.api.views import CustomerAPIView
 


urlpatterns = [
    path('customers/', CustomerAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerAPIView.as_view(), name='customer-detail'),
    
]
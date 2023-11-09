from django.urls import path

from onboard.api.views import BusinessDetailView, BusinessListView, CustomerDetailView, CustomerListView, LocationDetailView, LocationListView


urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('businesses/', BusinessListView.as_view(), name='business-list'),
    path('businesses/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    path('locations/', LocationListView.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
]
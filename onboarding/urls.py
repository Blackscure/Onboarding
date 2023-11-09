from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
       title="Onboarding API",
       default_version='v1',
       description="Onboarding Customers and Business",
       terms_of_service="",
       contact=openapi.Contact(email="Wekesabuyahi@gmail.com"),
       license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('apps/onboard/api/v1/', include('onboard.api.urls')),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/onboard/api/v1/', include('onboard.api.urls')),
]

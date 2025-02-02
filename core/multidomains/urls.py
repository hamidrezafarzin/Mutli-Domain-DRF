from django.urls import path, include

app_name = "multidomains"

urlpatterns = [
    # template base authentication
    # path('', include('django.contrib.auth.urls')),
    # api based authentication
    path("api/v1/", include("multidomains.api.v1.urls"))
]

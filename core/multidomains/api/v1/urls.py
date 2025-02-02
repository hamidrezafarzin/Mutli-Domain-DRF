from django.urls import path
from .views import DomainViewSet
from rest_framework.routers import DefaultRouter


app_name = "api-v1"
router = DefaultRouter()

urlpatterns = []


router.register(r'domains', DomainViewSet, basename='domain')

urlpatterns += router.urls
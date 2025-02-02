from django.urls import path
from .views import RegisterModelViewSet, ProfileModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


app_name = "api-v1"

urlpatterns = [
    path("register/", RegisterModelViewSet.as_view({"post": "create"}), name="register"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    path(
        "user/profile/",
        ProfileModelViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update", "put": "update"}
        ),
        name="profile",
    ),
]

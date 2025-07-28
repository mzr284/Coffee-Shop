from django.urls import path
from .views import  UserGetCode, UserRegister #, UserListView, UserDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path("users/", UserListView.as_view(), name="all-users"),
    # path("users/<str:username>/", UserDetail.as_view(), name="user-detail"),
    path("get-code/", UserGetCode.as_view(), name="get code"),
    path("register/", UserRegister.as_view(), name="user register"),
    path("users/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
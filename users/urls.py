from django.urls import path
from .views import UserListView, UserDetail, UserGetCode, UserRegister

urlpatterns = [
    path("users/", UserListView.as_view(), name="all-users"),
    path("users/<str:username>/", UserDetail.as_view(), name="user-detail"),
    path("get-code/", UserGetCode.as_view(), name="get code"),
    path("register/", UserRegister.as_view(), name="user register")
]
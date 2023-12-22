from django.urls import path
from .views import (
    HOMEPAGE,
    PostDetails,
    SignUpView,
    ProfileView,
    PostCreateView,
    PostUpdateView,
    Public_User_View,
    PostDeleteView,
    CategoryView,
)


urlpatterns = [
    path("", HOMEPAGE.as_view(), name="home"),
    path("post/<int:pk>/", PostDetails.as_view(), name="postdetail"),
    path("category/<str:category>/", CategoryView.as_view(), name="CategoryView"),
    path("register/", SignUpView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("user/<str:author>/", Public_User_View.as_view(), name="PublicUser"),
    path("profile/create/", PostCreateView.as_view(), name="createPost"),
    path("profile/update/<int:pk>", PostUpdateView.as_view(), name="updatePost"),
    path("profile/delete/<int:pk>", PostDeleteView.as_view(), name="deletePost"),
    # path("profile/setting/<int:pk>", Setting.as_view(), name="Setting"),
]

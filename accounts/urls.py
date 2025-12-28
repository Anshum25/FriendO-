from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("main/", views.main, name="main"),
    path("profile/", views.profile, name="profile"),
    path("profile-setup/", views.profile_setup, name="profile_setup"),
    path("search/", views.search_results, name="search_results"),
    path("user/<str:username>/", views.user_profile, name="user_profile"),
    path("search-user/", views.search_user, name="search_user"),
]

from django.urls import path

from users.views import SignUpView, LoginView, ProfileView, UpdateProfile, DeleteProfile, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:id>/', ProfileView.as_view(), name='profile'),
    path('profile/update/<int:id>/', UpdateProfile.as_view(), name='profile_update'),
    path('profile/delete/<int:id>/', DeleteProfile.as_view(), name='profile_delete'),
    path('profile/logout/<int:id>/', LogoutView.as_view(), name='profile_logout'),
]
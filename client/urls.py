from django.urls import path
from .views import RegisterUser, LoginUser, logout_user


urlpatterns = [
    path('create_user/', RegisterUser.as_view(), name='create_user'),
    path('sign_in/', LoginUser.as_view(), name='auth_user'),
    path('logout/', logout_user, name='logout')
]
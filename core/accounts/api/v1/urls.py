from django.urls import path, include
# from .views import Postlist
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api/v1'
#+======================================================================+
urlpatterns = [
    # registration
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
    # change password
    path('token/login/',views.ObtainAuthToken.as_view(), name='token-login'),
    # reset password
    path('token/logout/',views.CustomDisgardAuthTokenView.as_view(), name='token-logout'),
    # login token
    # login jwt


]


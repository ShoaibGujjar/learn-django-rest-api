from django.urls import URLPattern, path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('auth/',obtain_auth_token),
    path('', views.get),
]
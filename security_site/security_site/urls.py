
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from app.views import protected_view

urlpatterns = [
    path('api/token/', obtain_auth_token, name='obtain_token'),
    path('teste/', protected_view),
    path('admin/', admin.site.urls),
]

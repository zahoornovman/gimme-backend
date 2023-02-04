"""gimme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from custom_jwt_token.views import CustomObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/api/auth/token/', CustomObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('backend/api/auth/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),
    path('backend/api/wants/', include('want.urls')),
    path('backend/api/want_image/', include('want_image.urls')),
    path('backend/api/haves/', include('have.urls')),
    path('backend/api/have_image/', include('have_image.urls')),
    path('backend/api/user/', include('user_profile.urls')),
    path('backend/api/message/', include('message.urls')),
    path('backend/api/tags/', include('tag.urls')),

]

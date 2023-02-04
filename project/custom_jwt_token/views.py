from rest_framework_simplejwt.views import TokenObtainPairView

from custom_jwt_token.serializers import CustomTokenObtainPairSerializer


class CustomObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

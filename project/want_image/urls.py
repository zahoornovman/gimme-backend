from django.urls import path

from want_image.views import WantImageViewSet

urlpatterns = [
    path('<int:pk>/', WantImageViewSet.as_view()),
]

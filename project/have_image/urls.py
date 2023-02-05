from django.urls import path

from have_image.views import HaveImageDeleteView

urlpatterns = [
    path('<int:pk>/', HaveImageDeleteView.as_view()),
]

from django.urls import path

from user_profile.views import RetrieveUpdateView

urlpatterns = [
    path('me/', RetrieveUpdateView.as_view()),
]
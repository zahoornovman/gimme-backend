from django.urls import path

from user_profile.views import RetrieveUpdateDeleteUserProfileView

urlpatterns = [
    path('me/', RetrieveUpdateDeleteUserProfileView.as_view()),
]
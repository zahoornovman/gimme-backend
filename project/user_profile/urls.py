from django.urls import path

from user_profile.views import RetrieveUpdateView, GetSpecificUserView

urlpatterns = [
    path('<int:userprofile__id>/', GetSpecificUserView.as_view()),
    path('me/', RetrieveUpdateView.as_view()),
]
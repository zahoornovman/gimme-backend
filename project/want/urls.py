from django.urls import path

from want.views import ListAllWants, ListAndCreateWantsForLoggedInUser

urlpatterns = [
    path('', ListAllWants.as_view()),
    path('me/', ListAndCreateWantsForLoggedInUser.as_view())
]

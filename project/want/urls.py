from django.urls import path

from want.views import ListAllWantsView, ListAndCreateWantsForLoggedInUserView, RetrieveUpdateDeleteWantView

urlpatterns = [
    path('', ListAllWantsView.as_view()),
    path('me/', ListAndCreateWantsForLoggedInUserView.as_view()),
    path('<int:pk>/', RetrieveUpdateDeleteWantView.as_view()),
]

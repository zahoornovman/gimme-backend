from django.urls import path

from have.views import ListAllHavesView, ListAndCreateHavesForLoggedInUserView, RetrieveUpdateDeleteHaveView

urlpatterns = [
    path('', ListAllHavesView.as_view()),
    path('me/', ListAndCreateHavesForLoggedInUserView.as_view()),
    path('<int:pk>/', RetrieveUpdateDeleteHaveView.as_view()),
]

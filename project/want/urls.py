from django.urls import path

from want.views import ListAllWants

urlpatterns = [
    path('', ListAllWants.as_view()),
]

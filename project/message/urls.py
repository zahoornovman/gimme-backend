from django.urls import path

from message.views import ListCreateMessageView

urlpatterns = [
    path('', ListCreateMessageView.as_view()),
]
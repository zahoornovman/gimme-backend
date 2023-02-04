from django.urls import path

from tag.views import ListTagsView

urlpatterns = [
    path('', ListTagsView.as_view()),
]
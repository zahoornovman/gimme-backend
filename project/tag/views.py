from django.shortcuts import render
from rest_framework.generics import ListAPIView

from tag.models import Tag
from tag.serializers import TagSerializer


# List all tags

class ListTagsView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []
    pagination_class = None

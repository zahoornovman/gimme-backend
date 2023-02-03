from django.shortcuts import render
from rest_framework.generics import ListAPIView

from tag.models import Tag
from tag.serializers import TagSerializer


# Create your views here.

class ListTagsView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

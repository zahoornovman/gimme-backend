from django.shortcuts import render
from rest_framework.generics import ListAPIView

from want.models import Want
from want.serializers import WantSerializer


# Create your views here.


class ListAllWants(ListAPIView):
    queryset = Want.objects.all().order_by('-created_time')
    serializer_class = WantSerializer
    permission_classes = []

    def get_queryset(self):
        return Want.objects.all()



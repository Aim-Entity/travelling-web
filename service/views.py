from django.shortcuts import render
from .models import Location
from .serializers import LocationSerializers
from rest_framework import viewsets


def index(request):
    return render(request, "service/index.htm", {})


class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers

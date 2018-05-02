from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Anime, Breed, Website
from .serializers import BlogSerializer, TagSerializer, CategorySerializer, CommentSerializer, PostSerializer 

class AnimeViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, request):
      queryset = Anime.objects.all()
      serializer = AnimeSerializer(queryset, many=True)
      return Response(serializer.data)


class BreedViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
      queryset = Breed.objects.all()
      serializer = BreedSerializer(queryset, many=True)
      return Response(serializer.data)


class WebsiteViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
      queryset = Website.objects.all()
      serializer = WebsiteSerializer(queryset, many=True)
      return Response(serializer.data)

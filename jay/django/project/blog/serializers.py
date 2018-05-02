from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Anime, Breed, Website

class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ('title', 'description', 'director', 'release_date', 'score','picture')

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ('name', 'description', 'country', 'is_official')

class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ('name', 'link', 'owner', 'logo')


from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Tag, Category, Comment, Post
from .serializers import TagSerializer, CategorySerializer, CommentSerializer, PostSerializer 


class TagViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

class PostViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
        queryset = Post.objects.all()
        serializer_context = {'request': request,}
        serializer = PostSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            for tag in request.data.get('tags'):
                t = Tag.objects.get(id=tag)
                post.tags.add(t)
            return Response(serializer.data)
        return Response(serializer.errors)

    def get_tags(self, *args, **kwargs):
        tags = Tags.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Post.objects.all()
        except Post.DoesNotexist:
            raise Http404

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer_context = {'request': request}
        serializer = PostSerializer(post, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
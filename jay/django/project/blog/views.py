from blog.models import Post
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog, Tag, Category, Comment, Post
from blog.serializers import BlogSerializer, TagSerializer, CategorySerializer, CommentSerializer, PostSerializer 


class BlogViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, request):
      queryset = Blog.objects.all()
      serializer = BlogSerializer(queryset, many=True)
      return Response(serializer.data)

    def retrieve(self, request, pk=None):
      queryset = Blog.objects.all()
      blog = get_object_or_404(queryset, pk=pk)
      serializer = BlogSerializer(blog)
      return Response(serializer.data)

class TagViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
      queryset = Tag.objects.all()
      serializer = TagSerializer(queryset, many=True)
      return Response(serializer.data)

    def retrieve(self, request, pk=None):
      queryset = Tag.objects.all()
      tag = get_object_or_404(queryset, pk=pk)
      serializer = TagSerializer(tag)
      return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
      queryset = Category.objects.all()
      serializer = CategorySerializer(queryset, many=True)
      return Response(serializer.data)

    def retrieve(self, request, pk=None):
      queryset = Category.objects.all()
      category = get_object_or_404(queryset, pk=pk)
      serializer = CategorySerializer(category)
      return Response(serializer.data)


class CommentViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
      queryset = Comment.objects.all()
      serializer = CommentSerializer(queryset, many=True)
      return Response(serializer.data)

    def retrieve(self, request, pk=None):
      queryset = Comment.objects.all()
      comment = get_object_or_404(queryset, pk=pk)
      serializer = CommentSerializer(comment)
      return Response(serializer.data)


class PostViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def list(self, request):
      queryset = Post.objects.all()
      serializer = PostSerializer(queryset, many=True)
      return Response(serializer.data)

    def create(self, request):
      queryset = Blog.objects.all()
      serializer = BlogSerializer(queryset, many=True)
      return Response(serializer.data)

    def retrieve(self, request, pk=None):
      queryset = Post.objects.all()
      post = get_object_or_404(queryset, pk=pk)
      serializer = PostSerializer(post)
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
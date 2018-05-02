from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Blog, Tag, Category, Comment, Post

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('heading',
        'sub_heading')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',
        'date_created',
        'date_modified')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',
        'date_created',
        'date_modified')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post',
        'date_created',
        'author',
        'text')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title',
        'subtitle',
        'banner_photo',
        'blog',
        'date_created',
        'date_modified',
        'tags',
        'category',
        'body',
        'status')


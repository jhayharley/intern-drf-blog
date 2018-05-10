from rest_framework import serializers
from .models import Tag, Category, Comment, Post
from django.utils.timesince import timesince


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'title',
            'date_created',
            'date_modified'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'date_created',
            'date_modified'
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post',
            'date_created',
            'author',
            'text'
        )

class PostSerializer(serializers.ModelSerializer):
    #tags = serializers.StringRelatedField(many=True)
    date_display = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'title',
            'subtitle',
            'banner_photo',
            'date_created',
            'category_name',
            'date_modified',
            'tags',
            'category',
            'body',
            'status',
            'date_display',
            'timesince'
        )

    def get_category_name(self, instance):
        return instance.category.title

    def get_date_display(self, instance):
        return instance.date_created.strftime("%b d%, %Y | at %I %M %p")

    def get_timesince(self, instance):
        return timesince(instance.date_modified) + "ago"
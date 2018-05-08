from rest_framework import serializers
from .models import Blog, Tag, Category, Comment, Post
from django.utils.timesince import timesince

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'heading',
            'sub_heading'
        )

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
#    blog_name = serializers.SerializerMethodField()
    date_display = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
#    tags = TagSerializer(Tag, many=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'subtitle',
            'banner_photo',
            'blog',
#            'blog_name',
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

#    def get_blog_name(self, instance):
#        return instance.blog.heading

    def get_date_display(self, instance):
        return instance.date_created.strftime("%b d%, | at %M %p")

    def get_timesince(self, instance):
        return timesince(instance.date_modified) + "ago"
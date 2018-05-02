from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        eclude = ('post','author',)
        fields = ('text',)

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
            'subtitle',
            'banner_photo',
            'blog',
            'category',
            'body', 
            'status',)

class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
            'subtitle',
            'banner_photo',
            'blog',
            'category',
            'body', 
            'status',)
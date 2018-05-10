import re

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Count
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage

# Create your models here.

class TagManager(models.Manager):
    def most_popular(self, count=5):
        return self.annotate(num_posts=Count("post"))
        order_by("-num_posts")[:count]

tag_pattern = re.compile(r'^[\w.@ +-]+$',)
def validate_tag_name(title):
    if not tag_pattern.search(title):
        raise ValidationError("not a valid tag title")

class Tag(models.Model):
    title            = models.CharField(max_length=120, validators=[validate_tag_name])
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now=True)
    objects = TagManager()

    def __str__(self):
        return '{}'.format(self.title)

class Category(models.Model):
    title            = models.CharField(max_length=120)
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class Comment(models.Model):
    post             = models.ForeignKey('Post', on_delete=models.CASCADE)
    date_created     = models.DateTimeField(auto_now_add=True)
    author           = models.CharField(max_length=120)
    text             = models.TextField()

    def __str__(self):
        return '{}'.format(self.text)

STATUS_CHOICES = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('archive', 'Archive')
)

class PostManager(models.Manager):
    def filter_by_tags(self, tag_list=[], count=10):
        qs = self.all()
        for tag in tag_list:
            qs = qs.filter(tags__name=tag)
        if count:
            qs = qs[:count]
        return qs

class Post(models.Model):
    title            = models.CharField(max_length=200)
    subtitle         = models.CharField(max_length=200)
    banner_photo     = VersatileImageField('Image', upload_to = 'static/media')
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now_add=True)
    tags             = models.ManyToManyField("Tag", related_name="tags")
    category         = models.ForeignKey('Category', on_delete=models.CASCADE,)
    body             = models.TextField()
    status           = models.CharField(max_length=9, choices=STATUS_CHOICES, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.title)
    objects = PostManager()

    def tag_list(self):
        qs = self.tags.value_list("title", flat=True)
        if qs:
            return ",".join(qs)
        else:
            return ""
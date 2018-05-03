from django.db import models

# Create your models here.
class Blog(models.Model):
    heading          = models.CharField(max_length=120)
    sub_heading      = models.CharField(max_length=120)

    def __str__(self):
        return '{}'.format(self.heading)

class Tag(models.Model):
    title            = models.CharField(max_length=120)
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now=True)

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

class Post(models.Model):
    title            = models.CharField(max_length=120)
    subtitle         = models.CharField(max_length=120)
    banner_photo     = models.ImageField(upload_to = 'static/media')
    blog             = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now_add=True)
    tags             = models.ManyToManyField("Tag", related_name="tags")
    category         = models.ForeignKey('Category', on_delete=models.CASCADE,)
    body             = models.TextField()
    status           = models.CharField(max_length=9, choices=STATUS_CHOICES, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.title)
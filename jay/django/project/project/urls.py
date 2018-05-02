from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from blog import views
from blog.views import BlogViewSet, TagViewSet, CategoryViewSet, CommentViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet, base_name='blogs')
router.register(r'tags', TagViewSet, base_name='tags')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'comments', CommentViewSet, base_name='comments')
router.register(r'posts', PostViewSet, base_name='posts')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 ]
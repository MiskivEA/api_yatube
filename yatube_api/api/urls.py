from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register(r'api/v1/posts/(?P<post_id>.+)/comments',
                CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls))
]

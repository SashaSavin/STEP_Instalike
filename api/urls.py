from django.urls import include, path
from rest_framework import routers
from .viewsets import UserViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include((router.urls, 'api'), namespace='api')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
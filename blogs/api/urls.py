from rest_framework import routers
from blogs.api.viewsets import BlogViewSet

router = routers.DefaultRouter()
router.register('blogs/', BlogViewSet, 'blogs')

urlpatterns = router.urls

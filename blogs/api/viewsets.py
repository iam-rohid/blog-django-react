from rest_framework import viewsets, permissions
from blogs.models import Blog
from blogs.api.serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BlogSerializer

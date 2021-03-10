from rest_framework import viewsets
from blogs import models
from . import serializers


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BlogPostSerializer
    queryset = models.BlogPost.objects.all()

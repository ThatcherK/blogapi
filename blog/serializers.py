from rest_framework.serializers import ModelSerializer
from .models import Blog, Comment
from rest_framework import fields,serializers

class BlogSerializer(ModelSerializer):
    picture = serializers.ImageField(required=False)
    class Meta:
        model=Blog
        fields=['title', 'body', 'picture', 'user', 'likes', 'created_date']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['blog','author', 'comment', 'created_date']


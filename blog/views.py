from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateAPIView
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

class Blogs(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class Comments(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer





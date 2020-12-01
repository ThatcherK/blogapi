from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateAPIView
from .models import Blog
from .serializers import BlogSerializer

class Blogs(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer





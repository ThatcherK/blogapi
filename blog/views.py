from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .models import Blog, Comment, Profile
from .serializers import BlogSerializer, CommentSerializer, ProfileSerializer
from .permissions import IsOwnerOrReadOnly

class BlogView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        post_data = request.data
        post_data['user'] = request.user.id
        # title = post_data.get('title')
        # body = post_data.get('body')
        # picture = post_data.get('picture')
        # user = request.user.id
        # data = {}
        # if picture:
        #     data = {
        #         'title': title,
        #         'body': body,
        #         'picture': picture,
        #         'user': user
        #     }
        # data = {
        #         'title': title,
        #         'body': body,
        #         'user': user
        #     }
        serializer = BlogSerializer(data=post_data)
        print(post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = BlogSerializer
    lookup_url_kwarg = 'blog_id'

class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def patch(self,request,user_id):
        post_data = request.data
        bio = post_data.get('bio')
        profile_picture = post_data.get('profile_picture')
        user = User.objects.get(pk=user_id)
        user.profile.bio = bio
        user.profile.profile_picture = profile_picture
        data = {
            'user': user_id,
            'profile_picture': profile_picture,
            'bio': bio
        }
        serializer = ProfileSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikesView(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def patch(self, request, blog_id):
        post_data = request.data
        user = post_data.get('user_id')
        blog = Blog.objects.get(pk=blog_id)
        blog.likes.set(user)
        # data = {
        #     'user': user,
        # }
        serializer = BlogSerializer(blog)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





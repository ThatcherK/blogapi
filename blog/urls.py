from django.urls import path
from .views import BlogView, CommentView, ProfileView, LikesView, BlogUpdateView

urlpatterns = [
    path('blogs/', BlogView.as_view()),
    path('comments/', CommentView.as_view()),
    path('profile/<int:user_id>/', ProfileView.as_view()),
    path('like/<int:blog_id>/', LikesView.as_view()),
    path('update/<int:blog_id>/', BlogUpdateView.as_view())
]
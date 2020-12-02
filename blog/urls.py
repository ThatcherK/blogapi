from django.urls import path
from .views import Blogs, Comments

urlpatterns = [
    path('add_blog/', Blogs.as_view()),
    path('comments/', Comments.as_view())
]
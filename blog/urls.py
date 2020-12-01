from django.urls import path
from .views import Blogs

urlpatterns = [
    path('blog/', Blogs.as_view()),
]
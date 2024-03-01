from blog.views import post_list
from django.urls import path

from .views import PostDetailView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]

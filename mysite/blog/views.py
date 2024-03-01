from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request,
                  'post/list.html',
                  {'posts': posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

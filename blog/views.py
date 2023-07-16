from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect

# Create your views here.

def blog_list(request):
    post = Post.objects.all()
    context = {
        "blog_list":post
    }

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, id):
    each_post = Post.objects.get(id=id)
    context = {
       "blog_detail": each_post
    }
    return render(request, "blog/blog_detail.html", context)


def blog_delete(request, id):
    each_post = Post.objects.get(id=id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')
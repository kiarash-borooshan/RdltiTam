from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    return HttpResponse("hi")


def post_list(request):
    # ol = get_object_or_404(Post) # فقط برای تک آبجکت بکار می‌رود
    # ol = Post.published.all()
    # ol = Post.objects.y(2020)
    # ol = Post.objects.filter(publish__year="2024")
    # ol = Post.objects.filter(status="published")
    ol = Post.objects.all()
    print("&&&&&&", ol)
    pagination = Paginator(ol, 2)
    page = request.GET.get("page")

    try:
        post = pagination.page(page)
    except EmptyPage:
        post = pagination.page(1)
    except PageNotAnInteger:
        post = pagination.page(pagination.num_pages)

    return render(request,
                  "post/post_list.html",
                  {"posts": ol})


def post_detail(request, pk, slug):
    # post = Post.objects.get(pk=pk, slug=slug)
    post = get_object_or_404(Post, pk=pk, slug=slug)
    return render(request,
                  "post/post_detail.html",
                  {"post": post})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


def index(request):
    return HttpResponse("hi")


# def post_list(request):
#     # ol = get_object_or_404(Post) # فقط برای تک آبجکت بکار می‌رود
#     # ol = Post.published.all()
#     # ol = Post.objects.y(2020)
#     # ol = Post.objects.filter(publish__year="2024")
#     # ol = Post.objects.filter(status="published")
#     ol = Post.objects.all()
#
#     pagination = Paginator(ol, 2)
#     page = request.GET.get("page")
#
#     try:
#         posts = pagination.page(page)
#     except EmptyPage:
#         posts = pagination.page(1)
#     except PageNotAnInteger:
#         posts = pagination.page(pagination.num_pages)
#
#     return render(request,
#                   "post/post_list.html",
#                   {"posts": posts})


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2
    template_name = "post/post_list.html"


def post_detail(request, pk, slug):
    # post = Post.objects.get(pk=pk, slug=slug)
    post = get_object_or_404(Post, pk=pk, slug=slug)
    return render(request,
                  "post/post_detail.html",
                  {"post": post})

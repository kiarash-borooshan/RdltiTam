from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import AccountForm
from .models import Post, Account


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


def account_form(request, *args, **kwargs):
    user = request.user
    # account = kwargs.get(pk=user)
    try:
        account = Account.objects.get(user=user)
    except:
        account = Account.objects.create(user=user)

    if not user.is_authenticated:
        return redirect("blog:index")

    if request.method == "POST":
        form = AccountForm(data=request.POST)
        if form.is_valid():

            cd = form.cleaned_data

            account.gender = cd["gender"]
            account.address = cd["address"]

            user.first_name = cd["first_name"]
            user.last_name = cd["last_name"]

            user.save()
            account.save()

            return redirect("/")

    else:
        form = AccountForm(initial={
            "first_name": account.user.first_name,
            "last_name": account.user.last_name,
            "phone": account.phone,
            "address": account.address,
        })
        return render(request,
                      "forms/account_form.html",
                      {"form": form})

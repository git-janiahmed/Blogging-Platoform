from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    UpdateView,
    CreateView,
    DetailView,
    View,
    FormView,
)
from django.shortcuts import render

from .models import Post, Category, User_profile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.detail import SingleObjectMixin
from .forms import CommentForm

# Create your views here.


class HOMEPAGE(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context


class CategoryView(ListView):
    model = Post
    template_name = "CategoryView.html"
    context_object_name = "posts"

    def get_queryset(self):
        Category_FromURL = self.kwargs.get("category")
        Cate = get_object_or_404(Category, name=Category_FromURL)
        User_posts = Post.objects.filter(category=Cate)
        return User_posts


class ForCommentGet(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class ForCommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):  # new
    login_url = reverse_lazy("login")
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def form_valid(self, form):
        get_comment_data = form.save(commit=False)
        get_comment_data.title = self.get_object()
        get_comment_data.author = self.request.user
        get_comment_data.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("postdetail", kwargs={"pk": post.pk})


class PostDetails(View):
    def get(self, request, **kwargs):
        view = ForCommentGet.as_view()
        # print(*args, kwargs["pk"])
        return view(request, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ForCommentPost.as_view()
        return view(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")


class Public_User_View(ListView):
    template_name = "publicUser.html"
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get("author")
        user = get_object_or_404(User, username=username)
        context["posts"] = Post.objects.filter(author=user)
        context["profile"] = User_profile.objects.filter(username=user)

        return context


class ProfileView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Post
    template_name = "User/main.html"
    context_object_name = "posts"

    def get_queryset(self):
        # Only return posts of the logged-in user
        return Post.objects.filter(author=self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")

    model = Post
    template_name = "User/create_post.html"
    fields = ["title", "description", "image", "content", "category"]
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Post
    template_name = "user/update_post.html"
    fields = ["title", "description", "image", "content", "category"]
    success_url = reverse_lazy("profile")


class Update_Profile(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    model = User_profile
    template_name = "user/update_profile.html"
    fields = ["about", "image", "email"]
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class Update_Profile(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = User_profile
    template_name = "user/create_profile.html"
    fields = ["about", "image", "email"]
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    model = Post
    template_name = "user/delete_post.html"
    success_url = reverse_lazy("profile")

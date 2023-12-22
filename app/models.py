from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User_profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField()
    image = models.ImageField(upload_to="templates/static/uploads/")
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    description = models.TextField()
    image = models.FileField(upload_to="templates/static/uploads/")
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    content = RichTextField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return reverse("postdetail", kwargs={"pk": self.pk})


class Comment(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    def get_absolute_urls(self):
        return reverse("post_details")

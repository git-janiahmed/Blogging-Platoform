from django.contrib import admin
from .models import Post, Comment, Category, User_profile

# Register your models here.


class WithComment(admin.StackedInline):
    model = Comment
    extra = 0


class AdminNew(admin.ModelAdmin):
    inlines = [WithComment]


admin.site.register(User_profile)
admin.site.register(Comment)
admin.site.register(Post, AdminNew)
admin.site.register(Category)

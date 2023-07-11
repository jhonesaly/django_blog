from django.contrib import admin
from app_blog.models import Post, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']

admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
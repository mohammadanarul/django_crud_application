from django.contrib import admin
from .models import Post

class post_model_admin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'updated_at')

admin.site.register(Post, post_model_admin)

from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "-created_at"
    empty_value_display = "-empty-"
    list_display = ("title", "counted_views", "status", "published_date")

admin.site.register(Post, PostAdmin)
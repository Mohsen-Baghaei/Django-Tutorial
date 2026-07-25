from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(default="fallback.png", blank=True)
    # author
    title = models.CharField(max_length=250)
    content = models.TextField()
    # tags
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
    
from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField()
    # author
    title = models.CharField(max_length=250)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پست"
        verbose_name = "پست ها"

    def __str__(self) -> str:
        return self.title
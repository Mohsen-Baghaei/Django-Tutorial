from django.contrib import admin
from .models import Contact

# Register your models here.
class Contactadmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_date")
    date_hierarchy = "created_date"
    list_filter = ("email",)
    search_fields = ("name", "message")

admin.site.register(Contact, Contactadmin)
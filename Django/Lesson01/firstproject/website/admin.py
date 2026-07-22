from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "create_date")
    date_hierarchy = "create_date"
    list_filter = ("email",)
    search_fields = ("name", "message")

admin.site.register(Contact, ContactAdmin)
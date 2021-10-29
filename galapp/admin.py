from django.contrib import admin
from .models import Picture


@admin.register(Picture)
class AuthorAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Demo

# Register your models here.
@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'body']

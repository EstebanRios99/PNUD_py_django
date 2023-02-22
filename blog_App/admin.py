from django.contrib import admin

# Register your models here.
from .models import news, category

admin.site.register(news)
admin.site.register(category)

from django.contrib import admin
from .models import Article
# Register your models to the admin site here.
# so the Article is registered to the admin site
admin.site.register(Article)

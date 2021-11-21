from django.contrib import admin
from .models import ArticleColumn
from .models import ArticlePost

# 註冊文章Post到admin中
admin.site.register(ArticlePost)

# 註冊文章欄目
admin.site.register(ArticleColumn)
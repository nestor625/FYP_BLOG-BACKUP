# 引入表單類
from django import forms
# 引入文章
from .models import ArticlePost

# 寫文章的表單類
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明數據模型來源
        model = ArticlePost
        # 定義表單包含的字段
        fields = ('title', 'body')
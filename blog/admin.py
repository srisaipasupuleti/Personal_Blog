from django.contrib import admin
from .models import Article, Tag

# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title"]
    filter_horizontal = ["tags"]
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
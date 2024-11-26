from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    date_published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="articles")
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    disliked_by = models.ManyToManyField(User, related_name='disliked_comments', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    def __str__(self):
        return f"Commented by {self.user.username} on {self.article.title}"
    
    def likes_count(self):
        return self.liked_by.count()

    def dislikes_count(self):
        return self.disliked_by.count()
    
    class Meta:
        ordering = ['-date'] # Orders comments by date(newest first)
    


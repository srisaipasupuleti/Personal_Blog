from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    def __str__(self):
        return f"Commented by {self.user.username} on {self.article.title}"
    
    class Meta:
        ordering = ['-date'] # Orders comments by date(newest first)
    
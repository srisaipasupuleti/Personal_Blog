from django import forms
from .models import Article, Tag

class ArticleForm(forms.ModelForm):
    tags=forms.CharField(required=False, help_text="tags separated by commas")
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        names = self.cleaned_data['tags'].split(",")
        if commit:
            instance.save()
            for name in names:
                name = name.strip()
                tag, created = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag)
                
        
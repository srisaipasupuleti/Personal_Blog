from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from django.http import HttpResponse
from .forms import ArticleForm
from django.urls import reverse


def home(request):
    articles = Article.objects.all().order_by('-date_published')
    return render(request, "blog/index.html", {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article,id=article_id)
    return render(request, "blog/article.html", {"article": article})

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            url = reverse('article_detail', args=[article.id])
            return redirect(url)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.delete()
        return redirect('dashboard')
    return render(request, 'blog/delete_article.html', {'article': article})


# @login_required
def dashboard(request):
    articles = Article.objects.all()
    return render(request, 'blog/dashboard.html', {'articles': articles})
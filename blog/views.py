from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Article, Comment, Tag
from django.http import HttpResponse
from .forms import ArticleForm
from django.urls import reverse


# def user_signup(request):
#     if request.method == "POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user = User.objects.create_user(username=username, password=password)
#         login(request, user)
#         return redirect(request.POST.get('next', 'home'))
#     return render(request, 'blog/signup.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # todo: let user know the reason of failed login/authentication
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             # ? why request.GET.get when request.method=='POST'
#             next_url = request.GET.get('next','home') if request.GET.get('next','home') else 'home'
#             return redirect(next_url)
#     return render(request, 'blog/login.html')

# def user_logout(request):
#     logout(request)
#     next_url = request.GET.get('next','home') if request.GET.get('next','home') else 'home'
#     return redirect(next_url)

# def guest_login(request):
#     guest_user, created = User.objects.get_or_create(username='guest_user')
#     login(request, guest_user)
#     next_url = request.GET.get('next','home') if request.GET.get('next','home') else 'home'
#     return redirect(next_url)


def home(request):
    articles = Article.objects.all().order_by('-date_published')
    tags = Tag.objects.all()
    return render(request, "blog/home.html", {'articles': articles, 'tags': tags})

def article_detail(request, article_id):
    article = get_object_or_404(Article,id=article_id)
    comments = Comment.objects.filter(article=article, parent=None)
    return render(request, "blog/article.html", {"article": article, "comments": comments})

@login_required
def add_comment(request, article_id):
    if request.method == "POST":
        article = get_object_or_404(Article, id=article_id)
        text = request.POST['text']
        if text:
            Comment.objects.create(article=article, user=request.user, text=text)
        return redirect('blog:article_detail',article_id=article_id)
    return redirect('home')

@login_required
def handle_like(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user
    if user in comment.liked_by.all():
        comment.liked_by.remove(user)
    else:
        comment.liked_by.add(user)
        
    if user in comment.disliked_by.all():
        comment.disliked_by.remove(user)
    return redirect(reverse('article_detail', args=[comment.article.id]))

@login_required
def handle_dislike(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user
    if user in comment.disliked_by.all():
        comment.disliked_by.remove(user)
    else:
        comment.disliked_by.add(user)
        
    if user in comment.liked_by.all():
        comment.liked_by.remove(user)
    
    return redirect(reverse('article_detail', args=[comment.article.id]))

@login_required
def handle_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    article = comment.article
    if request.method == "POST":
        text = request.POST.get('text')
        
        if text:
            Comment.objects.create(
                article=article, 
                user=request.user, 
                text=text,
                parent = comment
            )
        return redirect(request.GET.get('next', reverse('article_detail', args=[article.id])))
    else:
        return redirect('article_detail', article.id)
            
        
        

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            url = reverse('blog:article_detail', args=[article.id])
            return redirect(url)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.delete()
        return redirect('blog:home')
    return render(request, 'blog/delete_article.html', {'article': article})


# @login_required
def dashboard(request):
    articles = Article.objects.all()
    return render(request, 'blog/dashboard.html', {'articles': articles})


def tagged_articles(request, tag_id):
    tag, created = Tag.objects.get_or_create(id=tag_id)
    articles = Article.objects.filter(tags=tag.id)
    tags=[article.tags for article in articles]
    return render(request, 'blog/home.html', {"articles": articles})
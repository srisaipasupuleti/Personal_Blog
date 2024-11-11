from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
    path('blog_admin/', views.dashboard, name='dashboard'),
    path('blog_admin/add/', views.add_article, name='add_article'),
    path('blog_admin/article/<int:article_id>/edit', views.edit_article, name='edit_article'),
    path('blog_admin/article/<int:article_id>/delete', views.delete_article, name='delete_article'),
    # path('admin/delete/<int:id>', views.delete_article, name='delete_article'),
]
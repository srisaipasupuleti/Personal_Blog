from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # ? is it better to end paths with / ?
    path('', views.home, name='home'),
    # path('signup', views.user_signup, name='signup'),
    # path('login', views.user_login, name='login'),
    # path('logout',views.user_logout, name='logout'),
    # path('guest_login', views.guest_login, name='guest_login'),
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
    path('article/add', views.add_article, name='add_article'),
    path('article/edit/<int:article_id>', views.edit_article, name='edit_article'),
    path('article/delete/<int:article_id>', views.delete_article, name='delete_article'),
    path("tag/<int:tag_id>",views.tagged_articles,name='tagged_articles'),
    path('add_comment/<int:article_id>', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/like', views.handle_like, name='handle_like'),
    path('comment/<int:comment_id>/dislike', views.handle_dislike, name='handle_dislike'),
    path('comment/<int:comment_id>/reply', views.handle_reply, name='handle_reply'),
    # path('blog_admin', views.dashboard, name='dashboard'),
    # path('admin/delete/<int:id>', views.delete_article, name='delete_article'),
]
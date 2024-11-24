from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    # ? is it better to end paths with / ?
    # path('signup', views.user_signup, name='signup'),
    # path('login', views.user_login, name='login'),
    # path('logout',views.user_logout, name='logout'),
    # path('guest_login', views.guest_login, name='guest_login'),
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
    path('add_comment/<int:article_id>', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/like', views.handle_like, name='handle_like'),
    path('comment/<int:comment_id>/dislike', views.handle_dislike, name='handle_dislike'),
    path('comment/<int:comment_id>/reply', views.handle_reply, name='handle_reply'),
    path('blog_admin', views.dashboard, name='dashboard'),
    path('blog_admin/add', views.add_article, name='add_article'),
    path('blog_admin/article/<int:article_id>/edit', views.edit_article, name='edit_article'),
    path('blog_admin/article/<int:article_id>/delete', views.delete_article, name='delete_article'),
    # path('admin/delete/<int:id>', views.delete_article, name='delete_article'),
]
from django.urls import path
from . import views
from users import views as user_views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('login/',user_views.login,name= 'blog-login'),
    path('register/',user_views.login,name= 'blog-register'),
    path('about/', views.about, name='blog-about'),
    path('content/',views.content,name='blog-content'),
    path('politics/',views.politics_data,name='blog-politics'),
]
from django.urls import path
from . import views as user_views
#from blog_app import views

urlpatterns = [
    #path('login/', views.login, name='blog-login'),
    path('updated_home/', user_views.show_updated_home, name='updated-home-page'),
    path('add_content/',user_views.add_content,name='add-content'),
    path('logout/', user_views.show_logout, name='logout'),
    
]


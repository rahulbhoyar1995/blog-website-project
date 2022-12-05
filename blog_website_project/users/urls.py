from django.urls import path
from . import views

urlpatterns = [
    #path('login/', views.login, name='blog-login'),
    path('updated_home/', views.show_updated_home, name='updated-home-page'),
    path('logout/', views.show_logout, name='logout')
]

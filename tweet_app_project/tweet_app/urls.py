from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_display,name='tweet_display'),
    path('create_tweet/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit_tweet/', views.edit_tweet,name='edit_tweet'),
    path('<int:tweet_id>/delete_tweet/', views.delete_tweet,name='delete_tweet'),
    path('register/', views.register,name='register'),
    path('logout/', views.log_out_view,name='logout'),
    path('search/', views.search,name='search'),
    
]
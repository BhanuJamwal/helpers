from django.urls import path
from tweet import views

urlpatterns = [
	path('profile/', views.UserRedirect.as_view()),
	path('tweets/', views.tweets, name='tweets'),
	path('tweets/new/',views.new_tweet,name='new_tweet'),
	path('tweets/<tweets_id>/follow', views.follow, name="tweets_follow"),

    #path('follow/',views.follow,name='follow')
]
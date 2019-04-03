from django.urls import path

from Status import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/new/',views.new_board,name='new_board'),
    path('home/<pk>/', views.board_topics, name='board_topics'),
    path('home/<pk>/new/', views.new_topic, name='new_topic'),
    path('home/<pk>/topics/<topic_pk>/', views.topic_posts, name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),

]

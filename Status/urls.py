from django.urls import path

from Status import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/<pk>/', views.board_topics, name='board_topics'),
    path('home/<pk>/new/', views.new_topic, name='new_topic'),
    
]
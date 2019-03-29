from django.urls import path

from verification.views import home_view


urlpatterns = [
    path('home/', home_view.as_view()),
]
from django.urls import path
from onetime import views
app_name="onetime"
urlpatterns = [
    path('new/', views.NewView.as_view(), name='new'),
    path('new/create/', views.CreateView.as_view(), name='create'),
    path('new/verify/', views.VerifyView.as_view(), name='verify'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm')
]
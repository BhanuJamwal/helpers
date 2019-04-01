from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views


urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='/home/bhanu/project/helpers/accounts/templates/accounts/login.html'), name='login'),
    path('reset/',auth_views.PasswordResetView.as_view(
        template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_reset.html',
        email_template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_reset_email.html',
        subject_template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_reset_subject.txt'
    ),name='password_reset'),
	path('reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_reset_done.html'),
    name='password_reset_done'),
	path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_reset_confirm.html'),name='password_reset_confirm'),
	path('reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_reset_complete.html'),
    name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='/home/bhanu/project/helpers/accounts/templates/accounts/password_reset.html'),
        name='password_change_done'),

]
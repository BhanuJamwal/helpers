from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.
@csrf_exempt
def signup(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			auth_login(request,user)
			return redirect('/Status/home')
	else:
		form=SignUpForm()	
	return render(request, 'accounts/signup.html', {'form':form})
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

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

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

def validate_user(request):
	username=request.GET.get('username',None)
	data={
	'is_taken':User.objects.filter(username__iexact=username).exists()
	}
	return JsonResponse(data)

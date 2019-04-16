from django.shortcuts import render
from django.views.generic import DetailView,View,TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
import nexmo
from onetime .models import Phone
from django.conf import settings

# Create your views here.
class NewView(LoginRequiredMixin,DetailView):
	template_name="onetime/new.html"
	model=Phone

	def get_object(self):
		try:
			return self.request.user.phone
			#if Phone.objects.filter(user=self.request.user).exists():
			#	return self.request.user
		except Phone.DoesNotExist:
			return Phone.objects.create(user=self.request.user)

class CreateView(LoginRequiredMixin,View):
	def post(self,request):
		number=self.find_or_set_number(request)
		response=self.send_verification_request(request,number)
		if (response['status'] == '0'):
			request.session['verification_id'] = response['request_id']
			return HttpResponseRedirect(reverse('onetime:verify')+"?next="+request.POST['next'])
		else:
			logout(request)
			messages.add_message(request, messages.INFO, 'Could not verify your number. Please contact support.')
			return HttpResponseRedirect('/Status/home')

	def find_or_set_number(self, request):
		two_factor = request.user.phone

		if (not two_factor.phone_number):
			two_factor.phone_number = request.POST['number']
			two_factor.save()
 
		return two_factor.phone_number
 
	def send_verification_request(self, request, number):
		client = nexmo.Client(key='26942665',secret='C8SRPIXatgidi3rj')
		return client.start_verification(number=number, brand='helpers')

class VerifyView(LoginRequiredMixin,TemplateView):
	template_name="onetime/verify.html"


class ConfirmView(LoginRequiredMixin, View):
	def post(self, request):
		response = self.check_verification_request(request)

		if (response['status'] == '0'):
			request.session['verified'] = True
			return HttpResponseRedirect('/Status/home')
		else:
			messages.add_message(request, messages.INFO, 'Could not verify code. Please try again.')
			return HttpResponseRedirect(reverse('onetime:verify')+"?next="+request.POST['next'])


	def check_verification_request(self, request):
		return nexmo.Client(key='26942665',secret='C8SRPIXatgidi3rj').check_verification(request.session['verification_id'], code=request.POST['code'])


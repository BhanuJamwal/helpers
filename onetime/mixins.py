from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse

class TwoFactorMixin(UserPassesTestMixin):
	def test_func(self):
		user=self.request.user
		return(user.is_authenticated and "verified" in self.request.session)

	def get_login_url(self):
		if(self.request.user.is_authenticated):
			return reverse("onetime:new")
		else:
			return reverse("login")
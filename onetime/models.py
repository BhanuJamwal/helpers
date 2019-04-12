from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Phone(models.Model):
	user=models.OneToOneField(User,on_delete=models.PROTECT)
	phone_number=models.CharField(max_length=16)

	def __str__(self):
		return self.phone_number

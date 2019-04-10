from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.CharField(max_length=50,unique=True)
	text = models.CharField(max_length=160)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text



class Follow(models.Model):
	following = models.ForeignKey(User, related_name="who_follows",unique=True,on_delete=models.PROTECT)
	follower = models.ForeignKey(User, related_name="who_is_followed",on_delete=models.PROTECT)
	follow_time = models.DateTimeField(auto_now_add=True)
	count = models.IntegerField(default=1)

	def __unicode__(self):
		return str(self.follow_time)
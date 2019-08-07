from django.db import models

from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
	age = models.IntegerField(null=True)
	score = models.DecimalField(max_digits=10,decimal_places=4, default=1.0)

	num_bought = models.IntegerField(default=0)
	num_added = models.IntegerField(default=0)
	num_discarded = models.IntegerField(default=0)


	def __str__(self):
		return self.username


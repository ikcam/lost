from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):
	name = models.CharField(max_length=255)
	phone = models.IntegerField(unique=True)
	email = models.EmailField(max_length=255)
	address = models.CharField(max_length=255)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('id',)

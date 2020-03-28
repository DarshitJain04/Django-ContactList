from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class List(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = PhoneNumberField() 

	def __str__(self):
		return f'{self.firstname} {self.lastname}'



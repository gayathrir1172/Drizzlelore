from django.db import models
from django import forms
from django.forms import ModelForm
# Create your models here.
class createEvent(models.Model):
	FirstName = models.CharField(max_length=150)
	LastName = models.CharField(max_length=150)
	EventName = models.CharField(max_length=150)
	EventOrganizer = models.CharField(max_length=150)
	Location = models.CharField(max_length=200)
	Date = models.DateField()
	LastDateOfRegistration = models.DateField()
	EventDetails = models.TextField()
	#UploadFiles = models.FileField(upload_to)		

	def __str__(self):
		return u'%s %s %s %s %s %s %s %s' %(self.FirstName,self.LastName,self.EventName,self.EventOrganizer,self.Location,self.Date,self.LastDateOfRegistration,self.EventDetails)

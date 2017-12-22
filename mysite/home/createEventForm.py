from django import forms
from .models import createEvent

class createEventForm(forms.ModelForm):
	class Meta:
		model = createEvent
		fields = [
			'FirstName',
			'LastName',
			'EventName',
			'EventOrganizer',
			'Location',
			'Date',
			'LastDateOfRegistration',
			'EventDetails',
#			'UploadFiles',
		]
	def __init__(self,*args,**kwargs):
		super(createEventForm,self).__init__(*args,*kwargs)
		self.fields['FirstName'].help_text = ''
		self.fields['LastName'].help_text = ''
		self.fields['EventName'].help_text = ''
		self.fields['EventOrganizer'].help_text = ''
		self.fields['Location'].help_text = ''
		self.fields['Date'].help_text = 'Enter in the format yyyy-mm-dd'
		self.fields['LastDateOfRegistration'].help_text = 'Enter in the format yyyy-mm-dd'
		self.fields['EventDetails'].help_text = ''
		#self.fields['EventDetails'].initial = 'Enter your details about the event'

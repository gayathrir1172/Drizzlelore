from django.shortcuts import render,HttpResponse
from . import createEventForm
from .models import createEvent
# Create your views here.
def home_view(request):
	title = "Drizzlelore"
	subtitle = "Welcome "
	uname = request.user.username
	if uname == "AnonymousUser":
		uname = " "
		print (uname)
		context = {
			"title":title,
			"subtitle":subtitle,
			"uname":uname,
		}
		return render(request,"home/index.html",context)
	else:
		print (uname)
		context = {
			"title":title,
			"subtitle":subtitle,
			"uname":uname,
		}
		return render(request,"home/index.html",context)
	#return render(request,"home/index.html",context)

def view_event(request):
	title = "Drizzlelore"
	subtitle = "Event List"
	print("View events")
	data = createEvent.objects.all()
	#edata = {
	#	"id" : data,
	#}
	context = {
		"title":title,
		"subtitle":subtitle,
		"id" : data,
	}
	return render(request,"home/viewevents.html",context)

def create_event(request):
	title = "Drizzlelore"
	subtitle = "Create event"
	if request.method == "POST":
		form = createEventForm.createEventForm(request.POST)
		print(form.errors)
		if form.is_valid():
			print()
			print()
			#event_id = form.cleaned_data.get('id')  
			#print("id is "+event_id)
			fname = form.cleaned_data.get('FirstName')
			print("fname is "+fname)
			lname = form.cleaned_data.get('LastName')
			print("fname is "+lname)
			eventName = form.cleaned_data.get('EventName')
			print("event name is "+eventName)
			eventOrganizer = form.cleaned_data.get('EventOrganizer')
			print("event organizer is "+eventOrganizer)
			location = form.cleaned_data.get('Location')
			print("loc is "+location)
			date = form.cleaned_data.get('Date')
			print(date)
			lastDateofReg = form.cleaned_data.get('LastDateOfRegistration')
			print(lastDateofReg)
			eventDetails = form.cleaned_data.get('EventDetails')
			print("event details is "+eventDetails)
			#form.save(commit=False)
			#print("form.save executed successfully")
			#print()
			#print()
		#uploadFile = form.cleaned_data.get('UploadFile')
			event = createEvent(FirstName=fname,LastName=lname,EventName=eventName,EventOrganizer=eventOrganizer,Location=location,Date=date,LastDateOfRegistration=lastDateofReg,EventDetails=eventDetails)
			event.save()
			context = {
	 	 		"title":title,
	    		"subtitle":subtitle,
	     		"form" : form,
			}
			return HttpResponse("Success form submitted")
		else:
			print("Not valid form..............")
			return HttpResponse("Failure")
	else:
		form = createEventForm.createEventForm() 
	context = {
	 	"title":title,
	    "subtitle":subtitle,
	    	"form":form,
	}
	return render(request,"home/createevents.html",context)

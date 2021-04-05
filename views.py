from django.shortcuts import render,HttpResponseRedirect
from .models import Profile
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages

#function to add data in database
def add_show(request):
	if request.method=="POST":
		em=request.POST.get('fname')
		nm=request.POST.get('slider_value')
		reg=Profile.objects.create(name=em,value=nm)
		reg.save()
		messages.success(request, 'Data submitted successful')
          
	
	return render(request,'enroll/addandshow.html')
#function to fetch data from database
def update_data(request):
	stud=Profile.objects.all()
	print(stud)
	return render(request,'enroll/showdata.html',{'stu':stud})
		

from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


@login_required(login_url='login')
def list(request):
	contact = List.objects.all()
	form = ListForm()
	if request.method == 'POST':
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ListForm()

	context = {'form':form , 'contacts':contact}
	return render(request,'list/home.html',context)

@login_required(login_url='login')
def editcontact(request,pk):
	contact = List.objects.get(id=pk)
	form = ListForm(instance=contact)
	if request.method == 'POST':
			form = ListForm(request.POST ,instance=contact)
			if form.is_valid():
				form.save()
			return redirect('/') 

	context = {'form':form}
	return render(request, 'list/edit.html',context)	

@login_required(login_url='login')
def deletecontact(request,pk):
	item = List.objects.get(id=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('/') 

	context = {'item':item}
	return render(request,'list/delete.html',context)			

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created!You are now able to login!')
			return redirect('login')
	else:		
		form = RegistrationForm()

	return render(request,'list/register.html',{'form':form})

def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username or password is incorrect!')
	return render(request,'list/login.html')


@login_required(login_url='login')
def logoutpage(request):
	logout(request)
	return redirect('login')

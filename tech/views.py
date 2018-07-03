# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def service(request):
	return render(request,'service.html')

def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)

		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['trevelynjune@gmail.com'])
			except BadHeaderError:
				return HttpResponse('invalid header found.')
			return redirect('success')
	return render(request,'contact.html', {'form' : form})

def team(request):
	return render(request, 'team.html')


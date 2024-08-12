from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse


from .forms import ContactForm

def index(request):
	"""The home page for Portfolio"""

	return render(request, 'portfolio/index.html')

def about(request):
	return render(request, 'portfolio/about.html')

def project(request):
	return render(request, 'portfolio/project.html')

def pricing(request):
	return render(request, 'portfolio/pricing.html')

def contact(request):
	if request.method == 'GET':
		form = ContactForm()
		context = {'form': form}
		return render(request, 'portfolio/contact.html', context)

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']

			'''template = render_to_string("email_template.html", {'name': name,
			'email':email, 'subject':subject, 'message':message})

			mail = EmailMessage(
				subject,
				email,
				name,
				message,
				settings.EMAIL_HOST_USER,
				['jesseakilaayams@gmail.com']
			)
			mail.send()'''

			# send email
			send_mail(
				f'Contact Form Submission - {subject}',
				f'Name: {name}\nEmail: {email}\nMessage: {message}',
				email,
				['jesseakilaayams@gmail.com'],
				fail_silently=False,
			)
			#return HttpResponse("Submitted Successfully...")
			return HttpResponseRedirect('/contact/success/')

def form_success(request):
	return render(request, 'portfolio/form_success.html')
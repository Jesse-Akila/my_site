"""Defines URL patterns for portfolio"""

from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
	# Home
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('project/', views.project, name='project'),
	path('pricing/', views.pricing, name='pricing'),
	path('contact/', views.contact, name='contact'),
	path('contact/success/', views.form_success, name='form_success'),
]
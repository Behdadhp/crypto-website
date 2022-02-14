from django.shortcuts import render
from . import models
from django.views import generic
from django.contrib.auth.models import LoginRequiredMixin
# Create your views here.



class SubmittedPage(generic.TemplateView, LoginRequiredMixin):
    template_name = 'templates/submitted.html'

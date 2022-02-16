from django.shortcuts import render
from . import models
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
from accounts.models import User
from .forms import ContactUsForm


class SubmittedPage(generic.TemplateView, LoginRequiredMixin):
    template_name = 'about/submitted.html'

class ContactUsCreateView(generic.CreateView, LoginRequiredMixin):

    model = models.ContactUs
    form_class = ContactUsForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

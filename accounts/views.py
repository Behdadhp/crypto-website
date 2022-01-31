from django.shortcuts import render
from  django.urls import reverse_lazy
from django.views.generic import (CreateView,TemplateView,
                                  UpdateView,ListView,)
from . import forms
from . import models
from market.models import Market

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/SignUp.html"

class ProfilePage(TemplateView):
    template_name="accounts/profile_page.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UpdateProfilePage(UpdateView):
    model = models.User
    fields= ('first_name','last_name','email','username')
    template_name = 'accounts/update_form.html'
    success_url = reverse_lazy("accounts:your_profile")

    def get_object(self):
        return self.request.user

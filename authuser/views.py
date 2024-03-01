from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .froms import SignUpForm

from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')
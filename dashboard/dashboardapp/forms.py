from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class generatee(forms.ModelForm):

    class Meta:
        model = generate
        fields = '__all__'
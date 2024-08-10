from django import forms
from django.forms import FileInput, ImageField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # removendo a opção de Password-based authentication
        if 'usable_password' in self.fields:
            del self.fields['usable_password']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
    
    image = forms.ImageField(widget=FileInput)

    class Meta:
        model = Profile
        fields = ['bio', 'image']

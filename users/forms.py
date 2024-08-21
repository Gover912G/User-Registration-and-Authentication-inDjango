from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django  import forms
from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput

# this for registering a user
class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# this for authenicatig the user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget= PasswordInput())
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegister(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.CharField(label='Email Address')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    dateofbirth = forms.DateField(label='Date of birth', widget=DateInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'dateofbirth',
            'email',
        ]

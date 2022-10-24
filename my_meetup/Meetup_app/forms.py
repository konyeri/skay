from .models import Meetup, MyUser, Participant, Speaker
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea, PasswordInput,DateTimeInput, DateInput
#from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, CheckBoxInput





class UserMeetupForm(forms.ModelForm):
    class Meta:
        model=Meetup
        fields=['title', 'from_date', 'to_date', 'meetup_time', 'description', 'organizer_email', 'location_name','location_address', 'activate', 'image']
       #fields='__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Participant
        fields=['email']
        widgets={
            'email':TextInput(
                attrs={
                    'placeholder':'Enter Your Email',
                    'class':'form-control w-50'
                }

            )
            }

class MyUserRegistration(UserCreationForm):
    class Meta:
        model=MyUser
        fields=['name', 'username', 'email', 'password1', 'password2']
        widgets={
            'name':TextInput(
                attrs={
                    'placeholder':'Enter your name',
                    'class':'form-control'
                }
            ),
            'username':TextInput(
                attrs={
                    'placeholder':'Enter your username',
                    'class':'form-control'
                }
            ),
            'email':TextInput(
                attrs={
                    'placeholder':'Enter your email',
                    'class':'form-control'
                }
            ),
            'password1':PasswordInput(
                attrs={
                    'placeholder':'Enter your password',
                    'class':'form-control'
                }
            ),
            'password2':PasswordInput(
                attrs={
                    'placeholder':'Enter your password',
                    'class':'form-control'
                }
            )

        }

class SpeakerForm(forms.ModelForm):
    class Meta:
        model=Speaker
        fields=['name', 'email', 'phone', 'bio', 'image']
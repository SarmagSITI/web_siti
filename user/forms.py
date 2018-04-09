from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea, ValidationError, ModelForm, TextInput
from django.forms.fields import Field
from .models import UserProfile
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='Username',
        widget=TextInput(attrs={'style': 'text-transform:lowercase;'})
    )
    first_name = forms.CharField(
        required=True,
        label='Nama Depan',
        widget=TextInput(attrs={'style': 'text-transform:uppercase;'})
    )
    last_name = forms.CharField(
        required=False,
        help_text='Optional.',
        label='Nama Belakang',
        widget=TextInput(attrs={'style': 'text-transform:uppercase;'})
    )
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean_mail(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("email telah terdigunakan")
        return email

class SignUpAddition(forms.ModelForm):
    phone = PhoneNumberField(help_text='Gunakan +62.',)
    class Meta:
        model = UserProfile
        fields = ('gender', 'phone',)

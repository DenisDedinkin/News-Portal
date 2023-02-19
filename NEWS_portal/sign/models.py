from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        commons_group = Group.objects.get(name='commons')
        commons_group.user_set.add(user)
        return user

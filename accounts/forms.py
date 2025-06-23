from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PortfolioProject


class LoginForm(forms.Form):
    username = forms.CharField(label="Введіть нікнейм", widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = ['title', 'description', 'screenshot', 'link', 'file']

    def clean(self):
        cleaned_data = super().clean()
        link = cleaned_data.get("link")
        file = cleaned_data.get("file")
        screenshot = cleaned_data.get("screenshot")


        # Check if at least one of media (link, file, or screenshot) is provided
        if not link and not file and not screenshot:
            raise forms.ValidationError("You must provide at least one of a link, a file, or a screenshot.")

        return cleaned_data



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


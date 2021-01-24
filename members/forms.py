from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'field', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "field"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password1"].widget.attrs["class"] = "field"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["class"] = "field"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'field'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'field'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class': 'field'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
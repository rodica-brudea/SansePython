from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import TextInput, Select, PasswordInput, HiddenInput, CharField


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email', 'username']

        widgets = {
            "username": TextInput(attrs={"placeholder": "Username", "class": "form-control"}),
            "first_name": TextInput(attrs={"placeholder": "First name", "class": "form-control"}),
            "last_name": TextInput(attrs={"placeholder": "Last name", "class": "form-control"}),
            "password": PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}),
            "email": TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        field_data = self.cleaned_data
        username_value = field_data.get('username')
        if self.pk:
            if User.objects.filter(username=username_value).exclude(id=self.pk).exists():
                self._errors['username'] = self.error_class(["Username-ul deja exista! "
                                                             "Te rugam sa alegi alte valori"])
        else:
            if User.objects.filter(username=username_value).exists():
                self._errors['username'] = self.error_class(["Username-ul deja exista! "
                                                          "Te rugam sa alegi alte valori"])
        return field_data

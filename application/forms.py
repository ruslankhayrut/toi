from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput())
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', required=True, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')

        try:
            User.objects.get(email=email)
            msg = 'User with this email address already exists'
            self.add_error('email', msg)
        except ObjectDoesNotExist:
            pass


        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)

        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)

        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)

        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                msg = "The two password fields must match."
                self.add_error('password', msg)
        return cleaned_data
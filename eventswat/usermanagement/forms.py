from django import forms
from django.contrib.auth.models import User
from usermanagement.models import Userprofile
from events.models import EventsSubCategory

GENDER_CHOICES = (('male', 'Male'),	('female', 'Female'), )
USER_TYPE_CHOICES = (('institution', 'Institution'),
                     ('organization', 'Organization'),
                     ('corporate', 'Corporate'), )


class UserCreationForm(forms.ModelForm):
    """
    This Form is used for User's Registeration
    """

    username = forms.CharField(widget=forms.TextInput(), required=True,
                               error_messages={'required': 'Field is required',
                                               'invalid': 'Field is invalid'})
    email = forms.EmailField(widget=forms.EmailInput, required=True,
                             error_messages={'required': 'Field is required',
                                             'invalid': 'Field is invalid'})
    password = forms.CharField(widget=forms.PasswordInput, required=True,
                               error_messages={'required': 'Field is required',
                                               'invalid': 'Field is invalid'})
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True,
                                       error_messages={'required': 'Field is required',
                                                       'match': 'password does not matched'})

    mobile = forms.CharField(widget=forms.TextInput, required=True,
                             error_messages={'required': 'Field is required',
                                             'invalid': 'Field is invalid'})

    class Meta:
        model = Userprofile
        fields = ('username', 'email', 'mobile',
                  'password', 'confirm_password')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """
    This Form is used  for User's Login
    """
    login_email = forms.EmailField(widget=forms.EmailInput, required=True,
                                   error_messages={'required': 'Field is required',
                                                   'invalid': 'Field is invalid'})
    login_password = forms.CharField(widget=forms.PasswordInput, required=True,
                                     error_messages={'required': 'Field is required',
                                                     'invalid': 'Field is invalid'})

    class Meta:
        fields = ('login_email', 'login_password')

from django import forms
from reviews.models import *


class WebsiteFeedbackForm(forms.Form):

   	name = forms.CharField(
		# max_length=254,
		widget=forms.TextInput(),
		required=True,
		error_messages={'required': 'Field is required', 'invalid':'Field is invalid'},
	)
	
	email = forms.EmailField(widget=forms.EmailInput, required=True, error_messages={'required': 'Field is required', 'invalid':'Field is invalid'})
	comments = forms.CharField(required=True,error_messages={'required': 'Field is required', 'invalid':'Field is invalid'},)
	rating = forms.IntegerField(required=True,error_messages={'required': 'Field is required', 'invalid':'Field is invalid'},)

	class Meta:
		model = WebsiteFeedback
		# fields = ('username',)
		fields = ('name','email','mobile', 'comments', 'rating')	


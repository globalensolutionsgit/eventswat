from django import forms
from reviews.models import *

class WebsiteFeedbackForm(forms.ModelForm):

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
        fields = ('name','email', 'comments', 'rating')  


class CommentForm(forms.ModelForm):
    #Hidden value to get a child's parent
    content = forms.CharField(required=True, error_messages={'required': 'Field is required', 'invalid':'Field is invalid'})
    rating = forms.IntegerField(required=True, error_messages={'required': 'Field is required', 'invalid':'Field is invalid'})

    parent = forms.CharField(widget=forms.HiddenInput(
                            attrs={'class': 'parent'}), required=False)
    
    class Meta:
        model = Comment
        fields = ('content','rating',)

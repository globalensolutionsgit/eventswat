import datetime
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from events.models import *
from datetime import datetime
from django import forms
from postevent.models import Postevent

class WebsiteFeedback(models.Model):
	name= models.CharField(max_length=50, null=True)
	email= models.EmailField(max_length=50)
	comments= models.TextField()
	rating=models.IntegerField()  

 
class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    path = models.CharField(blank=True, max_length=500, editable=False)
    depth = models.PositiveSmallIntegerField(default=0)
    postevent = models.ForeignKey(Postevent)

    def __unicode__(self):
        return self.content 
    
class CommentForm(forms.ModelForm):
    #Hidden value to get a child's parent
    parent = forms.CharField(widget=forms.HiddenInput(
                            attrs={'class': 'parent'}), required=False)
    
    class Meta:
        model = Comment
        fields = ('content',)


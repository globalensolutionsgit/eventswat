import datetime
import uuid
from eventswat.models import *

from django.db import models
from uuid import uuid4
from uuid import UUID
from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User

class PayuDetails(models.Model):
    mihpayid = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    txnid=models.CharField(max_length=50, null=True, blank=True)
    amount =models.FloatField(default=0.0,null=True, blank=True)
    productinfo=models.CharField(max_length=500, null=True, blank=True)
    error_Message =models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.mihpayid








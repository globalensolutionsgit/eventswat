from django.db import models

LOG_STATUS = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('process', 'Process'),
    ('reopen', 'Re-Open'),
)    

class ErrorLog(models.Model):
    level = models.CharField(max_length=200)
    error_msg = models.TextField()
    page = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    datetime = models.DateTimeField(null=True, blank=True)
    admin_status = models.CharField(max_length=10, default='open', choices=LOG_STATUS, help_text="Admin note of error log.")

    def __unicode__(self):
        return self.error_msg
    
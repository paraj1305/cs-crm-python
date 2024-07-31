

from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.apps import apps




class Leave(models.Model):
   
    employee = models.ForeignKey('superadmin.Employee', on_delete=models.CASCADE)
    leave_date = models.DateField()
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    leave_reason = models.CharField(max_length=255)
    status_choices = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"Leave ID: {self.id} - {self.employee.username} from {self.start_date} to {self.end_date}"

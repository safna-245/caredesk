
from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):

    COMPLAINT_TYPE = [
        ('Cleanliness', 'Cleanliness'),
        ('Staff Behavior', 'Staff Behavior'),
        ('Waiting Time', 'Waiting Time'),
        ('Billing', 'Billing'),
        ('Equipment', 'Equipment'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Under Review', 'Under Review'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    complaint_type = models.CharField(
        max_length=30,
        choices=COMPLAINT_TYPE
    )
    department = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Submitted'
    )
    reported_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='complaints'
    )

    def __str__(self):
        return self.title



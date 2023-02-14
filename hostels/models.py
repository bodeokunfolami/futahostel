from django.db import models
from django.urls import reverse
from users.models import StudentProfile

# Create your models here.
class Hostel(models.Model):
    class Meta:
        db_table = 'hostels'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("users:app_detail", kwargs={"id": self.pk})
    
    
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    beds = models.PositiveIntegerField()
    pirce = models.CharField(max_length=20, blank=True, null=True)
    hostel_type = models.CharField(max_length=1, default='M', choices=CHOICES)
    location = models.CharField(max_length=200, blank=True, null=True)

class HostelApplication(models.Model):
    class Meta:
        db_table = 'hostel_apps'

    STATUSES = (
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('N', 'Not Approved')
    )
    beds = models.PositiveIntegerField(default=1)
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    hostel = models.OneToOneField(Hostel, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='P', choices=STATUSES)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student.user.username
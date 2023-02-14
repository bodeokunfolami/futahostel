from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentProfile(models.Model):
    class Meta:
        db_table = 'student_profiles'

    CHOICES = (
        ('N', 'No Appplication'),
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('R', 'Rejected')
    )

    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    LEVELS = (
        ('100', '100L'),
        ('200', '200L'),
        ('300', '300L'),
        ('400', '400L'),
        ('500', '500L')
    )

    SCHOOLS = (
        ('SEET', 'School of Eng. and Eng. Tech.'),
        ('SOS', 'School of Sci.'),
        ('SAAT', 'School of Agric. and Agric. Tech.'),
        ('SET', 'School of Environmental Tech.'),
        ('SEMS', 'School of Earth and Mineral Sci.'),
        ('SAMT', 'School of Management Tech.'),
        ('SHHT', 'School of Health and Health Tech.'),
        ('SOC', 'School of Computing')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    hostel = models.ForeignKey('hostels.Hostel', on_delete=models.CASCADE, blank=True, null=True)
    matric_no = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='', 
        width_field='width_field', height_field='height_field', blank=True, null=True)
    width_field = models.PositiveIntegerField(default=0)
    height_field = models.PositiveBigIntegerField(default=0)
    telephone = models.CharField(max_length=11, blank=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    level = models.CharField(max_length=3, choices=LEVELS, blank=True)
    school = models.CharField(max_length=4, choices=SCHOOLS, blank=True, null=True)
    gender = models.CharField(max_length=1, default='M', choices=GENDERS)
    status = models.CharField(max_length=1, default='N', choices=CHOICES)
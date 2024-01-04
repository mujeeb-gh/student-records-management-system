from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    matric_number = models.CharField(primary_key=True, max_length=50)
    full_name = models.CharField(max_length=255)
    passport_photo = models.ImageField(upload_to='passport_photos/', null=True, blank=True)
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    cgpa = models.FloatField()
    
    def __str__(self):
      return self.full_name


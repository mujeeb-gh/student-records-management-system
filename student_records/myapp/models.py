# Create your models here.
from django.db import models

class Student(models.Model):
  id = models.AutoField(primary_key=True, null=False)
  matric_number = models.CharField(unique=True, max_length=20, null=False)
  full_name = models.CharField(max_length=255, null=False)
  passport_photo = models.ImageField(upload_to='passport_photos/', null=False)
  department = models.CharField(max_length=40, null=False)
  college = models.CharField(max_length=40, null=False)
  cgpa = models.FloatField(null=False)
  gender = models.CharField(max_length=10, null=False)
  age = models.IntegerField(null=False)
  date_of_birth = models.DateField(null=False)
  contact_no = models.CharField(max_length=15, null=False)
  address = models.CharField(null=False, max_length=100)
  email = models.EmailField(null=False)
  nationality = models.CharField(null=False, max_length=50)
  state = models.CharField(null=False, max_length=20)
  
  def __str__(self):
    return self.full_name


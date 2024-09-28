from django.db import models

# Create your models here.


class students(models.Model):
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=200)
    DOB = models.DateField()
    blood_group = models.CharField(max_length=3)
    father_name = models.CharField(max_length=50)
    ph_no = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

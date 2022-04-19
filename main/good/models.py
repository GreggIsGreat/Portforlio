from django.db import models


# Create your models here.

class Portfolio(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(unique=True, null=True, blank=True)
    Physical_Address = models.CharField(max_length=200)
    user_type = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    Gender = models.CharField(max_length=200,choices=user_type)
    Postal_Address = models.CharField(max_length=200)
    Name_of_Parent = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name
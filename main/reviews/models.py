from django.db import models
# Create your models here.
from good.models import Portfolio


class Review(models.Model):
    Name = models.ForeignKey(Portfolio, max_length=200, on_delete=models.CASCADE)
    performance_type = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

    )
    Performance = models.CharField(max_length=200,choices=performance_type )

    def __str__(self):
        return self.Performance


from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=25)
    description = models.CharField(max_length=150, null=True)
    year = models.CharField(max_length=20)

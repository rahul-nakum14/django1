from django.db import models

class helomodel(models.Model):
    name = models.CharField(max_length=130)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=True) 
from django.db import models

class NewYearPainting(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    keywords = models.CharField(max_length=100)

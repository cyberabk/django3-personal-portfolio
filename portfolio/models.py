from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "portfolio/images/")
    utl = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Package(models.Model):
     name = models.CharField(max_length=150)
     description = models.TextField(max_length=500)
     main_viewpoint=models.CharField(max_length=100)
     price = models.DecimalField(max_digits=10, decimal_places=3)
     duration = models.PositiveIntegerField(help_text="Duration in days")
     media_gallery = models.ImageField(upload_to="gallry/", null=True,blank=True,default=None)
     is_approved=models.BooleanField(default=False)

class Vendor(models.Model):
    company_name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20) 
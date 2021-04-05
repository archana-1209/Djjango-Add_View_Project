from django.db import models

# Create your models here.
class Profile(models.Model):
	name=models.CharField(max_length=70)
	value=models.IntegerField(default=0)
	
	
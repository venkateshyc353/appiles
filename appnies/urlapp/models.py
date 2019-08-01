from django.db import models

# Create your models here.
class url_model(models.Model):
    url=models.CharField(max_length=200)
    empolyer=models.CharField(max_length=100,default='appnies')

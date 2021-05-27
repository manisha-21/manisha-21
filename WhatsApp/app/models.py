from django.db import models
import datetime

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    msg = models.TextField(max_length=50)
    image = models.ImageField()
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    

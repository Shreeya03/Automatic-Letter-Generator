from django.db import models
from django.contrib.auth.models import User

class generate(models.Model):
    choice=(
        ('Email','Email'),
        ('Certificate','Certificate'),
        ('Letter','Letter'),
    )
    index=models.IntegerField()
    
    choicee=models.CharField(max_length=200,null=True,choices=choice)
    

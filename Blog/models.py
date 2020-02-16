from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    Title=models.CharField(max_length=200)
    Content=models.TextField()
    Date_Posted=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return  self.Title



    def get_absolute_url(self):
        return reverse("post-detail",kwargs={"pk":self.pk})




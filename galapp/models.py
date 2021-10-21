from django.contrib.auth.models import User
from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=50, blank=True, unique=True)
    image = models.ImageField(upload_to="images/")
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    location = models.FilePathField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
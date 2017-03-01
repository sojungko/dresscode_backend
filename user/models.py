from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    profile_pic = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

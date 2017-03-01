from django.db import models

class Picture(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.url

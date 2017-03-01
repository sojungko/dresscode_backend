from django.db import models

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.commenter + ' says ' + self.content
    

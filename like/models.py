from django.db import models

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    liked = models.BooleanField()

    def __str__(self):
        if self.liked == True:
            return self.liker + ' liked ' + self.picture
        elif self.liked == None:
            return self.liker + " hasn't liked " + self.picture
        else:
            return self.liker + ' disliked ' + self.picture

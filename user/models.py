from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    profile_pic = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Picture(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.url
        
class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.commenter + ' says ' + self.content
    
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
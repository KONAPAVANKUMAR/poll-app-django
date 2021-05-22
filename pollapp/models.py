from django.db import models

# Create your models here.
class PollModel(models.Model):
    question = models.CharField(max_length  = 50)
    upvotes = models.CharField(max_length= 50,default=0)
    downvotes = models.CharField(max_length= 50,default=0)
    
    def __str__(self):
        return self.question
    def __init__( self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        try:
            self.upvote_percentage = int(self.upvotes)*100/(int(self.downvotes)+int(self.upvotes))
            self.downvote_percentage = int(self.downvotes)*100/(int(self.downvotes)+int(self.upvotes))
        except:
            self.upvote_percentage = 0
            self.downvote_percentage = 0

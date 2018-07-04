from django.db import models

# Create your models here.

class TypingMaster(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()    
                 
    def __str__(self):
        return self.title
    
    def save_it(self):
        self.save()

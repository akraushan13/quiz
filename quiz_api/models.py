from django.db import models
from django.utils import timezone

# Create your models here.


class Quiz(models.Model):

    question = models.TextField()
    options = models.JSONField()
    right_answer = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10,default='inactive')
    
    def save(self, *args, **kwargs):
        if self.status == 'inactive' and self.start_date <= timezone.now():
            self.status = 'active'
        elif self.status == ('active'or 'inactive') and self.end_date <= timezone.now():
            self.status = 'finished'
        super().save(*args, **kwargs)
